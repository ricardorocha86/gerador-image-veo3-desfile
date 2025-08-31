import os
from moviepy.editor import VideoFileClip

def gerar_versao_stories(nome_anime):
    pasta_anime = os.path.join('resultados', nome_anime.replace(' ', '_').lower())  # Pasta do anime
    nome_original = f"{nome_anime.replace(' ', '_').lower()}_desfile_completo.mp4"  # Vídeo original
    caminho_original = os.path.join(pasta_anime, nome_original)  # Caminho completo
    
    if not os.path.exists(caminho_original):  # Verifica se existe
        print(f"❌ Vídeo não encontrado: {caminho_original}")
        return
    
    print(f"📱 Convertendo para Stories (4:5)...")  # Status
    video = VideoFileClip(caminho_original)  # Carrega vídeo
    
    # Verifica se vídeo carregou corretamente
    if video.duration == 0:
        print(f"❌ Vídeo original parece corrompido: {caminho_original}")
        video.close()
        return
    
    largura_original, altura_original = video.size  # Dimensões originais
    
    # Calcula nova largura para proporção 4:5 mantendo altura original
    nova_largura = int(altura_original * 4 / 5)  # Proporção 4:5
    
    # Calcula posição central para corte
    x_centro = (largura_original - nova_largura) // 2  # Centro horizontal
    
    print(f"🔄 {largura_original}x{altura_original} → {nova_largura}x{altura_original}")  # Conversão
    print(f"📊 Duração original: {video.duration:.1f}s")  # Debug duração
    
    # Crop central mantendo altura original
    video_stories = video.crop(x1 = x_centro, x2 = x_centro + nova_largura)  # Crop central
    
    # Redimensiona apenas se necessário para altura 720
    if altura_original != 720:
        fator_escala = 720 / altura_original  # Fator de escala
        video_stories = video_stories.resize(fator_escala)  # Escala proporcional
    
    # Mantém FPS original
    video_stories = video_stories.set_fps(video.fps)  # Mantém FPS original
    
    # Nome do arquivo Stories
    nome_stories = nome_original.replace('_desfile_completo.mp4', '_stories.mp4')  # Nome Stories
    caminho_stories = os.path.join(pasta_anime, nome_stories)  # Caminho Stories
    
    print(f"💾 Salvando versão Stories...")  # Status
    video_stories.write_videofile(caminho_stories, 
                                  codec = 'libx264', 
                                  audio_codec = 'aac')  # Salva Stories
    
    # Limpa memória
    video.close()  # Libera original
    video_stories.close()  # Libera Stories
    
    print(f"✅ Versão Stories salva: {caminho_stories}")  # Sucesso
    return caminho_stories
