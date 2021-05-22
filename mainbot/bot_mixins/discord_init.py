from ..__imports__ import *
from ..settings import *
from ..perks import perkdict

class DiscordInit:
    VERSION = version

    def __init__(self, client):
        self.pre = command_prefix
        self.perks = perkdict
        if not hasattr(self, 'client'):
            self.client = client
        self.avatar = self_avatar
        self.name = self_name
        # self.client.remove_command('help')
        self.client.event(self.on_ready)

        self.db = mongo_client['PacchuSlave']
        self.init_db()

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))
        if not hasattr(self,'name'):
            self.name = self.client.user.name
        if not hasattr(self, 'avatar'):
            self.avatar = self.client.user.avatar_url
        statustxt = "Questioning Everything now 🧠" #adding loop changing statuses
        activity = discord.Game(name=statustxt)
        if(self.client):
            print("Connected to Database")
        print(self.db.list_collection_names())
        await self.client.change_presence(status=discord.Status.online, activity=activity)

    def init_db(self):
        self.serverstat = self.db['serverstat']
        self.bruhs = self.db['bruh']
        self.animeSearch = self.db['animeSearch']
        self.charSearch = self.db['charSearch']
        self.animePics = self.db['animePics']
        self.mangaSearch = self.db['mangaSearch']
        self.gptDb = self.db['gptQuery']
        self.PodcastSuggest = self.db['PodSuggest']
        self.VoiceUsage = self.db['VoiceActivity']




class BaseBot(DiscordInit, commands.Cog):

    @commands.command()
    async def invite(self, ctx):
        await ctx.message.add_reaction('♥')
        embed = discord.Embed(title="Click here", url="https://discord.com/api/oauth2/authorize?client_id=709426015759368282&permissions=8&scope=bot",
                              description="Invite link for this bot", color=0xff2429)
        embed.set_thumbnail(url=self.avatar)
        await ctx.reply(embed=embed)

    # add pagination to this
    @commands.command(aliases=['h', 'halp', 'hel'])
    async def help(self, ctx):
        embed = discord.Embed(color=0xae00ff, description=f"Created by Pacchu \n well Leo helped too.. I guess..!!")
        embed.set_author(name=self.name, icon_url=self.avatar)
        embed.set_thumbnail(url=self.avatar)
        embed.add_field(name=f"{self.pre}perk",
                        value="Cool awesome stuff in this", inline=False)
        embed.add_field(name=f"{self.pre}anime/ani",
                        value="Searches for given anime", inline=True)
        embed.add_field(name=f"{self.pre}manga/m",
                        value="Searches for give Manga", inline=True)
        embed.add_field(name=f"{self.pre}anichar/ac",
                        value="Searches for given Anime Charactor ", inline=True)
        embed.add_field(name=f"{self.pre}anipics/ap",
                        value="Searches for Images of given Anime Charactor", inline=True)
        embed.add_field(
            name=f"{self.pre}stats", value="partially implemented **bugs**", inline=False)
        embed.add_field(name=f"{self.pre}pod",
                        value="Podcast playback section", inline=False)
        embed.add_field(name=f"{self.pre}play/p  , {self.pre}lofi/pl",
                        value="Youtube Playback and Lofi music", inline=False)
        embed.add_field(name=f"{self.pre}invite",
                        value="Invite link for this bot", inline=False)
        embed.add_field(name=f"{self.pre}help",
                        value="isnt it obvious :o", inline=False)
        embed.set_footer(
            text=f"{self.name} {self.VERSION}", icon_url=self.avatar)
        try:
            await ctx.reply(embed=embed)
        except AttributeError:
            await ctx.send(embed=embed)

    @commands.command(aliases=['per', 'perks'])
    async def perk(self, ctx):
        embed = discord.Embed(title=self.client.user.name.title(
        ), description=f"{self.name} Perks", color=0xff9500)
        embed.set_author(name=self.client.user.name,
                         icon_url=self.client.user.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name=f"{self.pre}avatar @Pacchu / {self.pre}av @Pacchu",
                        value=f"Something of use atleast", inline=False)
        embed.add_field(name=f"{self.pre}bruh [emote,link,text message]",
                        value=f"Something to be saved? idk why it an option", inline=False)
        embed.add_field(name=f"{self.pre}gpt \"Today is a wonderful..\"",
                        value="gpt neo text completion", inline=True)
        embed.add_field(name=f"{self.pre}q \"Why is chocolate beautiful?\"",
                        value="gpt neo answering", inline=True)
        embed.add_field(name=f"{self.pre}spotify @mention",
                        value="Gets the user's Spotify activity", inline=False)

        embed.add_field(name=f"{self.pre}kill @mention",
                        value=f"Kills the user ... well not really", inline=True)
        embed.add_field(
            name=f"{self.pre}kiss @mention", value=f"kiss?", inline=True)
        embed.add_field(name=f"{self.pre}hug @mention",
                        value=f"Hugs the user?", inline=True)

        embed.set_footer(
            text=f" {self.client.user.name} {version}", icon_url=self.client.user.avatar_url)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['av', 'pic', 'dp'])
    async def avatar(self, ctx, member: discord.Member = None):
        """

        """
        hgp = member
        await ctx.message.add_reaction('🙄')
        if(ctx.message.author == hgp or hgp == None):
            embed = discord.Embed(
                title="OwO", description=f"{ctx.message.author.mention} steals ...wait thats your OWN", colour=discord.Colour(0xa06a6a))
            embed.set_image(url=ctx.message.author.avatar_url)
        else:
            embed = discord.Embed(
                title="Swong..!", description=f"{ctx.message.author.mention} yeets {hgp.mention}'s profile pic 👀'", colour=discord.Colour(0x00ffb7))
            embed.set_image(url=hgp.avatar_url)
        try:
            embed.set_author(name=hgp.name, icon_url=hgp.avatar_url)
        except:
            embed.set_author(name=ctx.message.author.name,
                             icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=f"{self.client.user.name}",
                         icon_url=self.client.user.avatar_url)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(BaseBot(bot))
