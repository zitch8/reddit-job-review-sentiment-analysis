import praw
import os
from dotenv import load_dotenv

class RedditClient:
    def __init__(self):
        load_dotenv(dotenv_path = '.env')
        self.reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_CLIENT_USER_AGENT')
        )

    def get_instance(self):
        return self.reddit