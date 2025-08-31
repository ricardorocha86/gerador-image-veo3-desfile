# ANIME PRINCIPAL - definir aqui
NOME_ANIME = 'Cavaleiros do Zodíaco'

# CONFIGURAÇÕES DE PERSONAGENS
QUANTIDADE_PERSONAGENS = 4  # Quantidade total de personagens (use no maximo 7)

# CHAVE DA API GOOGLE - configurar aqui
API_KEY = 'AIzaSyAXOCQ7nO0tNb7d5vx-hCAb8epXui1o8Aw'  # Sua chave da API do Google

# MODELOS DE IA - escolher aqui
MODELO_GERADOR_PERSONAGEM = "gemini-2.5-flash-image-preview"  # Para gerar imagens de personagens
MODELO_GERADOR_CENARIO = "gemini-2.5-flash-image-preview"      # Para gerar cenários
MODELO_OBTER_PERSONAGENS = "gemini-2.5-flash"                  # Para obter lista de personagens

# MODELO PARA GERAR VÍDEOS
MODELO_GERADOR_VIDEO = "veo-2.0-generate-001"              # Para gerar vídeos

# OPÇÕES DISPONÍVEIS:
# Vídeo:  "veo-3.0-fast-generate-preview" (melhor custo beneficio), 
#         "veo-3.0-generate-preview" (melhor qualidade), 
#         "veo-2.0-generate-001" (mais barato)
# Imagem: "gemini-2.5-flash-image-preview" 
# Texto:  "gemini-2.5-flash" 

# PROMPT DO CENÁRIO
PROMPT_CENARIO_TEMPLATE = """
OUTPUT IMAGE ONLY

=== OBJETIVO PRINCIPAL ===
Criar um cenário de desfile de moda numa escola infantil temática de {nome_anime}, SEM modelos na passarela, focando apenas no ambiente dinâmico repleto de referências do anime.

=== AMBIENTE ESCOLAR TEMÁTICO ===
- Local: Auditório ou quadra de uma escola infantil decorada com tema {nome_anime}
- Palco improvisado com decorações coloridas inspiradas em {nome_anime} feitas pelas próprias crianças
- Passarela simples feita com tapetes coloridos nas cores características de {nome_anime}
- Cartazes e desenhos infantis dos personagens de {nome_anime} decorando as paredes ao fundo
- Símbolos e elementos icônicos de {nome_anime} espalhados pela decoração
- Iluminação escolar adaptada com holofotes improvisados

=== PLATEIA INFANTIL TEMÁTICA ===
- Crianças de 4 a 8 anos sentadas em cadeirinhas pequenas da escola
- Todas vestidas elegantemente como se fosse um baile de gala:
  - Meninas: vestidinhos de festa, laços no cabelo, sapatinhos brilhantes
  - Meninos: ternos pequenos, gravatas, sapatos sociais miniatura
- Algumas crianças usando acessórios sutis inspirados em {nome_anime}
- Crianças aplaudindo animadamente e apontando para a passarela
- Algumas segurando celulares dos pais para gravar
- Expressões de encantamento e alegria nos rostinhos

=== REFERÊNCIAS DE {nome_anime} NO CENÁRIO ===
- Banners e pôsteres de {nome_anime} decorando as paredes
- Balões coloridos nas cores características do anime
- Bandeirinhas com símbolos e elementos do anime penduradas no teto
- Desenhos infantis dos personagens principais colados nas paredes
- Elementos decorativos temáticos espalhados pelo ambiente
- Cores dominantes inspiradas na paleta visual de {nome_anime}

=== DETALHES DO CENÁRIO ===
- Passarela no centro, elevada como um pequeno palco escolar
- Espaço amplo e vazio na passarela (sem nenhum modelo presente)
- Decorações coloridas e festivas típicas de evento escolar com tema {nome_anime}
- Professoras ao fundo organizando e supervisionando

=== ATMOSFERA E ILUMINAÇÃO ===
- Ambiente acolhedor e festivo de escola infantil
- Iluminação suave mas alegre, típica de evento escolar
- Cores vibrantes inspiradas em {nome_anime} dominando o cenário
- Sensação de evento especial e mágico para as crianças fãs do anime
- SEM texto, palavras ou letras visíveis na imagem
"""

# PROMPT PARA OBTER PERSONAGENS - customizar aqui
PROMPT_PERSONAGENS_TEMPLATE = """
=== OBJETIVO PRINCIPAL ===
Gerar lista de personagens do anime '{nome_anime}' para desfile de moda no estilo humano realístico em ambiente de desfile de moda.

=== SELEÇÃO DE PERSONAGENS ===
- Total de personagens: {quantidade_total} mais famosos e queridos do público
- Distribuição: MAIORIA personagens principais da obra + ALGUNS personagens clássicos/icônicos
- Critério: Popularidade e reconhecimento pelos fãs
- Priorize personagens principais, mas inclua alguns clássicos memoráveis

=== INFORMAÇÕES OBRIGATÓRIAS PARA CADA PERSONAGEM ===

**nome_personagem:**
- Nome principal e mais simples, sem títulos desnecessários
- Exemplo: "Luffy" ao invés de "Monkey D. Luffy"

**cor_personagem:**
- Uma única cor simples associada ao personagem
- Formato: escrita por extenso em português
- Exemplos: "vermelho", "azul", "verde", "amarelo"

**acao_tipica:**
- Descrição EXTREMAMENTE DETALHADA e MINUCIOSA em inglês
- Ação maluca e dinâmica para vídeo de 8 segundos no desfile
- Deve incluir: movimentos específicos do corpo, gestos característicos, efeitos visuais únicos
- Deve incluir: velocidade dos movimentos, habilidades especiais do personagem
- Seja MUITO específico nos detalhes da ação

**pose_inicial:**
- Descrição EXTREMAMENTE DETALHADA e MINUCIOSA em inglês
- Para frame inicial do vídeo de desfile
- Deve incluir: posição exata do corpo, ângulo das pernas e braços, postura das mãos
- Deve incluir: expressão facial específica, direção do olhar, detalhes da roupa característica
- Deve incluir: acessórios, penteado, elementos visuais únicos do personagem
- Seja MUITO preciso em cada detalhe visual

=== FORMATO DE SAÍDA ===
- Lista JSON com objetos contendo as 4 chaves obrigatórias

=== RESTRIÇÕES IMPORTANTES ===
- Na 'pose_inicial': SEM texto, palavras, letras ou elementos textuais
- Apenas descrições de poses, roupas e características visuais
- Descrições em inglês para compatibilidade com gerador de vídeo
"""

# PROMPT PARA GERAR IMAGEM DE PERSONAGEM - customizar aqui
PROMPT_IMAGEM_PERSONAGEM_TEMPLATE = """
OUTPUT IMAGE ONLY

=== OBJETIVO PRINCIPAL ===
GERAR O PERSONAGEM {nome} DE {nome_anime} INSERIDO E IMERSO NO AMBIENTE DA IMAGEM EM ANEXO.

=== CARACTERÍSTICAS DA CRIANÇA ===
- Versão CRIANÇA DE 4 ANOS do personagem {nome}
- Cabeça desproporcionalmente GRANDE comparada ao corpo (pra ficar hilário mas 'cute')
- Corpo pequeno e rechonchudo de criança de 4 anos
- Rosto infantil com bochechas arredondadas
- Olhos grandes e expressivos típicos de criança
- Altura total da criança: aproximadamente 1 metro
- Tem que ficar uma gracinha

=== REALISMO FOTOGRÁFICO ===
- OBRIGATÓRIO: Aparência 100% humana realista, NUNCA desenho ou anime
- Pele humana real com textura natural, poros visíveis
- Iluminação natural e profissional
- Qualidade de fotografia de revista de moda
- Renderização fotorrealista perfeita

=== FIDELIDADE AO PERSONAGEM ORIGINAL ===
- Manter TODAS as características visuais únicas de {nome}
- Cor de cabelo, penteado e estilo EXATAMENTE como o personagem original
- Roupas inspiradas no visual icônico de {nome}, adaptadas para criança de 4 anos
- Personalidade e expressão facial características do personagem
- Todos os acessórios e detalhes visuais marcantes do personagem
- Adicione elementos discretos na cor: **{cor}** que combinem com o personagem

=== POSE E POSICIONAMENTO ===
- A pose inicial do personagem é: {pose}
- Criança posicionada no CENTRO EXATO da imagem
- CRIANÇA DEVE SER PEQUENA: ocupar APENAS 40% ou MENOS da altura total da imagem
- MUITO espaço vazio acima da cabeça (30% ou mais da imagem)
- MUITO espaço vazio abaixo dos pés (30% ou mais da imagem)
- Perspectiva MUITO distante, criança deve parecer pequena e distante
- ENFATIZAR: criança pequena no meio de um espaço grande

=== INSERÇÃO NO AMBIENTE ===
- INSERIR o personagem criança DENTRO do cenário da imagem em anexo
- ADAPTAR perfeitamente ao ambiente existente na imagem
- Manter a iluminação e atmosfera do cenário original
- Posicionar no centro da passarela do ambiente anexo
- IMPORTANTE: criança deve ficar pequena e proporcional ao ambiente
- SEM texto, palavras ou letras na imagem
"""

