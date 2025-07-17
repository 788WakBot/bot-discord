import discord
from discord.ext import commands
import asyncio

# Intents obrigatórios
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Para acessar membros e expulsar/aplicar timeout

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot está online como {bot.user}")

# !ping
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# !discord
@bot.command()
async def discord(ctx):
    await ctx.send("🔗 Link do servidor: https://discord.gg/U6dqVtdrWh")

# !twitch
@bot.command()
async def twitch(ctx):
    await ctx.send("📺 Canal da Twitch: https://www.twitch.tv/wak7888")

# !parceria
@bot.command()
async def parceria(ctx):
    await ctx.send("🔗 Link do servidor: https://discord.gg/fQS3BkfTsh")

# !comandos
@bot.command()
async def comandos(ctx):
    comandos_texto = """
📜 **Lista de Comandos Disponíveis:**

**⚙️ Comandos Gerais:**
`!discord` – Mostra o link do servidor Discord
`!twitch` – Mostra o link do canal da Twitch
`!parceria` – Mostra o link do servidor de parceria
`!comandos` – Lista todos os comandos disponíveis

**🛡️ Comandos de Moderação:**
`!expulsar` – Expulsa um usuário (será pedido o @)
`!timeout` – Coloca um usuário em timeout (será pedido o @ e o tempo em minutos)
    """
    await ctx.send(comandos_texto)

# !lock
@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    canal = ctx.channel
    cargo_membro = discord.utils.get(ctx.guild.roles, name="Membro")

    if not cargo_membro:
        await ctx.send("⚠️ Não encontrei o cargo 'Membro' no servidor.")
        return

    overwrite = canal.overwrites_for(cargo_membro)
    overwrite.send_messages = False
    overwrite.create_public_threads = False
    overwrite.create_private_threads = False

    await canal.set_permissions(cargo_membro, overwrite=overwrite)
    await ctx.send(f"🔒 O cargo {cargo_membro.mention} foi bloqueado para enviar mensagens e criar tópicos neste canal.")

# !unlock
@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    canal = ctx.channel
    cargo_membro = discord.utils.get(ctx.guild.roles, name="Membro")

    if not cargo_membro:
        await ctx.send("⚠️ Não encontrei o cargo 'Membro' no servidor.")
        return

    overwrite = canal.overwrites_for(cargo_membro)
    overwrite.send_messages = None  # None reseta a permissão para padrão
    overwrite.create_public_threads = None
    overwrite.create_private_threads = None

    await canal.set_permissions(cargo_membro, overwrite=overwrite)
    await ctx.send(f"🔓 O cargo {cargo_membro.mention} agora pode enviar mensagens e criar tópicos neste canal.")



# Coloca o teu token aqui
bot.run("MTM5NDgxNjU5OTQ4MzA5MzExNA.G9qz5a.Aub3Jy34ZRHch786tc-y3di3kkEwS0CmBrqBdg")
