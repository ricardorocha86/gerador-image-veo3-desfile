import os
from moviepy.editor import VideoFileClip

def gerar_versao_stories(nome_anime):
    pasta_anime = os.path.join('resultados', nome_anime.replace(' ', '_').lower())  # Pasta do anime
    nome_original = f"{nome_anime.replace(' ', '_').lower()}_desfile_completo.mp4"  # Vídeo original
    caminho_original = os.path.join(pasta_anime, nome_original)  # Caminho completo
    
    if not os.path.exists(caminho_original):  # Verifica se existe
        print(f"❌ Vídeo não encontrado: {caminho_original}")
        return
    
    print(f"📱 Convertendo para Stories (9:16)...")  # Status
    video = VideoFileClip(caminho_original)  # Carrega vídeo
    largura_original, altura_original = video.size  # Dimensões originais
    
    # Calcula nova largura para proporção 9:16 mantendo altura
    nova_largura = int(altura_original * 9 / 16)  # Proporção Stories
    
    # Calcula posição central para corte
    x_centro = (largura_original - nova_largura) // 2  # Centro horizontal
    
    print(f"🔄 {largura_original}x{altura_original} → {nova_largura}x{altura_original}")  # Conversão
    
    # Corta o centro do vídeo
    video_stories = video.crop(x1 = x_centro, x2 = x_centro + nova_largura)  # Crop central
    
    # Nome do arquivo Stories
    nome_stories = nome_original.replace('_desfile_completo.mp4', '_stories.mp4')  # Nome Stories
    caminho_stories = os.path.join(pasta_anime, nome_stories)  # Caminho Stories
    
    print(f"💾 Salvando versão Stories...")  # Status
    video_stories.write_videofile(caminho_stories, codec = 'libx264', audio_codec = 'aac')  # Salva
    
    # Limpa memória
    video.close()  # Libera original
    video_stories.close()  # Libera Stories
    
    print(f"✅ Versão Stories salva: {caminho_stories}")  # Sucesso
    return caminho_stories
