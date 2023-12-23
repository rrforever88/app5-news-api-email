# Design: From Input Data to Output Data
import requests
from send_email import send_email

topic = "tesla"
api_key = "5b9064658c87492b81179c44bef63ee9"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2023-11-23&"
       "sortBy=publishedAt&"
       "apiKey=5b9064658c87492b81179c44bef63ee9&"
       "language=en")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Set empty list
body = "Subject: Today's news \n"

# Add title and description to list
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
