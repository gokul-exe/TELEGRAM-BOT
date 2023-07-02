import requests
def main():
    img_search()

def img_search(query):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

    querystring = {"q":query,"pageNumber":"1","pageSize":"10","autoCorrect":"true"}

    headers = {
        "X-RapidAPI-Key": 'YOUR KEY',#replace with your key
        "X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()['value'][0]['url']

if __name__=="__main__":
     main()