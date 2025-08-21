import os
from dotenv import load_dotenv

import praw

load_dotenv(dotenv_path = '../.env')

def create_reddit_instance():
    
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_CLIENT_USER_AGENT')
    )

    return reddit