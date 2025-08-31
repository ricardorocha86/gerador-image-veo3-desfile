import asyncio
from google import genai
from scripts.obter_personagens import obter_personagens
from scripts.criar_cenario import criar_cenario
from scripts.processar_personagens import processar_personagens_async
from scripts.criar_galeria_html import criar_galeria_html
from scripts.gerar_multiplos_videos import gerar_multiplos_videos
from scripts.concatenar_videos import concatenar_videos
from scripts.gerar_versao_stories import gerar_versao_stories
from scripts.calcular_custo import calcular_custo_estimado
from config_anime import NOME_ANIME, API_KEY

# Calcula e exibe custo estimado
calcular_custo_estimado()

# Pede confirmação do usuário
confirmacao = input("\nDeseja prosseguir com a execução? (sim/não): ").strip().lower()
if confirmacao not in ['sim', 's', 'yes', 'y']:
    print("❌ Execução cancelada pelo usuário.")
    exit()

print("✅ Iniciando execução...")
client = genai.Client(api_key = API_KEY)

async def executar_imagens(nome_anime):
    # Loop para gerar cenário até aprovação
    while True:
        caminho_cenario = criar_cenario(client, nome_anime)  # Cenário
        
        # Pede confirmação do cenário
        aprovacao = input("\nCenário está OK? (ok/novo): ").strip().lower()
        if aprovacao in ['ok', 'o', 'sim', 's']:
            print("✅ Cenário aprovado, prosseguindo...")
            break
        else:
            print("🔄 Gerando novo cenário...")
    
    lista_personagens = obter_personagens(client, nome_anime)  # Personagens
    
    # Exibe tabela dos personagens gerados
    print("\n" + "="*100)
    print("PERSONAGENS GERADOS:")
    print("="*100)
    print(f"{'Nome':<20} {'Cor':<15} {'Ação Típica':<30} {'Pose Inicial':<30}")
    print("-"*100)
    
    for personagem in lista_personagens:
        nome = personagem['nome_personagem'][:20]
        cor = personagem['cor_personagem'][:15]
        acao = personagem['acao_tipica'][:50] + "..." if len(personagem['acao_tipica']) > 50 else personagem['acao_tipica']
        pose = personagem['pose_inicial'][:50] + "..." if len(personagem['pose_inicial']) > 50 else personagem['pose_inicial']
        print(f"{nome:<20} {cor:<15} {acao:<30} {pose:<30}")
    
    print("="*100)
    
    # Pede confirmação dos personagens
    aprovacao_personagens = input("\nPersonagens estão OK? (ok/novo/parar): ").strip().lower()
    if aprovacao_personagens in ['parar', 'p', 'stop', 'sair']:
        print("❌ Execução interrompida pelo usuário.")
        return
    elif aprovacao_personagens not in ['ok', 'o', 'sim', 's']:
        print("🔄 Para gerar novos personagens, execute novamente o script.")
        return
    
    print("✅ Personagens aprovados, gerando imagens...")
    
    # Loop para gerar imagens até aprovação
    while True:
        caminhos_imagens = await processar_personagens_async(client, caminho_cenario, lista_personagens, nome_anime)  # Imagens paralelo
        criar_galeria_html(caminhos_imagens, caminho_cenario)  # Galeria
        
        # Pede confirmação das imagens com opções
        aprovacao_imagens = input("\nImagens dos personagens estão OK? (ok/novo/parar): ").strip().lower()
        if aprovacao_imagens in ['ok', 'o', 'sim', 's']:
            print("✅ Imagens aprovadas, iniciando geração de vídeos...")
            break
        elif aprovacao_imagens in ['parar', 'p', 'stop', 'sair']:
            print("❌ Execução interrompida pelo usuário.")
            return
        else:
            print("🔄 Gerando novas imagens dos personagens...")


asyncio.run(executar_imagens(NOME_ANIME))  # Executa pipeline assíncrono
gerar_multiplos_videos(client, NOME_ANIME)  # Vídeos sequencial após async
concatenar_videos(NOME_ANIME)  # Edição final com trilha e contracapa
gerar_versao_stories(NOME_ANIME)  # Gera versão Stories
