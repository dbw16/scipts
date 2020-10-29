#!/usr/bin/env python3
from subprocess import Popen, PIPE, run
from bs4 import BeautifulSoup
from requests import get

# Get the current contents of clipboard mac
copyed = run("pbpaste", capture_output=True).stdout.decode("utf-8")

# Do some cheaky scraping thanks google
page = get("https://www.google.ie/search?q=" + copyed.replace(" ", "+") + "&num=1")
soup = BeautifulSoup(page.content, 'html.parser')
test = soup.find_all('a')

for i in test:
    if "spell" in str(i):
        html_result = str(i)

# only change clibboard if their was a suggestion from google
if "html_result" not in locals():
    exit(0)
else:
    result = html_result.split(";q=")[1].split("&")[0].replace("+", " ")

# send this back to clipboard
p1 = Popen(["echo", result], stdout=PIPE)
Popen('pbcopy', stdin=p1.stdout, stdout=PIPE)
