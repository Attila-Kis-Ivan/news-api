import requests

api_key = "0d02195b5bb64237aee68be37fcf7747"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-14&sortBy=publishedAt&apiKey=0d02195b5bb64237aee68be37fcf7747"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])