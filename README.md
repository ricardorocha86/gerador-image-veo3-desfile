# 🎬 Gerador de Vídeos Desfile

## 📱 Exemplos de Criações

Veja alguns vídeos criados com este sistema:

- [**Exemplo 1**](https://youtube.com/shorts/S2KbcxDjwjA) - Desfile gerado automaticamente
- [**Exemplo 2**](https://youtube.com/shorts/HMliJhNpnSs) - Personagens em ação na passarela
- [**Exemplo 3**](https://youtube.com/shorts/r0UTz-qA4D4) - Resultado final com trilha sonora

---

Sistema automatizado para criar vídeos de desfile de moda com personagens de anime usando IA generativa.

## 🚀 Tecnologias Principais

### **Google Generative AI (Gemini & Veo)**
- **`google-genai==1.21.1`** - SDK oficial do Google para IA generativa
- **Gemini 2.5 Flash Image Preview** - Geração de imagens dos personagens
- **Veo 3.0 Fast Generate Preview** - Geração de vídeos a partir das imagens
- **API Polling System** - Monitoramento assíncrono do progresso de geração

### **MoviePy** 
- **`moviepy==1.0.3`** - Biblioteca Python para edição de vídeos
- **Concatenação de vídeos** - União de múltiplos clipes
- **Manipulação de áudio** - Adição de trilha sonora
- **Efeitos visuais** - Fade in/out, redimensionamento
- **Conversão de formatos** - Export em MP4 com codec H.264

### **PIL (Pillow)**
- **`Pillow==10.4.0`** - Manipulação avançada de imagens
- **Conversão de formatos** - PNG, JPEG, bytes
- **Redimensionamento inteligente** - Manutenção de aspect ratio
- **Buffer de memória** - Processamento via BytesIO

### **Python AsyncIO**
- **`asyncio==4.0.0`** - Programação assíncrona nativa
- **Processamento paralelo** - Múltiplas imagens simultâneas
- **Threading integration** - `asyncio.to_thread()` para APIs síncronas
- **Task management** - `asyncio.gather()` para coordenação

### **Bibliotecas Built-in**
- **`json`** - Serialização de dados dos personagens
- **`os`** - Manipulação de arquivos e diretórios
- **`re`** - Normalização de nomes de arquivos
- **`time`** - Medição de performance e delays
- **`io`** - Buffer de dados binários

## 🏗️ Arquitetura do Sistema

### **Pipeline de Geração com Confirmações**
```
1. Cálculo de Custos → Confirmação usuário (sim/não)
2. Obter Personagens (Gemini) → Tabela + Confirmação (ok/novo/parar)
3. Criar Cenário (Gemini) → Imagem + Confirmação (ok/novo)
4. Gerar Imagens Async (Gemini) → Galeria + Confirmação (ok/novo/parar)
5. Gerar Vídeos Sequencial (Veo) → Múltiplas MP4
6. Concatenar + Trilha (MoviePy) → Vídeo final 16:9
7. Versão Stories (MoviePy) → 4:5 vertical (576x720)
```

### **Estrutura de Arquivos**
```
├── executar_tudo.py          # Pipeline completo
├── executar_imagens.py       # Apenas geração de imagens
├── executar_videos.py        # Apenas geração de vídeos  
├── executar_edicao.py        # Edição e versões finais
├── config_anime.py           # Configuração central
├── scripts/
│   ├── obter_personagens.py       # API Gemini - Lista
│   ├── criar_cenario.py            # API Gemini - Cenário
│   ├── gerar_imagem_personagem.py  # API Gemini - Imagem
│   ├── processar_personagens.py    # AsyncIO - Batch
│   ├── criar_galeria_html.py       # Visualização web
│   ├── gerar_video_simples.py      # API Veo - Vídeo
│   ├── gerar_multiplos_videos.py   # Batch sequencial
│   ├── concatenar_videos.py        # MoviePy - Union
│   └── gerar_versao_stories.py     # MoviePy - Crop 9:16
└── resultados/
    └── anime_name/
        ├── cenario.png
        ├── personagem_*.png
        ├── video_*.mp4
        ├── mapeamento_personagens.json
        ├── anime_desfile_completo.mp4
        └── anime_stories.mp4
```

### **Sistema de Mapeamento Inteligente**
- **Normalização de nomes** - `re.sub()` para caracteres especiais
- **Mapeamento direto** - `arquivo.png → dados_personagem`
- **Eliminação de matching** - Zero dependência de strings similares
- **Dados consistentes** - JSON com nome, cor, ação típica, pose

### **Robustez e Retry**
- **API error handling** - `while True: try/except` com delays
- **Skip de arquivos existentes** - Evita reprocessamento
- **Cleanup de memória** - `.close()` em todos os recursos
- **Timeout resilience** - Polling com intervalos configuráveis

## ⚡ Performance e Otimização

### **Processamento Assíncrono**
- **Imagens em paralelo** - Até N personagens simultâneos
- **Vídeos sequenciais** - Evita sobrecarga da API Veo
- **Memory management** - Liberação explícita de recursos

### **Caching Inteligente**
- **Arquivos existentes** - Skip automático
- **Mapeamento persistente** - JSON salvo localmente
- **Reaproveitamento** - Cenários e galerias reutilizáveis

## 🎨 Recursos Visuais

### **Formatos Suportados**
- **16:9 Landscape** - Vídeo principal para YouTube/TV
- **4:5 Portrait** - Versão Stories (576x720) para Instagram/TikTok
- **Aspect ratio preservado** - Crop inteligente sem distorções

### **Efeitos Profissionais**
- **Fade in/out** - Transições suaves (0.3s)
- **Contracapa** - 4 segundos de fechamento
- **Trilha sonora** - Sincronização automática
- **Crop inteligente** - Centro mantido na versão 4:5

## 🔧 Instalação

```bash
# Clone o repositório
git clone [repo-url]
cd GeradorDeVideosDesfile

# Instale dependências
pip install -r requirements.txt

# Configure sua API key do Google
# Edite config_anime.py com o nome do anime desejado
```

## 🎯 Uso Rápido

```bash
# Pipeline completo
python executar_tudo.py

# Apenas imagens
python executar_imagens.py

# Apenas vídeos
python executar_videos.py

# Edição final (16:9 + 9:16)
python executar_edicao.py
```

## 📊 Configuração

Edite `config_anime.py`:
```python
NOME_ANIME = 'One Piece'  # Seu anime favorito
```

O sistema suporta qualquer anime/franquia - a IA se adapta automaticamente!

## 🎬 Resultado Final

- **Vídeo 16:9** - Todos personagens em sequência + contracapa + trilha
- **Vídeo 4:5** - Versão Stories (576x720) otimizada para redes sociais
- **Galeria HTML** - Visualização interativa das imagens geradas
- **Dados JSON** - Metadados dos personagens para reutilização
- **Tabela de Personagens** - Preview detalhado antes da geração

## 🎛️ Controles Interativos

### **Sistema de Confirmações**
- **Custos** - Visualize gastos estimados antes de iniciar
- **Cenário** - Aprove ou regenere o cenário de fundo
- **Personagens** - Revise tabela detalhada com nome, cor, ação e pose
- **Imagens** - Confirme qualidade das imagens ou regenere
- **Controle Total** - Pare, continue ou refaça qualquer etapa

### **Códecs Otimizados**
- **H.264 (libx264)** - Máxima compatibilidade de vídeo
- **AAC** - Codec de áudio padrão para MP4
- **Configuração minimalista** - Apenas parâmetros essenciais

---

**Feito com ❤️ e muito minimalismo brasileiro! 🇧🇷**
