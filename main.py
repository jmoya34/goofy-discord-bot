import discord
client = discord.Client()

token = ''
pfp_path = ''

fp = open(pfp_path, 'rb')
pfp = fp.read()

email = ""
password = ""

@client.event
async def on_ready():
    await client.login(token, bot=False)
    await client.user.edit(password=password, avatar=pfp)

client.run(token, bot=False)
