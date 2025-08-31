from config_anime import QUANTIDADE_PERSONAGENS, MODELO_GERADOR_VIDEO

def calcular_custo_estimado():
    """
    Calcula e exibe o custo estimado da geração completa.
    """
    print("💰 CALCULADORA DE CUSTO ESTIMADO")
    print("=" * 50)
    
    # Custos por item
    custo_imagem = 0.04  # $0.04 por imagem
    custo_cenario = 0.04  # $0.04 para o cenário
    duracao_video = 8  # 8 segundos por vídeo
    
    # Custos por segundo de vídeo
    custos_video = {
        "veo-3.0-generate-preview": 0.75,
        "veo-3.0-fast-generate-preview": 0.40,
        "veo-2.0-generate-001": 0.35
    }
    
    # Cálculos básicos
    num_personagens = QUANTIDADE_PERSONAGENS
    custo_imagens = num_personagens * custo_imagem  # Imagens dos personagens
    custo_cenario_total = custo_cenario  # 1 cenário
    custo_base = custo_imagens + custo_cenario_total  # Custo sem vídeos
    
    # Exibição
    print(f"🖼️ CUSTO TOTAL DAS IMAGENS:")
    custo_base_brl = custo_base * 6.0
    print(f"   • Cenário: ${custo_cenario_total:.2f}")
    print(f"   • {num_personagens} Personagens: ${custo_imagens:.2f}")
    print(f"   • Total Imagens: ${custo_base:.2f} USD / R$ {custo_base_brl:.2f} BRL")
    print()
    
    print(f"🎬 CUSTO TOTAL DOS VÍDEOS POR MODELO:")
    for modelo, custo_seg in custos_video.items():
        custo_videos = num_personagens * duracao_video * custo_seg
        custo_videos_brl = custo_videos * 6.0
        
        # Destaca o modelo atual
        if modelo == MODELO_GERADOR_VIDEO:
            print(f"   ► {modelo}: ${custo_videos:.2f} USD / R$ {custo_videos_brl:.2f} BRL ⭐ ATUAL")
        else:
            print(f"   • {modelo}: ${custo_videos:.2f} USD / R$ {custo_videos_brl:.2f} BRL")
    
    print()
    print(f"💵 CUSTO TOTAL GERAL (IMAGENS + VÍDEOS):")
    
    for modelo, custo_seg in custos_video.items():
        custo_videos = num_personagens * duracao_video * custo_seg
        custo_total = custo_base + custo_videos
        custo_total_brl = custo_total * 6.0
        
        # Destaca o modelo atual
        if modelo == MODELO_GERADOR_VIDEO:
            print(f"   ► {modelo}: ${custo_total:.2f} USD / R$ {custo_total_brl:.2f} BRL ⭐ ATUAL")
        else:
            print(f"   • {modelo}: ${custo_total:.2f} USD / R$ {custo_total_brl:.2f} BRL")
    
    # Custo do modelo atual para retorno
    custo_atual = custo_base + (num_personagens * duracao_video * custos_video[MODELO_GERADOR_VIDEO])
    custo_atual_brl = custo_atual * 6.0
    
    print("=" * 50)
    
    return custo_atual, custo_atual_brl
