import dialogflow
import pyglet
from sentiment import analyze_sentiment
from google.api_core.exceptions import InvalidArgument

DIALOGFLOW_PROJECT_ID = 'bitberg-bot'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
SESSION_ID = 'current-user-id'
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

def __display_gif(emotion):
	ag_file = "dino_{}.gif".format(emotion)
	animation = pyglet.resource.animation(ag_file)
	sprite = pyglet.sprite.Sprite(animation)

	# create a window and set it to the image size
	win = pyglet.window.Window(width=sprite.width, height=sprite.height)

	# set window background color = r, g, b, alpha
	# each value goes from 0.0 to 1.0
	green = 0, 1, 0, 1
	pyglet.gl.glClearColor(*green)

	@win.event
	def on_draw():
			win.clear()
			sprite.draw()

	pyglet.app.run()

def talkbot (user):
	input_string = input("Enter your prompt for bitberg")
	while(input_string != 'close'):
		text_to_be_analyzed = input_string
		image_float = analyze_sentiment(user, text_to_be_analyzed)
		text_input = dialogflow.types.TextInput(text=text_to_be_analyzed,language_code=DIALOGFLOW_LANGUAGE_CODE)
		query_input = dialogflow.types.QueryInput(text=text_input)
		try:
			#display image somehow
			if  -1.0 < image_float < -0.5:
				__display_gif('angry')
				#display angry
			elif image_float < 0.0:
				__display_gif('sad')
				#display sad
			elif image_float < 0.5:
				__display_gif('bored')
				#display bored
			else:
				__display_gif('happy')
				#display happy
			response = session_client.detect_intent(session=session, query_input=query_input)
		except InvalidArgument:
			raise
		print("Query text:", response.query_result.query_text)
		print("Detected intent:", response.query_result.intent.display_name)
		print("Detected intent confidence:", response.query_result.intent_detection_confidence)
		print("Fulfillment text:", response.query_result.fulfillment_text)
		input_string = input()