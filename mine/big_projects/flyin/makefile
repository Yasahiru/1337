PYTHON := python3
PIP := $(PYTHON) -m pip
MAP := maps/challenger/01_the_impossible_dream.txt


.PHONY: install run debug clean lint lint-strict

install:
	$(PYTHON) -m pip install --upgrade pip
		$(PIP) install -U pygame mypy flake8;

run:
	$(PYTHON) main.py $(MAP)

run-capacity:
	$(PYTHON) main.py --capacity-info $(MAP)

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
