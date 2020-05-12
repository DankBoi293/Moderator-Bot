from discord.ext.commands import has_permissions
from discord.ext import commands
from datetime import datetime as d
import time
colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}
import discord
bot = commands.Bot(command_prefix='mod ')
@bot.command(oass_context=True)
async def DM(ctx, user: discord.User, *, message=None):
  message = message or 'This message was sent via DM'
  await bot.send_message(user, message)
class Basic(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name='ban',
        description='Ban someone, **MUST INCLUDE REASON**\n **BE A MOD ONLY** \n use `mod ban @user reason` \n-----\n',
       aliases=['bann']
    )
    async def ban(self, ctx, member : discord.Member, reason=None):
        if reason == None:
            await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
        else:
            messageok = f"You have been banned from {ctx.guild.name} for {reason}"
            await member.send(messageok)
            await ctx.send(f"banned {member.mention} from {ctx.guild.name} for {reason}")
            await member.ban(reason=reason)
        return
    @commands.command(
        name='unban',
        description='Ban someone, **MUST INCLUDE REASON**\n **BE A MOD ONLY** \n use `mod ban @user reason` \n-----\n',
       aliases=['unbann']
    )
    async def unban(self, ctx, *, member):
        banned_users = ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
          user=ban_entry.user
          if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned {user.name}#{user.discriminator}")
            return
        return

        
    # Define a new command
    @commands.command(
        name='ping',
        description='how long it takes for someone on the other end to see your message \n **also known as:** ◘`p`\n-----\n',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        start = d.timestamp(d.now())
        # Gets the timestamp when the command was used

        msg = await ctx.send(content='Pinging')
        # Sends a message to the user in the channel the message with the command was received.
        # Notifies the user that pinging has started

        await msg.edit(content=f'Pong!\nOne message round-trip took {(d.timestamp(d.now())-start) * 1000}ms.')
        await ctx.send(content=f"if the 'round-trip' is more than `2000.1ms` you might want to consider closing some apps, maybe try `task manager`(windows only)")
        # Ping completed and round-trip duration show in ms
        # Since it takes a while to send the messages, it will calculate how much time it takes to edit an message.
        # It depends usually on your internet connection speed
        #

        return
    


    @commands.command(
      name='ReportBugs',
      description='if you would like to report bugs [click here](https://discord.gg/GqwQ3rw)',
      aliases=["hises"]
    )
    async def reportbugs_command(self, ctx):
      await ctx.send(content="if you would like to report bugs: \nhttps://discord.gg/GqwQ3rw")
      return
    @commands.command(
      name='kick',
      description='kick people, **only with permissions!**\nuse `mod kick *member*`',
      aliases=['begon',"thot"]
    )
    @has_permissions(kick_members=True)  
    async def kick_command(self, ctx, Member: discord.Member ,*, reason=None):
      try:
        await ctx.kick(Member)
        ctx.send(content="member successfully kicked.")
      except Exception as e:
          ee = "Error: " + e
          await ctx.send_message(content=ee)
      return
      
   # @kick.error
   # async def kick_error(self, error, ctx):
   #   if isinstance(error, MissingPermissions):
   #        await ctx.send("You don't have permission to do that!")#    async kick_command(self, ctx, userName: discord.User):
#      prefix_used = ctx.prefix
#      alias_used = ctx.invoked_with
#      text = msg[len(prefix_used) + len(alias_used):]
#      if discord.User permissions = "admin":
#        try:
#          kick(User)
#        except Exception as e:
#          ee = "Error: " + e
#          await ctx.send_message(content=ee)
    @commands.command(
      name='website',
      description="get the website for this bot.",
      aliases=["web"]
    )
    async def website_command(self, ctx):
      msg = await ctx.send(content="getting link...")
      time.sleep(1)
      await msg.edit(content=">>> link is:\nhttps://moderator-bot-website--codingandmemes.repl.co/\n**This Website Was Made By The Developer Of This Bot**")
      return
    @commands.command(
      name='server',
      description="you can join the moderator bot server!\njust type in:\n`mod server` or click [here](https://discord.gg/Zef8eD7)\n-----\n",
      aliases=["serv"]
    )
    async def server_command(self,ctx):
      msg = await ctx.send(content="getting link...")
      await msg.edit(content=">>> link is:\nhttps://discord.gg/GqwQ3rw\n**This Link Never Expires**")
      return
    
    @commands.command(
        name='version',
        description="tells you the version of this bot\n**otherwise known as:**\n◘`mod ver`\n-----\n",
        aliases=['ver']

    )
    async def version_command(self, ctx):
        msg = await ctx.send(content='getting version')
        for i in (0,5):
          await msg.edit(content='getting version.')
          
          time.sleep(.5)
          await msg.edit(content='getting version..')
          time.sleep(.5)
          await msg.edit(content='getting version...')
          time.sleep(.5)
          await msg.edit(content='getting version')
        time.sleep(1)
        await msg.edit(content='>>> **version:**\n`3.3.0`')
        return

    
    @commands.command(
        name='get',
        description="get the bot for your server with the link provided\n-----\n",
        aliases=['gimme']
    )
    async def get_command(self, ctx):
        msg = await ctx.send(content="getting link...")
        time.sleep(1)
        await msg.edit(content=f'link is:\nhttps://discordapp.com/api/oauth2/authorize?client_id=646858532372873226&permissions=8&scope=bot')

        return
    #@commands.command(
    #  name='',
    #  description='',
    #  aliases=['',''],
    #  usage='<text>'
    #  
    #  )
    #async def _command(self,ctx):

      

    @commands.command(
        name='announce',
        description='an announcement!\nAlso known as\n`◘repeat`\n`◘parrot`\n`◘say`\n-----\n',
        aliases=['repeat', 'parrot','say'],
        usage='<text>'
    )
    async def say_command(self, ctx, bot):
        # The 'usage' only needs to show the parameters
        # As the rest of the format is generated automatically

        # Lets see what the parameters are: -
        # The self is just a regular reference to the class
        # ctx - is the Context related to the command
        # For more reference - https://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#context

        # Next we get the message with the command in it.
        msg = ctx.message.content

        # Extracting the text sent by the user
        # ctx.invoked_with gives the alias used
        # ctx.prefix gives the prefix used while invoking the command
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        # Next, we check if the user actually passed some text
        if text == '':
            # User didn't specify the text

            await ctx.send(content='You need to specify the text!')

            pass
        else:
            # User specified the text.
            
            await ctx.message.delete()
           # embed = discord.Embed(
          #    title="Announcement",
          #    description=text,
          #    color=0xE74C3C
          #  )
          #  embed.set_author(
          #      name=ctx.message.author.name,
          #      icon_url=ctx.message.author.avatar_url
          #  )
#            import turtle
 #           screen = turtle.Screen()
            
  #          screen.addshape("IMG_6587.png")
            #embed.set_thumbnail(url="IMG_6587.png")
             
            msg = await ctx.send(content='Now generating the embed')
            time.sleep(1)
            
            
            
        import random
        color_list = [c for c in colors.values()]
        # Convert the colors into a list
        # To be able to use random.choice on it
        text2 = ">>> **"+text+"**"
        embed = discord.Embed(
            title="Announcement!",
            description=text2,
            color=random.choice(color_list)
        )
        # Also set the thumbnail to be the bot's pfp
        embed.set_thumbnail(url="https://i.ibb.co/jW1Fq8z/944-E2-DA2-6-E34-4089-8652-4-D4-E8-CACC01-E.png")
        
        # Also set the embed author to the command user
        embed.set_author(
            name=ctx.message.author.name,
            icon_url=ctx.message.author.avatar_url
        )
        for i in(0,4):
          await msg.edit(content=f"Now generating the embed.")
          time.sleep(.5)
          await msg.edit(content=f"Now generating the embed..")
          time.sleep(.5)
          await msg.edit(content=f"Now generating the embed...")
          time.sleep(.5)
        
        await msg.edit(
            embed=embed,
            content=None
        )

        return


def setup(bot):
    bot.add_cog(Basic(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
