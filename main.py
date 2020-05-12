from discord.ext import commands
# Import the keep alive file
import keep_alive
import os
import replit
import discord


def get_prefix(client, message):

    prefixes = ['mod ']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['mod ']   # Only allow 'mod' as a prefix when in DMs

    # Allow users to @mention the bot instead of using a prefix when using a command.
    return commands.when_mentioned_or(*prefixes)(client, message)

global bot
bot = commands.Bot(                                         
    # Create a new bot
    command_prefix=['mod '],                              # Set the prefix
    description='Ze Moderator Bot For All Your Moderator Needs.',                  # Set a description for the bot
    owner_id=64384023132635146,                            # Your unique User ID
    case_insensitive=True                                   # Make the commands case insensitive
)

# case_insensitive=True is used as the commands are case sensitive by default

cogs = ['cogs.basic','cogs.embed']

@bot.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    bot.remove_command('help')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("mod help"))
    try:
      pass
      #guild = self.bot.get_guild(constants.Guild.id)
      #me = guild.me
      #bot.edit(nick="⇨ ⇨ m O d E r A t O r  B o T ⇦ ⇦")
      #await message.guild.get_member(self.user.id).edit(nick="⇨ ⇨ m O d E r A t O r  B o T ⇦ ⇦")
      #await me.edit(nick="⇨ ⇨ m O d E r A t O r  B o T ⇦ ⇦")
    except Exception as e:
      print("Error: ")
      print(e)
    for cog in cogs:
        bot.load_extension(cog)
    return
from discord.utils import find


@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello! I am Moderator Bot! I have my own server! Just type in `mod server`')
        await general.send('Please make sure your moderators have their role called "Mod" otherwise the `mod ban @user reason` command will not work')
# Start the server
keep_alive.keep_alive()

# Finally, login the bot
bot.run("########################", bot=True, reconnect=True)
