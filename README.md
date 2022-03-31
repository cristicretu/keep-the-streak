![github](https://user-images.githubusercontent.com/45521157/161111388-20e0a0b2-fb3e-4ec9-a8e5-2c890d68bf0b.png)
# Keep the Streak
Small GitHub Action that notifies the user when he hasn't committed on a particular day, to keep the streak. (Who wants to lose a commit streak?)

# How to use
Fork this repository, or hit `Use this template`.

Paste your GitHub Profile URL, like [https://github.com/cristicretu](https://github.com/cristicretu). This is used to crawl the page and get the number of commits for today.
> /main.py

The GitHub Action runs every day at 13:30 UTC, change it to whatever time you want
> /.github/workflows/main.yaml

Make an account at [Push](https://push.techulus.com) and get the `API_KEY`. You'll get up to 30 notifications/month with 4 devices connected. 
Log into your account on the Push mobile app.

In the repository page, go under `Settings` -> `Secrets` -> `Actions` -> `New Repository Secret` -> Name: `PUSH_API_KEY` and value the once that you previously copied.
