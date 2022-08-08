# reddit-account-wiper
Periodically wipe your reddit account

## usage TL;DR (proper docs WIP)
1. Create a GitHub account if you don't have it, then fork the repository I linked to (button in the top right)
2. go to [https://www.reddit.com/prefs/apps/](https://www.reddit.com/prefs/apps/)
3. create a new app, give it some name, select `script` for the type, and add something like `http://localhost` to `redirect_uri` field - it's not used here, but reddit requires it to be set.
4. Copy the string of characters under `personal use script` \- it's the ID of the app, and the secret.
5. Go to the settings of your forked repository, select Secrets, then Actions.
6. Create four new repository secrets: `REDDIT_CLIENT_ID` with the ID from before, `REDDIT_CLIENT_SECRET` with the secret value, `REDDIT_USERNAME` with your reddit username and `REDDIT_PASSWORD` with your password (I can't really do anything better than password authentication here, since with the fork model I'd have to share my secret value in the repository to use Oauth2)
7. Go to Actions tab and ensure it's enabled, then it will work in a week.
