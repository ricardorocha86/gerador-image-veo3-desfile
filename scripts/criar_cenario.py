from PIL import Image
from io import BytesIO
import os

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
    
    resposta = client.models.generate_content(
        model="gemini-2.5-flash-image-preview",
        contents="The runway scene captures a modern, indoor fashion show setting, devoid of a model, focusing solely on the dynamic environment. A sleek, illuminated glass runway stretches into the distance, flanked on both sides by a seated audience, many of whom are applauding or capturing the event on their phones. The background features expansive digital LED screens showcasing a vibrant, cosmic tableau of swirling blues, oranges, and purples, reminiscent of a distant galaxy or nebula. Overhead, bright spotlights cast a brilliant glow on the walkway, while a shower of colorful confetti descends from the ceiling, adding a festive and energetic ambiance to the entire spectacle."
    )

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
