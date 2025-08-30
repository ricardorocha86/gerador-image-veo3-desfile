# 🎬 Gerador de Vídeos Desfile

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

### **Pipeline de Geração**
```
1. Obter Personagens (Gemini) → Lista JSON
2. Criar Cenário (Gemini) → Imagem PNG
3. Gerar Imagens Async (Gemini) → Múltiplas PNG
4. Gerar Vídeos Sequencial (Veo) → Múltiplas MP4
5. Concatenar + Trilha (MoviePy) → Vídeo final
6. Versão Stories (MoviePy) → 9:16 vertical
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
- **9:16 Portrait** - Versão Stories para Instagram/TikTok
- **Aspect ratio preservado** - Sem distorções

### **Efeitos Profissionais**
- **Fade in/out** - Transições suaves (0.3s)
- **Contracapa** - 4 segundos de fechamento
- **Trilha sonora** - Sincronização automática
- **Crop inteligente** - Centro mantido no Stories

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
- **Vídeo 9:16** - Mesma sequência cortada para Stories
- **Galeria HTML** - Visualização das imagens geradas
- **Dados JSON** - Metadados dos personagens para reutilização

---

**Feito com ❤️ e muito minimalismo brasileiro! 🇧🇷**
