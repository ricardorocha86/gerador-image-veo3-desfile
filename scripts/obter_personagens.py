from pydantic import BaseModel, Field
import json
import sys
sys.path.append('.')  # Permite importar config_anime
from config_anime import MODELO_OBTER_PERSONAGENS, PROMPT_PERSONAGENS_TEMPLATE, QUANTIDADE_PERSONAGENS

class InfoPersonagem(BaseModel):
    nome_personagem: str = Field(..., description="O nome principal e mais simples do personagem, sem títulos ou sobrenomes desnecessários.")
    cor_personagem: str = Field(..., description="Uma única cor simples associada ao personagem, escrita por extenso em português.")
    acao_tipica: str = Field(..., description="Descrição DETALHADA e MINUCIOSA em inglês de uma ação maluca e dinâmica que o personagem faria em um vídeo de 8 segundos no desfile. Deve incluir movimentos específicos do corpo, gestos característicos, efeitos visuais únicos do personagem, velocidade dos movimentos e qualquer habilidade especial. Seja MUITO específico nos detalhes da ação.")
    pose_inicial: str = Field(..., description="Descrição EXTREMAMENTE DETALHADA e MINUCIOSA em inglês da pose inicial do personagem para o frame inicial do vídeo. Deve incluir: posição exata do corpo, ângulo das pernas e braços, postura das mãos, expressão facial específica, direção do olhar, detalhes completos da roupa característica, acessórios, penteado, e qualquer elemento visual único do personagem. Seja MUITO preciso em cada detalhe visual.")

def obter_personagens(client, nome_anime):
    """
    Obtém lista de personagens principais de um anime.

    Args:
        client: Cliente da API Gemini
        nome_anime (str): O nome do anime.

    Returns:
        list: Lista de personagens em formato JSON.
    """
    prompt = PROMPT_PERSONAGENS_TEMPLATE.format(
        nome_anime=nome_anime,
        quantidade_total=QUANTIDADE_PERSONAGENS
    )

    while True:
        try:
            resposta = client.models.generate_content(
                model=MODELO_OBTER_PERSONAGENS,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": list[InfoPersonagem],
                },
            )
            break
        except Exception as erro:
            print(f"❌ {erro}")
            import time
            time.sleep(5)
 

    lista_personagens = json.loads(resposta.text)
    print(f"✓ {len(lista_personagens)} personagens obtidos para {nome_anime}:")
    for personagem in lista_personagens:
        print(f"  • {personagem['nome_personagem']} - {personagem['cor_personagem']}")
    
    return lista_personagens
