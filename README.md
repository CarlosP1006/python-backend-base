````markdown
# python-backend-base

Template profissional para APIs em Python, com arquitetura simples, desacoplada e pronta para iniciar novos projetos.

## Visao geral

Esta base segue um fluxo claro entre camadas:

`Controller -> Service -> Provider/Repository`

Responsabilidades de cada camada:

- `Controller`: interface HTTP (entrada e saida)
- `Service`: orquestracao da regra de negocio
- `Provider`: integracoes externas ou logica adaptadora
- `Repository`: acesso a dados (in-memory, banco ou outro backend)

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Dependency Injector
- python-dotenv
- Ruff

## Estrutura do projeto

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
  utils/
    sleep.py
```

## Como executar localmente (Windows)

### 1. Clonar o repositorio

```powershell
git clone <url-do-repositorio>
cd python-backend-base
```

### 2. Criar o ambiente virtual

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

### 4. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 5. Configurar variaveis de ambiente

Copie o arquivo de exemplo:

```powershell
copy .env.example .env
```

Exemplo de valor:

```env
API_PORT=3000
```

### 6. Rodar a aplicacao

```powershell
python -m src.main
```

## Opcional: executar com Makefile

Se o `make` estiver disponivel no Windows:

```powershell
make install
make dev
```

Comandos:

- `make install`: cria `.venv` (se necessario) e instala dependencias
- `make dev`: sobe a aplicacao em modo de desenvolvimento

## Endpoints

- `GET /health`
- `GET /random`

## Como usar esta base em novos projetos

1. Renomeie os artefatos `random` para o dominio do seu negocio.
2. Implemente `providers` e `repositories` reais.
3. Registre as dependencias no container em `src/infra/containers/app_container.py`.
4. Mantenha o fluxo `Controller -> Service -> Provider/Repository` para escalar com organizacao.
````
