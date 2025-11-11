# Chambeando en Ramoncito Barros Ignacio para Discord. creación: 07/05/2025. Mod 1: 08/05. Mod 2: 09/05. Mod 3: 20/05.
import discord, logging
# Con este módulo harémos que el bot funcione
# pip install discord.py, requests, py-cord, "py-cord[voice]"
# pip freeze > requirements.txt
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
logging.basicConfig(level=logging.INFO)
bot = commands.Bot(command_prefix='Remy.', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print(f'Bot {bot.user.name} ha iniciado sesión.')
@bot.event
async def on_member_join(member):
	await member.send(f"HOLAAAAA {member.mention}")

@bot.command()
async def hola(ctx):
	await ctx.send("¡Hola! ¿Cómo estás?")

@bot.command()
async def adios(ctx):
	await ctx.send("¡Adiós! Que tengas un buen día.")

@bot.command()
async def ayuda(ctx):
	embed = discord.Embed(title="Comandos", description="""
					   ¡Hola! Soy Remy, y vengo a ayudarte a entender mi funcionamiento\n
					   # Comandos disponibles:
					   -# (El prefijo es Remy.comando)
					   **hola** - Saludo. 🤖
					   **saludar @user** - Puedes enviar a Remy para saludar a un usuario. 🔌
					   **adios** - Despedida. 🛜
					   **ayuda** - Lista de comandos. 💻
					   **info** - Información del bot. 🤖
					   **Server** - Invitación al servidor de Discord donde hablamos de Remy, el bot y mucho más. 🔌""", color=0xcc0202)
	embed.set_footer(text="¡Espero que sea de ayuda!")
	await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
	embed = discord.Embed(title="""Información del Bot", description="¡Hola! Soy Ramoncito Ignacio, pero me llaman \"Remy Lucho del Barrio\", y mi misión es hacer de mi colegio un lugar más animado y divertido con la tecnología.
											 ¿Me apoyan?.""", color=0x0145cc)
	embed.set_footer(text="(Mini proyecto hecho por una humilde estudiante)")
	await ctx.send(embed=embed)

@bot.command()
async def saludar(ctx, member:discord.Member):
	author = ctx.author
	if member.mention == bot.mention:
		await ctx.send(f"Veo que me has mencionado. ¡Hola {author.mention}!")
	elif member.mention == author:
		await ctx.send("¿Te estás auto-saludando?")
	else:
		await ctx.send(f"{author.mention} ha saludado a {member.mention}, ¡Dile hola!")
	
@bot.command()
async def server(ctx):
	await ctx.send("¡Hola! Te presento a nuestra humilde comunidad, puedes ser parte de ella con este enlace:\n- https://discord.gg/YshtfYq26s")

@bot.command()
async def grasa(ctx):
	await ctx.send(":v")
	
@bot.event
async def on_command_error(ctx, error):
	logging.error(f'Error en el comando {ctx.command}: {error}')
	await ctx.send('Ha ocurrido un error. Inténtalo de nuevo más tarde.')

bot.run('') # Recordatorio de ocultar esto