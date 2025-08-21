from config import reddit_loader
import scraper

if __name__ == "__main__":
    reddit_instance = reddit_loader.create_reddit_instance()
    scraper.fetch_job_reviews(reddit_instance)
    