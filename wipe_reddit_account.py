"""A simple script for deleting all comments and posts from a user's account."""

# imports some built in packages:
# os.environ is used to access environmental variables, where we will pass our secrets
from os import environ
# the chain function is used to combine two lists (iterators) into one
from itertools import chain

# reddit API wrapper, basically makes connecting to reddit really simple and more readable
# without this one would need to write a lot of code to even log in
import praw

# create a Reddit instance using environment variables for authentication (set in workflow file)
# this will be used to interact with Reddit API
reddit = praw.Reddit(
    # this is the ID of the app we created in the Reddit developer portal
    client_id=environ.get('REDDIT_CLIENT_ID'),
    # this is the secret of the app we created in the Reddit developer portal
    client_secret=environ.get('REDDIT_CLIENT_SECRET'),
    # this is the username of the account we want to delete all content from
    # should be yours otherwise it probably won't work :)
    username=environ.get('REDDIT_USERNAME'),
    # this is the password of the account we want to delete all content from
    # unfortunate it is necessary for this authentication method
    password=environ.get('REDDIT_PASSWORD'),
    user_agent="weekly account wiper by u/opliko95",
)

# a function just as good practice - so this can be imported and called from other scripts
def main():
    """Delete all comments and posts from a user's account."""
    # this just puts the current user into a variable
    user = reddit.user.me()

    # just output this string to have *some* feedback in logs
    print("Deleting all comments and posts...")

    # variable to keep track of how many comments and posts we deleted
    count = 0

    # chain combines the two lists into one, where comments will come after all posts are gone
    # limit=None is used to iterate over all comments and posts instead of just the first 100
    content_list = chain(user.submissions.new(limit=None), user.comments.new(limit=None))

    # loop over comments and posts for the currently logged in user
    # enumerate returns list of two element tuples that look like this: (index, element)
    # this is used to keep track of the number of items deleted
    # the 1 at the end means we start counting from 1 instead of 0
    # count is assigned to the index of the current element (number of items deleted)
    # content is assigned to the current element (the comment or post)
    for count, content in enumerate(content_list, 1):
        # content is a single post or comment, both have a delete method so we don't care which
        content.delete()

        # every 100 comments/posts, print how many have been deleted as a crude progress indicator
        if count % 100 == 0:
            print(f"Deleted {count} comments and posts")

    # just some feedback at the end and the total count of deleted content
    print(f"Account wiped! Deleted {count} comments and posts.")

# runs the main function if the script is called directly (eg. `python3 wipe_reddit_account.py`)
# without this the main method wouldn't run
if __name__ == "__main__":
    main()
