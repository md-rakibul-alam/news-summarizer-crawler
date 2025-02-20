import requests

url = "https://www.prothomalo.com/api/v1/collections/latest?offset=20&limit=10"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    items = data["items"]
    urls = []

    for item in items:
        story = item["story"]

        urls.append({
            "Url": story["url"],
            "PublishedDate": story["content-updated-at"],
            "HeadLine": story["headline"]
        })

    print(urls)

