from bs4 import BeautifulSoup
import requests
import datetime
import sys, os, errno

# Config
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

# Change this with your url
url = "https://github.com/cristicretu"

# Get the page
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")

# Get today's date
today = datetime.date.today()
# Format the date as a string
stringday = today.strftime("%Y-%m-%d")

# Get today's contributions
result = soup.find("rect", {"data-date": stringday})["data-count"]

if result == "0":
  sys.exit(os.EX_OK)
else:
  sys.exit(errno.ECANCELED)

