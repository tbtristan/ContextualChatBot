from google.cloud import language_v1

emotion_list = {0 : 'Angry', 1 : 'Upset', 2 : 'Happy'}
client = language_v1.LanguageServiceClient()

def analyze_sentiment(user, text):
    # The text to analyze
    # text = u"i can't believe this is happening to me"
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

    updateGlobalSentiment(user, sentiment.score)
    return sentiment.score

#   Average can be swayed too easily 
def updateGlobalSentiment(user, sentiment_score):
    DOCUMENT_COUNTER  = user.interactions_counter
    OVERALL_SENTIMENT = user.persistent_sentiment

    DOCUMENT_COUNTER = DOCUMENT_COUNTER + 1
    OVERALL_SENTIMENT = (((DOCUMENT_COUNTER - 1) * OVERALL_SENTIMENT) + sentiment_score)/DOCUMENT_COUNTER
    print("Overall Sentiment: {}".format(OVERALL_SENTIMENT))

    user.interactions_counter = DOCUMENT_COUNTER
    user.persistent_sentiment = OVERALL_SENTIMENT