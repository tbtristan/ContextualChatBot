#################
# Project Title – BitBerg Bot

# Description   – Twitter bot that simulates conversation 
#                 to your tweets		
# Tools & APIS  – Python (Coding)
#                 Cloud Natural Language API 
#                 Dialogflow API
#                 Text-to-Speech API
#                 echoAR

# Members       – Tristan Bradfield
#                 Aidan Gray
#                 Kameron Melvin
#################

#modules : sentiment analysis on users tweets
#					 gifs and sprites
#					 chat responses based on sentiment
#					 general comments based on sentiment over past N tweets
#					 make it work in AR, have it run around doin gay little memes

# from google.cloud import dialogflow
# from google.cloud import language
# from google.cloud import language_v1
# from google.cloud import

from user import User
from dialogflow import detect_intent
    
if __name__ == '__main__':
    test1 = User("nobody knows it")
    detect_intent(test1)
    test1.close()
