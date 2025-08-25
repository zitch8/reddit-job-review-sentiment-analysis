from reddit import reddit_scraper

# Define the query to search for job-related posts in the Philippines
# query = "job review Philippines OR job review PH OR entry level job review Philippines OR entry level job review PH"

company = "P&G Philippines Software Developer"
query = f"{company} job review"
print (query)

def fetch_job_reviews(reddit_instance):
    subreddit = reddit_instance.subreddit('all')
    
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

