# Design: From Input Data to Output Data
import requests

api_key = "5b9064658c87492b81179c44bef63ee9"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2023-11-23&sortBy=publishedAt&apiKey="
       "5b9064658c87492b81179c44bef63ee9")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content['articles']:
    print(article["title"])
    print(article["description"])
