# -*- coding: utf-8 -*-

from line.linepy import *
import json, requests, sys

listApp = [
	"CHROMEOS\t2.1.5\tHelloWorld\t11.2.5", 
	"DESKTOPWIN\t5.9.2\tHelloWorld\t11.2.5", 
	"DESKTOPMAC\t5.9.2\tHelloWorld\t11.2.5", 
	"IOSIPAD\t8.11.0\tHelloWorld\t11.2.5", 
	"WIN10\t5.5.5\tHelloWorld\t11.2.5"
]
try:
	for app in listApp:
		try:
			try:
				with open("authToken.txt", "r") as token:
					authToken = token.read().replace("\n","")
					if not authToken:
						client = LINE()
						with open("authToken.txt","w") as token:
							token.write(client.authToken)
						continue
					client = LINE(authToken, speedThrift=False, appName=app)
				break
			except Exception as error:
				print(error)
				if error == "REVOKE":
					sys.exit("[ INFO ] BOT REVOKE")
				elif "auth" in error:
					continue
				else:
					sys.exit("[ INFO ] BOT ERROR")
		except Exception as error:
			print(error)
except Exception as error:
	print(error)
with open("authToken.txt", "w") as token:
    token.write(str(client.authToken))
channel = Channel(client, client.server.CHANNEL_ID['JUNGEL_PANG'])
admin = ["u0237b0ec326fc36a91743df4a1ad2591"]
channelToken = channel.getChannelResult()
clientMid = client.profile.mid
clientPoll = OEPoll(client)
clientProfile = client.getProfile()
contact = client.getProfile()
backup = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def clientBot(op):
	try:
		if op.type == 0:
			print ("[ 0 ] END OF OPERATION")
			return

		if op.type == 26:
			try:
				print("[ 26 ] RICIEVE MESSAGE")
				msg = op.message
				text = str(msg.text)
				msg_id = msg.id
				receiver = msg.to
				sender = msg._from
				cmd = text.lower()
				if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
					if msg.toType == 0:
						if sender != client.profile.mid:
							to = sender
						else:
							to = receiver
					elif msg.toType == 1:
						to = receiver
					elif msg.toType == 2:
						to = receiver
					if msg.contentType == 0:
						if cmd == "salam":
							if msg.from in admin:
							_session = requests.session()
							image = "https://media1.tenor.com/images/6d8fe5bf4457fe9948edd06c4dcfd15c/tenor.gif?itemid=12328554"
							url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
							headers = {
								"Host": "game.linefriends.com",
								"Content-Type": "application/json",
								"User-Agent": "Mozilla/5.0",
								"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
							}
							jsonData = {
								"cc": channelToken.token,
								"to": to,
								"messages": [
									  {
											"type": "template",
											"altText": "ar sayang kamu",
											"template": {
												"type": "image_carousel",
												"columns": [
													{
														"imageUrl": "https://media1.tenor.com/images/6d8fe5bf4457fe9948edd06c4dcfd15c/tenor.gif?itemid=12328554",
														"action": {
															"type": "uri",
															"uri": "https://line.me/ti/p/~mase-pesek" 
														}
													}
												]
											}
										}
								]
							}
							data = json.dumps(jsonData)
							sendPost = _session.post(url, data=data, headers=headers)
						if cmd == "coursel":
							_session = requests.session()
							image = "https://media1.tenor.com/images/4ebcc01c5c49ae9785815ab7c4db4a99/tenor.gif?itemid=10163322"
							url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
							headers = {
								"Host": "game.linefriends.com",
								"Content-Type": "application/json",
								"User-Agent": "Mozilla/5.0",
								"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
							}
							jsonData = {
								"cc": channelToken.token,
								"to": to,
								"messages": [
									{
										"type": "template",
										"altText": "this is a carousel template",
										"template": {
											"type": "carousel",
											"actions": [],
											"columns": [
												{
													"thumbnailImageUrl": "https://steamusercontent-a.akamaihd.net/ugc/97230215087482034/3694E72D5E5CA1EAB5F4E2746A1C264FED589FCE/",
													"title": "Title",
													"text": "Text",
													"actions": [
														{
															"type": "uri",
															"label": "Action 1",
															"uri": "https://steamusercontent-a.akamaihd.net/ugc/97230215087482034/3694E72D5E5CA1EAB5F4E2746A1C264FED589FCE/"
														}
													]
												},
												{
													"thumbnailImageUrl": "https://steamusercontent-a.akamaihd.net/ugc/97230215087482034/3694E72D5E5CA1EAB5F4E2746A1C264FED589FCE/",
													"title": "Title",
													"text": "Text",
													"actions": [
														{
															"type": "uri",
															"label": "Action 1",
															"uri": "https://steamusercontent-a.akamaihd.net/ugc/97230215087482034/3694E72D5E5CA1EAB5F4E2746A1C264FED589FCE/"
														}
													]
												}
											]
										}
									}
								]
							}
							data = json.dumps(jsonData)
							sendPost = _session.post(url, data=data, headers=headers)
						if cmd == "mode":
							_session = requests.session()
							image = "https://media1.tenor.com/images/4ebcc01c5c49ae9785815ab7c4db4a99/tenor.gif?itemid=10163322"
							url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
							headers = {
								"Host": "game.linefriends.com",
								"Content-Type": "application/json",
								"User-Agent": "Mozilla/5.0",
								"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
							}
							jsonData = {
								"cc": channelToken.token,
								"to": to,
								"messages": [
									{
										"type": "template",
										"altText": "RA",
										"template": {
										"type": "buttons",
											"style": "primary",
											"actions": [
												{
													"type": "uri",
													"label": "tercyduk",
													"uri": "https://line.me/ti/p/~mase-pesek"
												}
											],
											"thumbnailImageUrl": "https://media1.tenor.com/images/4ebcc01c5c49ae9785815ab7c4db4a99/tenor.gif?itemid=10163322",
											"title": "Selingkuh",
											"text": "pergilah jika sudah tak sayang jangan brtahan dalam kemunafikan"
										}
									}
								]
							}
							data = json.dumps(jsonData)
							sendPost = _session.post(url, data=data, headers=headers)
						if cmd == "me.":
							_session = requests.session()
							image = "https://lh3.googleusercontent.com/proxy/-qcXIaVI5RPLI_rZgSi8T-QyHCDuVXRoFQUksJ2tzKKOGt8vGLQ6EW7yZBO9SIpQ0b5GlZgahj8S4lENJRr2PDK7jN-vPImkR628uGfvOlr3HpSjBCWrGfCGiOsj9pT7PjH8OuZ6bZ7_9RB7tTeUcmld8U5z=w256-h256-nc"
							url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
							headers = {
								"Host": "game.linefriends.com",
								"Content-Type": "application/json",
								"User-Agent": "Mozilla/5.0",
								"Referer": "https://game.linefriends.com/cdn/jbp-lcs/"
							}
							jsonData = {
								"cc": channelToken.token,
								#contact = client.getContact(msg._from)
								"to": to,
								"messages": [
                                                              {
                                                                   "type": "flex",
                                                                   "altText": "AR SAYANG KAMU",
                                                                   "contents": {
                                                                       "type": "bubble",
                                                                       "hero": {
                                                                               "type": "image",
                                                                               "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
                                                                               "size": "full",
                                                                               "aspectRatio": "1.51:1",
                                                                               "aspectMode": "cover",
                                                                       },
                                                                       "body": {
                                                                               "type": "box",
                                                                               "layout": "vertical",
                                                                               "contents": [
                                                                                  {
                                                                                    "type": "text",
                                                                                    "text": "Detail Profile",
                                                                                    "size": "xl",
                                                                                    "weight": "bold",
                                                                                    "wrap": True
                                                                                  },
                                                                                  {
                                                                                    "type": "text",
                                                                                    "text": " MID:\n {}\n\n Nama:\n  {}\n\nStatus:\n  {}".format(contact.mid,contact.displayName,contact.statusMessage),
                                                                                    "wrap": True
                                                                                  }
                                                                               ]
                                                                       },
                                                                       "footer": {
                                                                               "type": "box",
                                                                               "layout": "vertical",
                                                                               "spacing": "md",
                                                                               "contents": [
                                                                                  {
                                                                                    "type": "button",
                                                                                    "style": "primary",
                                                                                    "action": {
                                                                                        "type": "uri",
                                                                                        "label": "Profile",
                                                                                        "uri": "line://nv/profile"
                                                                                     }
                                                                                  },
                                                                                  {
                                                                                    "type": "button",
                                                                                    "style": "primary",
                                                                                    "action": {
                                                                                        "type": "uri",
                                                                                        "label": "Creator",
                                                                                        "uri": "https://line.me/ti/p/~mase-pesek"
                                                                                     }
                                                                                  }
                                                                               ]
                                                                       }
                                                                   }
                                                              }
                                                           ]
                                                       }	
							data = json.dumps(jsonData)
							sendPost = _session.post(url, data=data, headers=headers)
			except Exception as error:
				print(error)
		
	except Exception as error:
		print(error)

def run():
	while True:
		ops = clientPoll.singleTrace(count=50)
		if ops != None:
			for op in ops:
				try:
					clientBot(op)
				except Exception as error:
					print(error)
				clientPoll.setRevision(op.revision)

if __name__ == "__main__":
	run()
