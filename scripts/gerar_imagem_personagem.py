from PIL import Image
from io import BytesIO
import time
import os

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
    acao = dados_personagem['acao_tipica']
    pose = dados_personagem['pose_inicial']

    prompt = f"""
    Create a COMPLETELY PHOTOREALISTIC HUMAN VERSION of {nome} from {nome_anime} in a fashion runway setting.

    CRITICAL SIZE AND POSITIONING:
    - Character must be SMALL in the image - only 50% of the total image height
    - Character positioned EXACTLY in the CENTER of the image
    - LARGE EMPTY SPACE above the character's head (25% of image)
    - LARGE EMPTY SPACE below the character's feet (25% of image)
    - Character should look DISTANT, not close-up 

    HUMAN REALISM REQUIREMENTS:
    - MUST be 100% realistic human, NOT animated/cartoon/drawn style
    - Real human skin texture, pores, natural lighting
    - Photographic quality like a real fashion magazine
    - NO anime/cartoon features whatsoever

    CHARACTER DETAILS:
    - Maintain {nome}'s gender and key characteristics
    - {pose}
    - High-fashion outfit inspired by {nome}'s style
    - {cor} color theme in lighting/outfit accents

    TECHNICAL:
    - Professional fashion photography with wide shot
    - Studio lighting, sharp focus on character
    - Photorealistic rendering, magazine quality
    - NO TEXT OR WORDS anywhere in image
    """

    imagem_cenario = Image.open(caminho_cenario)

    resposta = client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents=[prompt, imagem_cenario],
    )

    partes_imagem = [
        part.inline_data.data
        for part in resposta.candidates[0].content.parts
        if part.inline_data
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
    
    return None
