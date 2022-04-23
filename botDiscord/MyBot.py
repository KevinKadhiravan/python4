from discord import Client
from Logs import TheLog
import logging

class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.log = TheLog()

    async def on_ready(self):
        print("Ready")
        self.log.Infolog(f"{self.user} has connected to Discord!")
        
    async def on_message(self,message):
        print(message.content)
        if message.author != self.user:
            self.log.SauvMsg(message.author,message.content)
            await message.channel.send(f"{message.author} : {message.content}")
    
        if message.content == 'hello':
            await message.channel.send(f"Hello {message.author}")
            self.log.SauvMsg(message.author,message.content)

client = MyBot()
client.run("OTY0NDQ1NTcyMDQxOTUzMjgx.Ylkv7g.KoknD-YCPahUulcOhi4283I2iRo")