import time
import io
from PIL import Image
from google.genai import types
import sys
sys.path.append('.')  # Permite importar config_anime
from config_anime import MODELO_GERADOR_VIDEO

def gerar_video_simples(client, caminho_imagem, prompt, nome_arquivo = "video_teste.mp4"):
    tempo_inicio = time.time()  # Marca início
    
    imagem = Image.open(caminho_imagem)  # Carrega imagem
    image_bytes_io = io.BytesIO()  # Buffer
    imagem.save(image_bytes_io, format = imagem.format)  # Converte
    image_bytes = image_bytes_io.getvalue()  # Bytes
    
    while True:  # Loop de retry
        try:
            print(f"🎬 Gerando vídeo...")  # Início
            
            operacao = client.models.generate_videos(  # Solicita vídeo
                model = MODELO_GERADOR_VIDEO,
                prompt = prompt,
                image = types.Image(image_bytes = image_bytes, mime_type = imagem.format),
                config = types.GenerateVideosConfig(aspect_ratio = "16:9"),
            )
            
            while not operacao.done:  # Aguarda
                print("⏳ Processando...")  # Status
                time.sleep(3)  # Espera 3s
                operacao = client.operations.get(operacao)  # Atualiza
            
            video = operacao.response.generated_videos[0]  # Pega vídeo
            client.files.download(file = video.video)  # Baixa
            video.video.save(nome_arquivo)  # Salva
            
            tempo_total = time.time() - tempo_inicio  # Calcula tempo
            print(f"✅ Vídeo salvo em {tempo_total:.1f}s: {nome_arquivo}")  # Resultado
            return nome_arquivo
            
        except Exception as erro:  # Erro na API
            print(f"❌ Erro: {erro}")  # Mostra erro
            print("🔄 Tentando novamente em 10s...")  # Retry
            time.sleep(10)  # Espera antes de tentar
