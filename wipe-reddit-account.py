# built in packages: os.environ for getting environental variables (secrets) and chain to combine lists of comments and posts
from os import environ
from itertools import chain

# reddit API wrapper
import praw

# create a reddit instance using environment variables for authentication
reddit = praw.Reddit(
    client_id=environ.get('REDDIT_CLIENT_ID'),
    client_secret=environ.get('REDDIT_CLIENT_SECRET'),
    password=environ.get('REDDIT_PASSWORD'),
    username=environ.get('REDDIT_USERNAME'),
    user_agent="account wiper by u/opliko95",
)
def main():
    # get redditor instance for the currently logged in user
    user = reddit.user.me()

    # get all comments and posts for the currently logged in user
    for content in chain(user.submissions(limit=None), user.comments(limit=None)):
        # delete the content
        content.delete()

# runs the function if the script is called directly (eg. `python3 wipe-reddit-account.py`)
if __name__ == "__main__":
    main()