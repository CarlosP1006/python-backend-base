venv:
	if not exist .venv\Scripts\python.exe python -m venv .venv

install: venv
	.venv\Scripts\pip.exe install -r requirements.txt

dev: venv
	.venv\Scripts\python.exe -B -m src.main