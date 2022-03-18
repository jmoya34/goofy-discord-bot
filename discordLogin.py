import discord, os, glob, random

def fileLocation(fileName): #returns a readFile
    file = os.getcwd() + "/" + fileName
    return file


email = str(input("Input account email "))
password = str(input("Input account password "))
client = discord.Client()

token_file = open(fileLocation("token/token.txt"), 'rb')
token = str(token_file.read())

pfp_list = []
pfp_file = glob.glob("profilePictures/*.jpg")
for pic in pfp_file:
    pfp_list.append(pic)


@client.event
async def on_ready():
    await client.login(token, bot=False)
    await client.user.edit(password=password, avatar=random.choice(pfp_list))


client.run(token, bot=False)
print("pfp has changed")
