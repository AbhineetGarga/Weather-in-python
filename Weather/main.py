# import requests
# from gtts import gTTS
# import json
# import os
# from playsound import playsound
#
#
# city = input('Enter city name: ')
#
# url = f'https://api.weatherapi.com/v1/current.json?key=fba0f5a59db5414681e145343241804&q={city}'
#
# r= requests.get(url)
#
# # print(r.text)
# # print(type(r.text))
# weatherdic = json.loads(r.text)
# W =weatherdic["current"]["temp_c"]
# F =weatherdic["current"]["wind_kph"]
#
#
# # Import the required module for text
# # to speech conversion
#
#
# # This module is imported so that we can
# # play the converted audio
#
#
# # The text that you want to convert to audio
# mytext = f'The current TEmperature in {city} is {W}degree celcious And wind in kilometer per hour is {F}'
#
# # Language in which you want to convert
# language = 'en'
#
# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
#
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome.mp3")
#
# # Playing the converted file
# # os.system("start welcome.mp3")
# playsound("welcome.mp3")
#
#
#









import requests
from gtts import gTTS
import json
import os
from playsound import playsound


while True:

    city = input('Enter city name: ')

    url = f'https://api.weatherapi.com/v1/current.json?key=fba0f5a59db5414681e145343241804&q={city}'

    r= requests.get(url)


    if(city) == "nocity":
        break





    weatherdic = json.loads(r.text)
    W =weatherdic["current"]["temp_c"]
    F =weatherdic["current"]["wind_kph"]


    mytext = f'The current TEmperature in {city} is {W}degree celcious And wind in kilometer per hour is {F}'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("welcome.mp3")
    playsound("welcome.mp3")

