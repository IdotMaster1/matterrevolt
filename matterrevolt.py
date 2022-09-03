from time import sleep
import pyrevolt
import requests
import json
import traceback

bot = pyrevolt.Bot(prefix="!")

def sendMsg(username, gateway, text):
    headers = {'content-type': 'application/json'}
    payload = {"text": text,"username":username ,"gateway":gateway}
    r = requests.post('http://localhost:4242/api/message', data=json.dumps(payload), headers=headers)

def recvMsg():
    while True:
     h = requests.get('http://localhost:4242/api/messages').json()
     return str(h)

sendMsg("Revolt", "gateway1", "Bot is ready!")

@pyrevolt.ReadySimplified()
async def onReady() -> None:
    print("Ready!")

@bot.on(pyrevolt.GatewayEvent.OnMessage)
async def onMessage(message: pyrevolt.Message) -> None:
 print(f"{message.author.username} said: {message.content}")
 sendMsg(message.author.username, "gateway1", message.content)

@bot.commands.Command(name="message")
async def message(message: pyrevolt.Message) -> None:
    await message.Send(recvMsg)

@bot.commands.Command(name="ping")
async def ping(message: pyrevolt.Message) -> None:
    await message.Send(content=f"Pong {message.author.username}!", embed=pyrevolt.Embed.Create(title="Pong!", description=f"{message.author.mention}!", colour="#0000ff"), replies=[pyrevolt.Reply(message.messageID, True)])

bot.Run(token="NN4d5EKY9KK7gVijp2zbn2Om6gmvm3MB7cnP54H5rfXY0zgSj_I2Qhg0PRGTti99")