<!-- Meu Corinthians -->

Projeto de uma landing page do Sport Club Corinthians Paulista, desenvolvido em etapas: primeiro com HTML, CSS e JavaScript: depois evoluído para uma aplicação com backend em Python (FastAPI) e banco de dados SQLite.

<!-- TECNOLOGIAS UTILIZADAS -->


<!-- FRONT END -->

HTML | CSS | JAVASCRIPT

LIVE SERVER(EXTENSÃO DO VSCODE)

<!-- BACK END -->

PYTHON | FAST API

<!-- SERVIDOR -->

UVICORN

<!-- BANCO DE DADOS -->

SQLITE (VIA MÓDULO SQLITE3 DO PYTHON)

<!-- ESTRUTURA DE PASTAS -->

meu-Corinthians/
├── index.html
├── style.css
├── js/
│   └── main.js
├── img/
└── backend/
    ├── main.py          # Endpoints da API (FastAPI)
    ├── database.py       # Conexão, criação de tabelas e operações no SQLite
    ├── meu_corinthians.db # Arquivo do banco (gerado automaticamente)
    └── venv/              # Ambiente virtual Python (não versionado)

<!-- COMO RODAR O PROJETO -->

Front end via LiveServer
Back end via Uvicorn


<!-- BACK END -->
# Abra um terminal na pasta Backend: 

# # Criar o ambiente virtual (só na primeira vez)
python -m venv venv

# Ativar o ambiente virtual
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (Git Bash):
source venv/Scripts/activate
# Linux/Mac:
source venv/bin/activate

# Instalar as dependências (só na primeira vez)
pip install fastapi uvicorn

# Criar e popular o banco de dados (só na primeira vez, ou se o .db for apagado)
python database.py

# Subir o servidor da API
python -m uvicorn main:app --reload:

# Uvicorn running on http://127.0.0.1:8000 copiar e colar no navegador

<!-- FRONT END -->
# No index.html :
# "Open with LiveServer"



O frontend faz requisições para http://127.0.0.1:8000, então o backend precisa estar no ar para as seções de jogadores e favoritos funcionarem.

Endpoints da API
Método	Rota	Descrição
GET	/api/jogadores	Retorna a lista completa do elenco atual, vinda do banco de dados
GET	/api/favoritos	Retorna os ids dos jogadores favoritados
POST	/api/favoritos	Favorita um jogador. Corpo: {"jogador_id": 1}
DELETE	/api/favoritos/{jogador_id}	Remove um jogador dos favoritos
Banco de dados

Duas tabelas no arquivo meu_corinthians.db:

jogadores

Coluna	Tipo	Descrição
id	INTEGER (PK, autoincrement)	Identificador único
nome	TEXT	Nome do jogador
numero	INTEGER	Número da camisa
posicao	TEXT	Posição em campo

favoritos

Coluna	Tipo	Descrição
id	INTEGER (PK, autoincrement)	Identificador único
jogador_id	INTEGER	Referência ao id da tabela jogadores

A tabela jogadores é populada automaticamente na primeira execução de database.py, com os 34 jogadores do elenco atual do Corinthians (o script verifica se a tabela já tem dados antes de inserir, para não duplicar em execuções futuras).
 
<!-- FUNCIONALIDADES -->

# Navegação por âncora com rolagem suave via JavaScript (scrollIntoView), incluindo os botões de ação da seção inicial.

# Seção "Ídolos": conteúdo histórico fixo em HTML (não muda com o tempo, por isso não usa API).

# Seção "Elenco Atual": os cards são gerados dinamicamente em JavaScript a partir dos dados retornados pela API (GET /api/jogadores), agrupados por posição.

# Sistema de favoritos: clicar na estrela (☆/★) de um jogador salva ou remove o favorito no banco de dados (via POST/DELETE), e o estado é recuperado do backend ao recarregar a página (via GET /api/favoritos), garantindo persistência real.

# Tratamento de erros: se o backend estiver fora do ar, o frontend exibe uma mensagem amigável em vez de travar ou mostrar erro técnico.

# CORS habilitado no backend, permitindo que o frontend (porta 5501) se comunique com a API (porta 8000), mesmo rodando em origens diferentes.

<!-- OBSERVAÇÕES  -->

O ambiente virtual (venv) não deve ser copiado entre computadores — cada máquina precisa criar o seu próprio, seguindo os passos da seção "Backend" acima.

Caso o arquivo meu_corinthians.db seja apagado ou não exista, basta rodar python database.py novamente: as tabelas e os dados dos jogadores são recriados automaticamente.

Os dois servidores (frontend e backend) são independentes e precisam ser iniciados separadamente, em terminais diferentes.