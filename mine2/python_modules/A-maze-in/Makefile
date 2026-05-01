PYTHON      = python3
PIP         = pip3
MAIN        = a_maze_ing.py
CONFIG      = config.txt
PACKAGE_DIR = srcs

all: install lint run

.PHONY: install run debug clean lint lint-strict

install:
	$(PIP) install --upgrade pip
	$(PIP) install -e .

run:
	$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

package:
	python3 -m build
	mv dist/mazegen-* .
	rm -rf dist build *.egg-info

clean:
	rm -rf `find . -type d -name "__pycache__"`
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf build/
	rm -rf dist/
	rm maze.txt
	rm -rf *.egg-info

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict
