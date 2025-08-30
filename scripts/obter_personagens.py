from pydantic import BaseModel, Field
import json

class InfoPersonagem(BaseModel):
    nome_personagem: str = Field(..., description="O nome do personagem do anime.")
    cor_personagem: str = Field(..., description="Uma cor associada ao personagem.")
    acao_tipica: str = Field(..., description="Uma ação típica que o personagem realizaria em um ambiente de desfile de moda.")
    pose_inicial: str = Field(..., description="Texto em inglês descrevendo a roupa, detalhes e a pose inicial do personagem no desfile, caracterizando-o com suas características únicas.")

def obter_personagens(client, nome_anime):
    """
    Obtém lista de personagens principais de um anime.

    Args:
        client: Cliente da API Gemini
        nome_anime (str): O nome do anime.

    Returns:
        list: Lista de personagens em formato JSON.
    """
    estilo = "humano realistico"
    ambiente = "desfile de moda"

    prompt = f"""Dado o anime '{nome_anime}', no estilo '{estilo}', ambientado em um '{ambiente}', liste os personagens principais e para cada um,
        forneça a cor associada, uma ação típica que eles realizariam neste cenário e uma descrição da pose inicial no desfile, incluindo detalhes da roupa e características do personagem.
        Forneça a saída como uma lista JSON de objetos com as chaves 'nome_personagem', 'cor_personagem', 'acao_tipica' e 'pose_inicial'.
        Escolha os 7 mais famosos e queridos do publico. Desses 7, use 4 ou 5 principais da obra e 2 ou 3 personagens clássicos.
        Por exemplo, em One Piece, Luffy, Zoro, Sanji, Brook, Franky seriam personagens principais, euquanto Roger, Garp, Barba Branca seriam clássicos.

        IMPORTANTE: Na descrição da 'pose_inicial', NÃO inclua nenhum texto escrito, palavras, letras ou qualquer elemento textual nas imagens. Apenas descreva poses, roupas e características visuais.

        """

    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": list[InfoPersonagem],
        },
    )
 

    lista_personagens = json.loads(resposta.text)
    print(f"✓ {len(lista_personagens)} personagens obtidos para {nome_anime}:")
    for personagem in lista_personagens:
        print(f"  • {personagem['nome_personagem']} - {personagem['cor_personagem']}")
    
    return lista_personagens
