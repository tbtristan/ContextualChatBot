#################
# Project Title – BitBerg Bot

# Description   – Twitter bot that simulates conversation 
#                 to your tweets

# Tools & APIS  – Python (Coding)
#                 Cloud Natural Language API 
#                 Dialogflow API
#                 Text-to-Speech API
#                 echoAR
#
# Members       – Tristan Bradfield
#                 Aidan Gray
#                 Kameron Melvin
#################

#modules : sentiment analysis on users tweets
#					 gifs and sprites
#					 chat responses based on sentiment
#					 general comments based on sentiment over past N tweets
#					 make it work in AR, have it run around doin gay little memes

#from google.cloud import dialogflow
from google.cloud import language
#from google.cloud import texttospeech

def language_analysis(text):
  client  = language.Client()

  document  = client.document_from_text(text)

  sent_analysis = document.analyze_sentiment()
  print(dir(sent_analysis))

  sentiment = sent_analysis.sentiment
  print(sentiment)

  ent_analysis  = document.analyze_entities()
  entities      = ent_analysis.entities
  for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience)


if __name__ == '__main__':
  text = "The circumplex model on the other hand, needs these data points to complete the “circle” that gives the model its name. Rubin & Talarico (2009) had participants rate emotion related stimuli on scales for valence and intensity (or arousal), and attempted to fit the circumplex and vector models on this data. Interestingly, they were unable to find high-intensity neutral words, which gives credit to the vector model over the circumplex model when dealing with textual data."

  language_analysis(text)