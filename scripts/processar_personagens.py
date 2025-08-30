import asyncio
from scripts.gerar_imagem_personagem import gerar_imagem_personagem

async def gerar_imagem_async(client, caminho_cenario, nome_anime, personagem):
    nome = personagem['nome_personagem']
    
    while True:
        try:
            print(f"🔄 {nome}...")  # Inicia processamento
            resultado = await asyncio.to_thread(gerar_imagem_personagem, client, caminho_cenario, nome_anime, personagem)  # Thread separada
            if resultado:
                print(f"✅ {nome}")  # Sucesso
                return resultado  # Retorna dict com caminho e dados
        except Exception as erro:
            print(f"⚠️ {nome}: {erro}")  # Erro, tenta novamente
            await asyncio.sleep(2)

async def processar_personagens_async(client, caminho_cenario, lista_personagens, nome_anime):
    import json
    import os
    
    print(f"🚀 {len(lista_personagens)} personagens em paralelo...")  # Início
    tasks = [gerar_imagem_async(client, caminho_cenario, nome_anime, p) for p in lista_personagens]  # Cria tasks
    resultados = await asyncio.gather(*tasks)  # Executa simultaneamente
    resultados_validos = [r for r in resultados if r]  # Filtra válidos
    
    # Cria mapeamento inteligente arquivo -> dados
    mapeamento = {}
    caminhos_imagens = []
    for resultado in resultados_validos:
        arquivo = os.path.basename(resultado['caminho'])  # Nome do arquivo
        mapeamento[arquivo] = resultado['dados']  # Dados do personagem
        caminhos_imagens.append(resultado['caminho'])
    
    # Salva mapeamento na pasta do anime
    pasta_anime = os.path.join('resultados', nome_anime.replace(' ', '_').lower())
    caminho_mapeamento = os.path.join(pasta_anime, 'mapeamento_personagens.json')
    with open(caminho_mapeamento, 'w', encoding = 'utf-8') as f:
        json.dump(mapeamento, f, ensure_ascii = False, indent = 2)
    print(f"💾 Mapeamento salvo: {caminho_mapeamento}")
    
    print(f"✅ {len(resultados_validos)} concluídos!")  # Resultado
    return caminhos_imagens
