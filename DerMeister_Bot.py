import discord




bestatigung_itid = 902136682420240385
bestatigungid = 902176553398575155



bestätigungtext = "Willkommen, drück auf den Haken um dich zu verifizieren und die AGBs zu akzeptieren"

bestätigungtextIT = "Willkommen, drück auf den Haken um dich als ITler zu verifizieren und die AGBs zu akzeptieren"




class MyClient(discord.Client):




    #Einloggen in die Konsole rückmeldung
    async def on_ready(self):
        print("Login Successfully.")
        
        bestatigung = client.get_channel(bestatigungid)
        await bestatigung.send(bestätigungtext)

        bestatigungit = client.get_channel(bestatigung_itid)
        await bestatigungit.send(bestätigungtextIT)


    async def on_reaction_add(self, reaction, user):
        friend = discord.utils.get(user.guild.roles, name="Friend")
        if str(reaction.emoji) == "✅":
           await user.add_roles(friend)

        IT = discord.utils.get(user.guild.roles, name="IT")
        if str(reaction.emoji) == "☑️":
           await user.add_roles(IT)






          

    #Wenn Nachricht geschickt wird 
    async def on_message(self, message):
        if message.author == client.user:       #mcacht das der Bott nicht auf sich selber antowrtet
            return




        if message.content == "<help":
            await message.channel.send("""
            
            Ich kann nix ausser:

            <help = Zeigt dir das du doofi 
            <meinung = Ich sage dir was ich von dir halte
                                                     """)
            


        if message.content.startswith("<meinung"):
            await message.channel.send("Schau in deinen privaten Nachrichten ;)")
            await message.author.send("Du willst meine Meinung wissen? \n Also, ich finde dich komisch <3")


        if message.content.startswith("Hallo"):
            await message.channel.send("Hallooo")


        if message.content.startswith("feierabend") or message.content.startswith("Feierabend"):
            await message.add_reaction("✅")




    async def on_typing(self, channel, user, when):             #hört ob jemand schreibt, wenn ja passiert etc
        print(str(user) + " tippt in " + str(channel))  



    async def on_message_delete(self, message):                  #hört ob jemand was gelöscht hat, wenn ja passiert etc
        print("Geloeschte Nachricht == " + str(message.content) + " von " + str(message.author))



    async def on_message_edit(self, before, after):             #hört ob jemand was edited hat, wenn ja passiert etc
        print("Eine Nachricht wurde geaendert von " + before.content + " zu " + after.content)










token = open("C:\\Users\\giuli\\Documents\\token.txt", "r")
client = MyClient()
client.run(token.readline())

