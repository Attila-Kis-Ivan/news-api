import requests
from send_email import send_email

topic = "apple"
api_key = "0d02195b5bb64237aee68be37fcf7747"
url = "https://newsapi.org/v2/everything?q=apple&from=2024-01-20&to=2024-01-20&sortBy=popularity&apiKey=0d02195b5bb64237aee68be37fcf7747&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(len(content["articles"]))

# Access the article title
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["author"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")    
send_email(message=body)
   


