import asyncio
from google import genai
from scripts.obter_personagens import obter_personagens
from scripts.criar_cenario import criar_cenario
from scripts.processar_personagens import processar_personagens_async
from scripts.criar_galeria_html import criar_galeria_html
from scripts.gerar_multiplos_videos import gerar_multiplos_videos
from scripts.concatenar_videos import concatenar_videos

client = genai.Client(api_key = 'AIzaSyAXOCQ7nO0tNb7d5vx-hCAb8epXui1o8Aw')

async def executar_imagens(nome_anime):
    caminho_cenario = criar_cenario(client, nome_anime)  # Cenário
    lista_personagens = obter_personagens(client, nome_anime)  # Personagens
    caminhos_imagens = await processar_personagens_async(client, caminho_cenario, lista_personagens, nome_anime)  # Imagens paralelo
    criar_galeria_html(caminhos_imagens, caminho_cenario)  # Galeria



from config_anime import NOME_ANIME

asyncio.run(executar_imagens(NOME_ANIME))  # Executa pipeline assíncrono
gerar_multiplos_videos(client, NOME_ANIME)  # Vídeos sequencial após async
concatenar_videos(NOME_ANIME)  # Edição final com trilha e contracapa
