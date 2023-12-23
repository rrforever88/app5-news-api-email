# Design: From Input Data to Output Data
import requests
from send_email import send_email

api_key = "5b9064658c87492b81179c44bef63ee9"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2023-11-23&sortBy=publishedAt&apiKey="
       "5b9064658c87492b81179c44bef63ee9")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Set empty list
body = "Subject: Tesla News Of The Day \n"

# Add title and description to list
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(body)
