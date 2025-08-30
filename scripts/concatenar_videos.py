import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, ImageClip, AudioFileClip

def concatenar_videos(nome_anime):
    pasta_anime = os.path.join('resultados', nome_anime.replace(' ', '_').lower())  # Converte para pasta
    
    videos_mp4 = [arq for arq in os.listdir(pasta_anime) if arq.startswith('video_') and arq.endswith('.mp4')]  # Lista vídeos
    videos_mp4.sort()  # Ordena alfabeticamente
    
    if not videos_mp4:  # Sem vídeos
        print(f"❌ Nenhum vídeo encontrado em {pasta_anime}")
        return
    
    print(f"🎬 Concatenando {len(videos_mp4)} vídeos...")
    
    clips = []  # Lista de clips
    for i, arquivo_video in enumerate(videos_mp4, 1):  # Carrega cada vídeo
        caminho_video = os.path.join(pasta_anime, arquivo_video)  # Caminho completo
        print(f"[{i}/{len(videos_mp4)}] Carregando {arquivo_video}...")  # Progresso
        clip = VideoFileClip(caminho_video)  # Carrega clip
        clips.append(clip)  # Adiciona à lista
    
    videos_concatenados = concatenate_videoclips(clips)  # Concatena vídeos
    
    print("🖼️ Adicionando contracapa...")  # Status
    # Pega dimensões do primeiro vídeo para manter aspect ratio
    primeiro_video = clips[0]
    largura, altura = primeiro_video.size
    
    contracapa = ImageClip('recursos/contracapa.png', duration = 4)  # Contracapa por 4s
    contracapa = contracapa.resize((largura, altura))  # Força mesmo tamanho dos vídeos
    contracapa = contracapa.fadein(0.3).fadeout(0.3)  # Fade in/out rápido
    
    video_completo = concatenate_videoclips([videos_concatenados, contracapa])  # Adiciona contracapa
    
    print("🎵 Adicionando trilha sonora...")  # Status
    trilha = AudioFileClip('recursos/trilhasonora.mp3')  # Carrega trilha
    duracao_final = min(video_completo.duration, trilha.duration)  # Usa menor duração
    
    video_final = video_completo.subclip(0, duracao_final).set_audio(trilha.subclip(0, duracao_final))  # Aplica trilha
    
    nome_arquivo_final = f"{nome_anime.replace(' ', '_').lower()}_desfile_completo.mp4"  # Nome final
    caminho_final = os.path.join(pasta_anime, nome_arquivo_final)  # Caminho final
    
    print(f"💾 Salvando vídeo final...")  # Status
    video_final.write_videofile(caminho_final, codec = 'libx264', audio_codec = 'aac')  # Salva
    
    # Limpa memória
    for clip in clips:  # Para cada clip
        clip.close()  # Libera memória
    videos_concatenados.close()  # Libera vídeos
    contracapa.close()  # Libera contracapa
    trilha.close()  # Libera trilha
    video_final.close()  # Libera vídeo final
    
    print(f"✅ Vídeo final salvo: {caminho_final}")  # Sucesso
    return caminho_final
