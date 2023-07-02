import requests
def main():
     meme()
def meme():
    url = "https://meme-generator11.p.rapidapi.com/meme"

    headers = {
        "X-RapidAPI-Key": 'YOUR KEY',#replace with your key
        "X-RapidAPI-Host": "meme-generator11.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    

    return response.json()['title'],response.json()['url']
if __name__=="__main__":
     main()