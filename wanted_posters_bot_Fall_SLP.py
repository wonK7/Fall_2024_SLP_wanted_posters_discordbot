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
    
    try:

        if user is None:
            user = ctx.author
        
        elif user.bot:
            # Bot Debugging
            print(f"User: {user}")          # User info
            print(f"User ID: {user.id}")    # User Id
            print(f"Is bot: {user.bot}")    # Bot verification
            print()

            await ctx.reply("📜 Oops! The wanted poster vanished! "
            "Looks like someone’s trying to hide! Is it you? 🕵️")
            return

        else:
            user = await ctx.guild.fetch_member(user.id)
    
        # Debugging
        print(f"User: {user}")          # User info
        print(f"User ID: {user.id}")    # User Id
        print(f"Is bot: {user.bot}")    # Bot verification
        print()

        # Generating a Wanted Poser

        wanted = Image.open("wanted.jpg") # load wanted picture

        data = BytesIO(await user.display_avatar.read())

        profilePicture = Image.open(data) # get discord profile picture

        profilePicture = profilePicture.resize((233, 268)) # picture size
    
        wanted.paste(profilePicture, (150, 189)) #picture x, y derection

        wanted.save("profile.jpg") # saved the discord profile picture onto the wanted picture

        await ctx.reply(file = nextcord.File ("profile.jpg")) # !wanted output

    except nextcord.NotFound:
        print("User not found. Please input a valid user.") 
        await ctx.reply("📜 Oops! The wanted poster vanished! "
        "Looks like someone’s trying to hide! Is it you? 🕵️")

client.run('Bot token')



