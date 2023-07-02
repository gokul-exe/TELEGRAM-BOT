import requests
import unicodedata

def main():
      translation()
def translation(question):
            url = "https://text-translator2.p.rapidapi.com/translate"

            payload = {
                  "source_language": "en",
                  "target_language": "ta",
                  "text": question
                        }
            headers = {
                        "content-type": "application/x-www-form-urlencoded",
                        "X-RapidAPI-Key": 'YOUR KEY',#replace with your key
                        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
                              }
            response = requests.post(url, data=payload, headers=headers)

            if response.status_code == 200:
                  result= response.json()["data"]
                  result['translatedText']
                  readable_text = unicodedata.normalize("NFKD",result['translatedText']).encode("UTF-8").decode("UTF-8")
                  return readable_text
            else:
                  error="Failed to translate text. Error message:", response.json()["data"]
                  return error
if __name__=="__main__":
    main()