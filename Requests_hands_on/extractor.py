import requests
import json

with open("News.csv", "w") as f:
    for i in range(1, 6):
        url = 'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page=1'
        res = requests.get(url)
        data = json.loads(res.text)

        for news in data:
            author = news["author"]
            summary = news["summary"]
            f.write(f"{author}, {summary}\n")