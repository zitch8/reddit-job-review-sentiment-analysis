import os
from dotenv import load_dotenv

import praw

load_dotenv(dotenv_path='.env')

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_CLIENT_USER_AGENT')
)

# Define the query to search for job-related posts in the Philippines
query = "job review Philippines OR job review PH OR entry level job review Philippines OR entry level job review PH"

subreddit = reddit.subreddit('all')
for submission in subreddit.search(query, sort='relevance', time_filter='all', limit=10):
    print(f"Title: {submission.title}")
    print(f"URL: {submission.url}")
    print(f"Score: {submission.score}")
    print(f"Created at: {submission.created_utc}")
    print(f"Author: {submission.author}\n")
    print("-----")

    # Fetch all comments for the submission
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list()[:5]:
        print(f"Comment by {comment.author}: {comment.body}")
        print(f"Score: {comment.score}")
        print("-----")

