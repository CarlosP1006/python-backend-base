PROJECT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

venv:
	cd /d "$(PROJECT_DIR)" && if not exist .venv\Scripts\python.exe python -m venv .venv

install: venv
	cd /d "$(PROJECT_DIR)" && .venv\Scripts\pip.exe install -r requirements.txt

dev: venv
	cd /d "$(PROJECT_DIR)" && .venv\Scripts\python.exe -B -m src.main