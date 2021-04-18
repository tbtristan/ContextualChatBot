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
#from google.cloud import

OVERALL_SENTIMENT = 0
DOCUMENT_GLOBAL = ""
DOCUMENT_COUNTER = 0
client = language_v1.LanguageServiceClient()



def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

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

def analyze_sentiment(text):
    # The text to analyze
    # text = u"i can't believe this is happening to me"
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

    updateGlobalSentiment(sentiment.score)
    updateGlobalEmotion(sentiment.score)
    return sentiment.score

def updateGlobalEmotion(sentiment_score):
    global OVERALL_SENTIMENT
    subdivisions = 3
    emotion_val  = int(((OVERALL_SENTIMENT + 1)* 100)/(2*(100/subdivisions)))
    emotion_list = {0 : 'Angry', 1 : 'Upset', 2 : 'Happy'}
    print("Current Emotion: " + emotion_list[emotion_val])


#   Average can be swayed too easily 
def updateGlobalSentiment(sentiment_score):
    global DOCUMENT_COUNTER, OVERALL_SENTIMENT
    DOCUMENT_COUNTER = DOCUMENT_COUNTER + 1
    OVERALL_SENTIMENT = (((DOCUMENT_COUNTER - 1) * OVERALL_SENTIMENT) + sentiment_score)/DOCUMENT_COUNTER
    print("Overall Sentiment: {}".format(OVERALL_SENTIMENT))
    
if __name__ == '__main__':
##    print("Overall Sentiment: " + str(OVERALL_SENTIMENT))
##    text_content = "The circumplex model on the other hand, needs these data points to complete the “circle” that gives the model its name. Rubin & Talarico (2009) had participants rate emotion related stimuli on scales for valence and intensity (or arousal), and attempted to fit the circumplex and vector models on this data. Interestingly, they were unable to find high-intensity neutral words, which gives credit to the vector model over the circumplex model when dealing with textual data."
##
##    text_1 = "i feel alright"
##    text_2 = "i am "
##
##    sent_1 = analyze_sentiment(text_1)
##    print("Sentiment 1: {}\n".format(sent_1))
##    sent_2 = analyze_sentiment(text_2)
##    print("Sentiment 2: {}\n".format(sent_2))

##
##    print("Overall Sentiment: {}".format(OVERALL_SENTIMENT))

    
    
    # sample_analyze_sentiment(text_content)


	# hashing tweets to change appearance? 
    import hashlib

	# take a Tweet contents string as
	# input and sha256 it. bits of 256 will be used to color and modify sprite
	# example : 

    str = "This is an example"
    result = hashlib.sha256(str.encode())
    print('\r',result.hexdigest())

    user_text = input("Enter text to be analyzed: ")
    while (user_text.lower() != ""):
        analyze_sentiment(user_text)
        user_text = input("Enter text to be analyzed: ")  