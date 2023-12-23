import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Siam_lilacpoint.jpg/294px-Siam_lilacpoint.jpg"

response = requests.get(url)

content = response.content

with open("image.jpg", 'wb') as file:
    file.write(response.content)

