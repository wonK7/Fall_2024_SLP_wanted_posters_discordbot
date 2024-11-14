import nextcord
from nextcord.ext import commands
from PIL import Image
from io import BytesIO

#Define the WantedPoster class
class WantedPoster:
    def __init__(self, poster):
        self.poster = poster

    def creat_poster(self, profile_picture):
        wanted = Image.open("wanted.jpg") # Load the base wanted poster image
        profile_picture = profile_picture.resize((175, 175)) 
        wanted.paste(profile_picture, (120, 210)) # Poste the profile picture onto the poster
        wanted.save(self.poster) # Save the final poster

    def get_image(self):
        return nextcord.File(self.poster) # Return the poster image as a file for discord 


# Bot setup
intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!")

@client.command()
async def wanted(ctx, user: nextcord.User = None):
    if user is None:
        user = ctx.author

    # Fetch the user's profile picture
    data = BytesIO(await user.display_avatar.read())
    profile_picture = Image.open(data)
    
    # Use the WantedPoster class to create the poster
    poster = WantedPoster("profile.jpg")
    poster.creat_poster(profile_picture)

    # Send the created poster as a reply
    await ctx.reply(file=nextcord.File ("profile.jpg"))

client.run('discord bot token')


