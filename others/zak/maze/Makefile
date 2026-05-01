CONFIG_FILE = config.txt
VENV_PATH = .venv/bin

LINT_FLAGS = --warn-return-any \
	     --warn-unused-ignores \
	     --ignore-missing-imports \
	     --disallow-untyped-defs \
	     --check-untyped-defs

install:
	$(VENV_PATH)/pip install requirements.txt

run:
	$(VENV_PATH)/python a_maze_ing.py $(CONFIG_FILE)

debug:
	$(VENV_PATH)/python -m pdb a_maze_ing.py $(CONFIG_FILE)

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache
	rm -rf ./**/__pycache__ ./**/.mypy_cache ./**/.pytest_cache

lint:
	$(VENV_PATH)/flake8 .
	$(VENV_PATH)/mypy . $(LINT_FLAGS)

lint_strict:
	$(VENV_PATH)/flake8 .
	$(VENV_PATH)/mypy . --strict

