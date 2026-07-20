PYTHON := python3
PIP := $(PYTHON) -m pip
MAP := t.txt

.PHONY: install run debug clean lint lint-strict

install:
	$(PYTHON) -m pip install --upgrade pip
		$(PIP) install -U pygame mypy flake8;

run:
	$(PYTHON) main.py $(MAP)

debug:
	$(PYTHON) -m pdb main.py

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
