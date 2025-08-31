from google import genai
from config_anime import NOME_ANIME, API_KEY
from scripts.gerar_multiplos_videos import gerar_multiplos_videos
from scripts.calcular_custo import calcular_custo_estimado


client = genai.Client(api_key = API_KEY)

gerar_multiplos_videos(client, NOME_ANIME)
