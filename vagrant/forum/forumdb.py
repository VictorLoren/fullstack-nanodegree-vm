#
# Database access functions for the web forum.
#

import time
import psycopg2



## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    # Database connection and fetch all results
    DB = psycopg2.connect("dbname=forum")
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM posts ORDER BY time DESC")
    results = cursor.fetchall()
    # Get a proper list to be returned
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in results]
    posts.sort(key=lambda row: row['time'], reverse=True)
    # Close connection and return list
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    t = time.strftime('%c', time.localtime())
    # Database connection and insert
    DB = psycopg2.connect("dbname=forum")
    cursor = DB.cursor()
    cursor.execute("INSERT INTO posts (content,time) VALUES ('%s','%s')"
        %(content,t))
    DB.commit()
    DB.close()
