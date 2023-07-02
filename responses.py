from translationapi import translation
from weatherapi import weather_api
from randmemeapi import meme
from imgsearch import img_search



def resp_collec(user_message, context, update):
    if user_message.startswith('translation'):
        question = user_message[12:]
        return translation(question)
        
    elif user_message == ("weather"):      
      return weather_api()   
    
    
    elif user_message == ("meme"):
        text,url=meme()
        resp={'CAPTION':text,'image':url}
        return resp
    
    elif user_message.startswith('imagesearch'):
        query=user_message[10:]
        
        return img_search(query)
    
       
    else: pass
if __name__=="__main__":
     pass