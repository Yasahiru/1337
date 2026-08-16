PYTHON      = python3
PIP         = $(PYTHON) -m pip
MAIN        = a_maze_ing.py
CONFIG      = config.txt


all: install lint run

.PHONY: install run debug clean lint lint-strict package

install:
	$(PIP) install --upgrade pip
	$(PIP) install build
	$(PIP) install -e .

run:
	$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

package:
	$(PYTHON) -m build
	mv dist/mazegen-* .
	rm -rf dist
	rm -rf build
	rm -rf mazegen.egg-info

clean:
	rm -rf `find . -type d -name "__pycache__"`
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -f maze.txt

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
