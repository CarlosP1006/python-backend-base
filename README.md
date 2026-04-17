````markdown
# python-backend-base

Template profissional para APIs em Python com arquitetura simples, desacoplada e pronta para iniciar novos projetos.

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Dependency Injector
- python-dotenv
- Ruff

## Arquitetura

A base segue o fluxo:

HTTP Controller -> Service -> Provider/Repository

Responsabilidades:

- Controller: interface HTTP
- Service: orquestração de regra de negócio
- Provider: integrações externas ou lógica adaptadora
- Repository: acesso a dados (ou mock/in-memory no início)

## Estrutura

```text
src/
  main.py
  infra/
    containers/
      app_container.py
    database/
      entities/
        random_item.py
      repositories/
        random_repository.py
    http/
      api_server.py
      controllers/
        random_controller.py
      middlewares/
        http_error.py
  providers/
    random_provider.py
  services/
    get_random_service.py
```

## Como começar

### 1. Baixar o projeto

Clone o repositório e entre na pasta:

```powershell
git clone <url-do-repositorio>
cd python-backend-base
```

### 2. Criar o ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

### 3. Ativar o ambiente virtual

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

CMD:

```cmd
.\.venv\Scripts\activate.bat
```

### 4. Instalar as dependências

Com o ambiente ativado:

```powershell
python -m pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente

Se existir um arquivo `.env.example`, copie para `.env`:

```powershell
copy .env.example .env
```

Depois ajuste as variáveis necessárias, como:

```env
API_PORT=3000
```

### 6. Rodar o projeto

Com o ambiente ativado:

```powershell
python -m src.main
```

## Opcional: usar o Makefile

Se o `make` estiver disponível no Windows, você também pode usar:

```powershell
make install
make dev
```

Observações:

- `make install` cria o ambiente virtual, se necessário, e instala as dependências.
- `make dev` sobe a aplicação em modo de desenvolvimento.

## Endpoints

- GET /health
- GET /random

## Como usar como base

1. Renomeie os arquivos e classes de `random` para seu domínio.
2. Implemente seus providers e repositories reais.
3. Registre dependências no container em `src/infra/containers/app_container.py`.
4. Mantenha o fluxo Controller -> Service -> Provider/Repository para escalar com organização.
````
