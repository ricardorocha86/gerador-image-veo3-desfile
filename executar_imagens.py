import asyncio
from google import genai
from config_anime import NOME_ANIME
from scripts.obter_personagens import obter_personagens
from scripts.criar_cenario import criar_cenario
from scripts.processar_personagens import processar_personagens_async
from scripts.criar_galeria_html import criar_galeria_html

client = genai.Client(api_key = 'AIzaSyAXOCQ7nO0tNb7d5vx-hCAb8epXui1o8Aw')

async def executar_imagens(nome_anime):
    caminho_cenario = criar_cenario(client, nome_anime)  # Cenário
    lista_personagens = obter_personagens(client, nome_anime)  # Personagens
    caminhos_imagens = await processar_personagens_async(client, caminho_cenario, lista_personagens, nome_anime)  # Imagens paralelo
    criar_galeria_html(caminhos_imagens, caminho_cenario)  # Galeria

asyncio.run(executar_imagens(NOME_ANIME))
