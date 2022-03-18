import discord
client = discord.Client()

token = str("MjMzNDEyNTI5MjgyNDgyMTc3.YjRKdQ.4XdY8GJnKBPTRj8mbDVMxfrWmK0")
pfp_path = "C:/Users/trolo/Desktop/DiscordPfpAutomation/venv/Discord-pfp-automation/profilePictures/3c1e0c2710390529f8f4d951f01e4b8f.jpg"

fp = open(pfp_path, 'rb')
pfp = fp.read()

email = "kkazap4@gmail.com"
password = str("1Atrolsaysha")

@client.event
async def on_ready():
    await client.login(token, bot=False)
    await client.user.edit(password=password, avatar=pfp)

client.run(token, bot=False)
