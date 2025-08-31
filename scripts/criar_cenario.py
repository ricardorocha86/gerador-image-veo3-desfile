from PIL import Image
from io import BytesIO
import os
import sys
sys.path.append('.')  # Permite importar config_anime
from config_anime import MODELO_GERADOR_CENARIO, PROMPT_CENARIO_TEMPLATE

def criar_cenario(client, nome_anime):
    """
    Cria imagem do cenário do desfile de moda.

    Args:
        client: Cliente da API Gemini
        nome_anime (str): Nome do anime para criar pasta

    Returns:
        str: Caminho do arquivo do cenário criado
    """
    print("Criando cenário do desfile...")
    
    prompt_cenario = PROMPT_CENARIO_TEMPLATE.format(nome_anime=nome_anime)
    
    while True:
        try:
            resposta = client.models.generate_content(
                model=MODELO_GERADOR_CENARIO,
                contents=prompt_cenario
            )
            break
        except Exception as erro:
            print(f"❌ {erro}")
            import time
            time.sleep(5)

    # Cria pasta dentro de resultados
    os.makedirs('resultados', exist_ok = True)  # Garante pasta resultados
    pasta_anime = os.path.join('resultados', nome_anime.replace(' ', '_').lower())
    os.makedirs(pasta_anime, exist_ok = True)
    
    partes_imagem = [part.inline_data.data for part in resposta.candidates[0].content.parts if part.inline_data]

    if partes_imagem:
        imagem = Image.open(BytesIO(partes_imagem[0]))
        caminho_cenario = os.path.join(pasta_anime, 'cenario.png')
        imagem.save(caminho_cenario)
        imagem.show()
        print(f"✓ Cenário criado: {caminho_cenario}")
        return caminho_cenario
    
    return None
