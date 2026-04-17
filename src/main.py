import os
from pathlib import Path

import uvicorn
from dotenv import load_dotenv

load_dotenv()

from src.infra.http.api_server import app
from src.infra.http.controllers.random_controller import router

app.include_router(router)


def main() -> None:
  root = Path(__file__).resolve().parent.parent
  uvicorn.run(
    "src.main:app",
    host="0.0.0.0",
    port=int(os.environ.get("API_PORT", "8080")),
    reload=True,
    reload_dirs=[str(root / "src")],
  )


if __name__ == "__main__":
  main()
