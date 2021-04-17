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

#from google.cloud import dialogflow
#from google.cloud import language
from google.cloud import language_v1
#from google.cloud import texttospeech
import os

GOOGLE_APPLICATION_CREDENTIALS = os.path.abspath("bitberg-bot-c4fd2dc89602.json")

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))




if __name__ == '__main__':
  text_content = "The circumplex model on the other hand, needs these data points to complete the “circle” that gives the model its name. Rubin & Talarico (2009) had participants rate emotion related stimuli on scales for valence and intensity (or arousal), and attempted to fit the circumplex and vector models on this data. Interestingly, they were unable to find high-intensity neutral words, which gives credit to the vector model over the circumplex model when dealing with textual data."

  sample_analyze_sentiment(text_content)


	# hashing tweets to change appearance? 
  import hashlib

	# take a Tweet contents string as
	# input and sha256 it. bits of 256 will be used to color and modify sprite
	# example : 

  str = "This is an example"
  result = hashlib.sha256(str.encode())
  print('\r',result.hexdigest())