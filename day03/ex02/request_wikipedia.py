import requests
import dewiki
import json
import sys

def main(query: str):
    session = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"

    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
    params = {
        "action": "parse",
        "page": query,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }

    result = session.get(url=url, params=params, headers=headers)
    if (result.status_code == 403):
        return print("Could not connect to Wikipedia API. Response status code: 403")
    elif (result.status_code != 200):
        return print(f"An error occurred while fetching the result. Response status code: {result.status_code}")

    try:
        data = json.loads(result.text)
    except:
        return print("Could not parse wikipedia's result")
    
    try:
        content = dewiki.from_string(data["parse"]["wikitext"]["*"])
    except:
        return print("Incorrectly formated response")
    
    with open(f"{query}.wiki", "w") as f:
        f.write(content)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print(f"Correct usage: python3 {sys.argv[0]} <query>")
        exit()
    
    main(sys.argv[1])
