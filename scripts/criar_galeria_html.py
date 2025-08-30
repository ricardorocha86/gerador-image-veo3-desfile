import os

def criar_galeria_html(caminhos_personagens, caminho_cenario):
    """
    Cria galeria HTML em grid 2x4 com as imagens geradas.

    Args:
        caminhos_personagens (list): Lista com caminhos das imagens dos personagens
        caminho_cenario (str): Caminho da imagem do cenário
    """
    if not caminhos_personagens:
        print("Nenhuma imagem encontrada para criar a galeria")
        return

    # Adiciona o cenário no início da lista
    todas_imagens = [caminho_cenario] + caminhos_personagens
    
    conteudo_html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Galeria de Personagens</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f0f0f0; }
            .container { width: 100%; max-width: none; margin: 0; background: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .grid { display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, 1fr); gap: 20px; height: 80vh; }
            .image-item { border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .image-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease; }
            .image-item:hover img { transform: scale(1.05); }
            .image-label { text-align: center; padding: 10px; background: #f8f9fa; font-size: 14px; font-weight: bold; }
            h1 { text-align: center; margin-bottom: 30px; color: #333; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Galeria de Personagens</h1>
            <div class="grid">
    """
    
    for i, caminho in enumerate(todas_imagens):
        nome_exibicao = os.path.basename(caminho).replace('.png', '').replace('_', ' ').title()
        if i == 0:
            nome_exibicao = "Cenário"
        
        # Usa apenas o nome do arquivo (caminho relativo simples)
        nome_arquivo = os.path.basename(caminho)
        
        conteudo_html += f"""
                <div class="image-item">
                    <img src="{nome_arquivo}" alt="{nome_exibicao}">
                    <div class="image-label">{nome_exibicao}</div>
                </div>
        """
    
    conteudo_html += """
            </div>
        </div>
    </body>
    </html>
    """
    
    # Salva o arquivo HTML na pasta do desenho
    pasta_desenho = os.path.dirname(caminho_cenario)  # Extrai pasta do caminho do cenário
    caminho_html = os.path.join(pasta_desenho, 'galeria_personagens.html')
    
    with open(caminho_html, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_html)
    
    print(f"✓ Galeria criada com {len(todas_imagens)} imagens: {caminho_html}")
