import dialogflow
import pyglet
from sentiment import analyze_sentiment, find_emotion_gif
from google.api_core.exceptions import InvalidArgument
#import google.cloud.dialogflowcx_v3

# DIALOGFLOW_PROJECT_ID = 'bitberg-bot'
language_code = 'en-us'
session_id = "something-here"
location_id = "us-central1"
project_id = "bitberg-bot"
agent_id = "ae6e9b73-bbeb-44cd-88f3-60abd02d8cdc"
agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
session_client = dialogflow.SessionClient()
session = session_client.session_path(project_id, session_id)

def display_gif(gif_file):
  ag_file = gif_file
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

def detect_intent(user): #, agent, session_id, language_code
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session_path = f"{agent}/sessions/{session_id}"
    print(f"Session path: {session_path}\n")
    client_options = None
    agent_components = dialogflow.AgentsClient.parse_agent_path(agent)
    location_id = agent_components["location"]
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    session_client = dialogflow.SessionsClient(client_options=client_options)

    input_string = input("Enter your prompt for bitberg")
    while(input_string != 'close'):
      image_float = analyze_sentiment(user, input_string)
      text_input = session.TextInput(text=input_string)
      query_input = session.QueryInput(text=text_input, language_code=language_code)
      request = session.DetectIntentRequest(
           session=session_path, query_input=query_input
			)
      response = session_client.detect_intent(request=request)
			#display image somehow
      #
      #
      ### display_gif(find_emotion_gif(image_float))
      #
      #
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
      print("=" * 20)
      print(f"Query text: {response.query_result.text}")
      response_messages = [
      " ".join(msg.text.text) for msg in response.query_result.response_messages
      ]
      print(f"Response text: {' '.join(response_messages)}\n")
      input_string = input()

''''
def talkbot (user):
	input_string = input("Enter your prompt for bitberg")
	while(input_string != 'close'):
		text_to_be_analyzed = input_string
		image_float = analyze_sentiment(user, text_to_be_analyzed)
		text_input = dialogflow.types.TextInput(text=text_to_be_analyzed,language_code="en-us")
		query_input = dialogflow.types.QueryInput(text=text_input)
		try:
			#display image somehow
      #
      #
      ### display_gif(find_emotion_gif(image_float))
      #
      #
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
		'''