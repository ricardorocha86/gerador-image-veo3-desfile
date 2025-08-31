from PIL import Image
from io import BytesIO
import time
import os
import sys
sys.path.append('.')  # Permite importar config_anime
from config_anime import MODELO_GERADOR_PERSONAGEM, PROMPT_IMAGEM_PERSONAGEM_TEMPLATE

def gerar_imagem_personagem(client, caminho_cenario, nome_anime, dados_personagem):
    """
    Gera imagem de um personagem no cenário do desfile.

    Args:
        client: Cliente da API Gemini
        caminho_cenario (str): Caminho da imagem do cenário
        nome_anime (str): Nome do anime
        dados_personagem (dict): Dados do personagem

    Returns:
        str: Caminho da imagem gerada ou None se falhar
    """
    nome = dados_personagem['nome_personagem']
    cor = dados_personagem['cor_personagem']
    pose = dados_personagem['pose_inicial']

    prompt = PROMPT_IMAGEM_PERSONAGEM_TEMPLATE.format(
        nome=nome,
        nome_anime=nome_anime,
        cor=cor,
        pose=pose
    )

    imagem_cenario = Image.open(caminho_cenario)

    resposta = client.models.generate_content(
        model=MODELO_GERADOR_PERSONAGEM,
        contents=[imagem_cenario, prompt],
    )

    # Verificações de segurança
    if not resposta or not resposta.candidates:
        print(f"⚠️ {nome}: Resposta vazia da API")
        return None
        
    if not resposta.candidates[0].content or not resposta.candidates[0].content.parts:
        print(f"⚠️ {nome}: Conteúdo vazio na resposta")
        return None

    partes_imagem = [
        part.inline_data.data
        for part in resposta.candidates[0].content.parts
        if hasattr(part, 'inline_data') and part.inline_data
    ]

    if partes_imagem:
        imagem = Image.open(BytesIO(partes_imagem[0]))
        pasta_anime = os.path.join('resultados', nome_anime.replace(' ', '_').lower())
        
        # Gera nome de arquivo único e consistente
        import re
        nome_limpo = re.sub(r'[^\w\s-]', '', nome).strip()  # Remove caracteres especiais
        nome_limpo = re.sub(r'\s+', '_', nome_limpo).lower()  # Substitui espaços por _
        nome_arquivo = f'personagem_{nome_limpo}.png'
        caminho_arquivo = os.path.join(pasta_anime, nome_arquivo)
        
        imagem.save(caminho_arquivo)
        imagem.show()
        return {'caminho': caminho_arquivo, 'dados': dados_personagem}  # Retorna mapeamento
    else:
        print(f"⚠️ {nome}: API retornou texto ao invés de imagem")
    
    return None
