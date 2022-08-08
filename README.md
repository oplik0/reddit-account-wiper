# Reddit Account Wiper
Periodically wipe your reddit account

## What is this doing

This repository contains a single simple python script (`wipe_reddit_account.py`) and a single GitHub Actions workflow (`.github/workflows/wipe_reddit_account.yml`). I recommend you read them yourself before giving this access to your account. They should hopefully be simple and well-commented enough to understand even without any programming experience.

The `pyproject.toml` and `poetry.lock` files are from a tool called [Poetry](https://python-poetry.org/) which is a package manager for Python that I prefer over using `pip` directly. The workflow installs and uses poetry already, but if you want to develop it locally without Poetry, there is currently just a single dependency (`praw`), so you can just install it by running `pip install praw` instead.

## Usage

1. Fork this repository (requires an GitHub Account)

![fork button location](https://user-images.githubusercontent.com/25460763/183402131-46c4955f-9545-4ca5-8c9c-da8f860075a5.png)

2. Create a new Reddit app:
    1. Go to https://www.reddit.com/prefs/apps/
    2. Click the `are you a developer? create an app...` button at the bottom of the page
    3. Create some name (for example `account-wiper`. It can't contain `reddit` though)
    4. Select `script` as the application type
    5. Write some URL in `redirect_uri` - for example `http://localhost` or even something like `http://invalid-uri`. It won't be useful for this application, but Reddit requires that this field contains an URL.
    6. Other fields are optional, so you can just create the app now
    
    ![filled app creation form](https://user-images.githubusercontent.com/25460763/183403287-76139f11-1e2a-4100-ae8f-0e2396e3459b.png)
3. Save two pieces of information from your created app (or just leave the tab open) - client id and secret:

![client id and client secret locations](https://user-images.githubusercontent.com/25460763/183404430-656f88c5-e028-4081-b9d5-a7d7473760da.png)

4. Open your forked repository in another tab and go to Settings, then Security>Secrets>Actions. You'll need to create a total of 4 repository secrets. Repository secrets are saved in encrypted form and can't be retrieved directly - they will even be hidden from actions logs (but if you give them to a malicious script in an action it can still send them somewhere, so beware):
    - `REDDIT_CLIENT_ID` - the ID of the app from earlier
    - `REDDIT_CLIENT_SECRET` - the app secret from earlier
    - `REDDIT_USERNAME` - your username
    - `REDDIT_PASSWORD` - your password; Unfortunately this authentication flow requires it. For hosted applications normal Oauth2 flow would be better, but as this repository is meant to be copied and used for a single account this is the least bad option.

5. Ensure you have workflows enabled in the repository by going to the Actions tab on the top and selecting `I understand my workflows, go ahead and enable them`:

![Actions warning](https://user-images.githubusercontent.com/25460763/183405553-1ce872f0-7790-466a-a115-7e3f4bdcf0dc.png)

6. And it'd done - the workflow will now run at 00:00 UTC on every Monday. You can also trigger it manually by going to Actions, selecting `.github/workflows/wipe_reddit_account.yml` and using the `Run workflow` button:

![Running the workflow manually](https://user-images.githubusercontent.com/25460763/183406938-af2f4c77-9f8b-44bb-bf15-6943e120d1e5.png)

## How to change the schedule

The workflow runs using the `cron` trigger in the GitHub Actions workflow. You can easily modify the current schedule or even add more cron expressions. Just edit this part of the file (you can do this easily in the GitHub web UI):
```yaml
on:
  schedule:
    - cron: "0 0 * * MON"
```

If you aren't familiar with cron's notation (and even if you are), you can use a tool like [Crontab.guru](https://crontab.guru/) to create the expression.
For example, `33 3 * * 0` (weekdays are numbered 0-6, with 0 being sunday. You can also just use short names as above) will run the script at 03:33 every Sunday and result in this configuration:
```yaml
on:
  schedule:
    - cron: "33 3 * * 0"
```
