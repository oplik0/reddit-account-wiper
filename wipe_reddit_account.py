# built in packages: os.environ is for getting environental variables (secrets) and chain to combine lists of comments and posts
from os import environ
from itertools import chain

# reddit API wrapper, basically makes connecting to reddit really simple and more readable
import praw

# create a reddit API instance using environment variables for authentication
reddit = praw.Reddit(
    client_id=environ.get('REDDIT_CLIENT_ID'),
    client_secret=environ.get('REDDIT_CLIENT_SECRET'),
    password=environ.get('REDDIT_PASSWORD'),
    username=environ.get('REDDIT_USERNAME'),
    user_agent="weekly account wiper by u/opliko95",
)

# a function just as good practice, this is the main logic of the script
def main():
    # get the currently logged in user
    user = reddit.user.me()

    # loop over comments and posts for the currently logged in user
    # chain combines the two lists into one
    for content in chain(user.submissions.new(limit=None), user.comments.new(limit=None)):
        # content is a single post or comment, both have a delete method
        content.delete()

# runs the main function if the script is called directly (eg. `python3 wipe_reddit_account.py`)
# without this the main method wouldn't run
if __name__ == "__main__":
    main()