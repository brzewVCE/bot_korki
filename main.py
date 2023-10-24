import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
token = 'YOUR_BOT_TOKEN_HERE'

@client.event
async def on_member_join(member):
    await member.send("Hej, witam na moich lekcjach! Proszę, podaj Imię i Nazwisko:")
    name = await client.wait_for("message", check=lambda message: message.author == member)
    name = name.content

    await member.edit(nick=name)

    guild = member.guild
    category = discord.utils.get(guild.categories, name=name)
    if not category:
        category = await guild.create_category(name)
        text_channel = await guild.create_text_channel(name, category=category)
        voice_channel = await guild.create_voice_channel(name, category=category)
        everyone_perms = discord.PermissionOverwrite(
            read_messages=False, send_messages=False, connect=False)
        user_perms = discord.PermissionOverwrite(
            read_messages=True, send_messages=True, connect=True)
        admin_perms = discord.PermissionOverwrite(
            read_messages=True, send_messages=True, connect=True)
        await text_channel.set_permissions(guild.default_role, overwrite=everyone_perms)
        await text_channel.set_permissions(member, overwrite=user_perms)
        await voice_channel.set_permissions(guild.default_role, overwrite=everyone_perms)
        await voice_channel.set_permissions(member, overwrite=user_perms)
        for role in guild.roles:
            if role.permissions.administrator:
                await text_channel.set_permissions(role, overwrite=admin_perms)
                await voice_channel.set_permissions(role, overwrite=admin_perms)
    else:
        text_channel = discord.utils.get(
            guild.text_channels, name=name, category=category)
        voice_channel = discord.utils.get(
            guild.voice_channels, name=name, category=category)
        await text_channel.set_permissions(member, read_messages=True, send_messages=True)
        await voice_channel.set_permissions(member, connect=True)

client.run(
    token)
