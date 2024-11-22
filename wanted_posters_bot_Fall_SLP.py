import nextcord
from nextcord.ext import commands
from PIL import Image
from io import BytesIO

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True 
client = commands.Bot(command_prefix="!", intents=intents)

@client.command()
async def wanted(ctx, user: nextcord.User = None):
    if user == None:
        user = ctx.author
    print("Bot is running") # for debugging

    wanted = Image.open("wanted.jpg") # open wanted picture

    data = BytesIO(await user.display_avatar.read())
    profilePicture = Image.open(data) # get discord profile picture

    profilePicture = profilePicture.resize((233, 268)) # picture size
    wanted.paste(profilePicture, (150, 189)) #picture x, y derection

    wanted.save("profile.jpg") # saved the discord profile picture onto the wanted picture

    await ctx.reply(file = nextcord.File ("profile.jpg")) # !wanted output


client.run('token')



