# bot.py
import os
import time

import discord

class BotContext:

    def __init__(self, voice_channel):
        self._voice_channel = voice_channel

    def set_voice_channel(self, vc):
        self._voice_channel = vc

    def get_voice_channel(self):
        return self._voice_channel

TOKEN = ""
DISCORD_GUILD = "European Server"
client = discord.Client(intents=discord.Intents.default())
bot_context = BotContext(None)

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == DISCORD_GUILD, client.guilds)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )





@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 364304837028085763:
            vc = await after.channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:/Tools/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe",
                                           source="C:/Project/Discord/roflbot/welcome.mp3"))
            while vc.is_playing():
                time.sleep(.1)
            await vc.disconnect()
            # if bot_context.get_voice_channel() is None:
            #     vc = await after.channel.connect()
            #     bot_context.set_voice_channel(vc)
            # while bot_context.get_voice_channel().is_playing():
            #     time.sleep(.1)
            # if not bot_context.get_voice_channel().is_connected:
            #     vc = await after.channel.connect()
            #     bot_context.set_voice_channel(vc)
            # bot_context.get_voice_channel().play(discord.FFmpegPCMAudio(executable="C:/Tools/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe",
            #                                source="C:/Project/Discord/roflbot/welcome.mp3"))
            # while vc.is_playing():
            #     time.sleep(.1)
            # await vc.disconnect()
            # for ch in member.guild.text_channels:
            #     if ch.id == 296709157376229376:
            #         await ch.send(f'Hi {member.name}, welcome to the club buddy!')
    # elif before.channel is not None and after.channel is None:
    #     if before.channel.id == 364304837028085763:
    #         if bot_context.get_voice_channel() is None:
    #             vc = await before.channel.connect()
    #             bot_context.set_voice_channel(vc)
    #         while bot_context.get_voice_channel().is_playing():
    #             time.sleep(.1)
    #         if not bot_context.get_voice_channel().is_connected:
    #             vc = await before.channel.connect()
    #             bot_context.set_voice_channel(vc)
    #         bot_context.get_voice_channel().play(discord.FFmpegPCMAudio(executable="C:/Tools/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe",
    #                                        source="C:/Project/Discord/roflbot/bye.mp3"))
    #         while vc.is_playing():
    #             time.sleep(.1)
    #         await vc.disconnect()


client.run(TOKEN)
