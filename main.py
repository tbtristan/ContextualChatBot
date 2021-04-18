#################
# Project Title – BitBerg Bot

# Description   – Twitter (discord) bot that simulates conversation 
#                 to your tweets		
# Tools & APIS  – Python (Coding)
#                 Cloud Natural Language API 
#                 Dialogflow API

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
import discord
# import requests
# import io
# import os

client = discord.Client()
TOKEN = "ODMzMzI2NTU0NDg1NjIwNzU2.YHwt1Q.SqU4Cm5hwvBwY1N92_R5l7iQDCU"

from user import User
from dialogflow import discord_response
    
if __name__ == '__main__':
	@client.event
	async def on_ready():
		print('We have logged in as {0.user}'.format(client))

	@client.event
	async def mentioned_in(message):
		if(message.author.bot == False):
			#content = message.content
			user = message.author.id
			poten_new_user = User(user)
			temp_tuple = discord_response(user, message)
			await message.channel.send(temp_tuple[1], file=discord.File(temp_tuple[0]))
			poten_new_user.close()
	client.run(TOKEN)

#     test1 = User("nobody knows it")
#     print("TEST")
#     detect_intent(test1)
#     test1.close()
# >>>>>>> origin/master
