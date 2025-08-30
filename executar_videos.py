from google import genai
from config_anime import NOME_ANIME
from scripts.gerar_multiplos_videos import gerar_multiplos_videos

client = genai.Client(api_key = 'AIzaSyAXOCQ7nO0tNb7d5vx-hCAb8epXui1o8Aw')

gerar_multiplos_videos(client, NOME_ANIME)
