import os
import json
from scripts.gerar_video_simples import gerar_video_simples

def gerar_multiplos_videos(client, nome_anime):
    pasta_anime = os.path.join('resultados', nome_anime.replace(' ', '_').lower())  # Converte para pasta
    caminho_mapeamento = os.path.join(pasta_anime, 'mapeamento_personagens.json')  # Mapeamento inteligente
    
    with open(caminho_mapeamento, 'r', encoding = 'utf-8') as f:  # Lê mapeamento
        mapeamento = json.load(f)
    
    imagens = [arq for arq in os.listdir(pasta_anime) if arq.startswith('personagem_') and arq.endswith('.png')]  # Lista PNGs
    
    for i, arquivo_img in enumerate(imagens, 1):  # Loop sequencial
        nome_video = arquivo_img.replace('personagem_', 'video_').replace('.png', '.mp4')  # Nome vídeo
        caminho_video = os.path.join(pasta_anime, nome_video)  # Caminho vídeo
        
        if os.path.exists(caminho_video):  # Vídeo já existe
            nome_personagem = mapeamento[arquivo_img]['nome_personagem']
            print(f"[{i}/{len(imagens)}] {nome_personagem} - já existe ✓")  # Pula
            continue
        
        # Busca direta no mapeamento - SEM MATCHING de string!
        if arquivo_img not in mapeamento:
            print(f"❌ ERRO: Arquivo '{arquivo_img}' não encontrado no mapeamento!")
            continue
            
        dados_personagem = mapeamento[arquivo_img]  # Dados diretos
        nome_personagem = dados_personagem['nome_personagem']
        acao = dados_personagem['acao_tipica']  # Pega ação
        
        prompt = f"Desfile de moda realista com {nome_personagem} fazendo {acao} elegantemente na passarela"  # Monta prompt
        caminho_img = os.path.join(pasta_anime, arquivo_img)  # Caminho imagem
        
        print(f"[{i}/{len(imagens)}] {nome_personagem} - gerando...")  # Progresso
        gerar_video_simples(client, caminho_img, prompt, caminho_video)  # Gera vídeo
