from config_anime import NOME_ANIME
from scripts.concatenar_videos import concatenar_videos
from scripts.gerar_versao_stories import gerar_versao_stories

concatenar_videos(NOME_ANIME)  # Concatena vídeos
gerar_versao_stories(NOME_ANIME)  # Gera versão Stories
