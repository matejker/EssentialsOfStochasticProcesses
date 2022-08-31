TEST_PATH=./tests
MIN_COVERAGE=80

.PHONY: requirements
requirements:
	poetry install --no-dev

.PHONY: requirements_tools
requirements_tools:
	poetry install

.PHONY: notebook
notebook: requirements_tools
	poetry run jupyter notebook

.PHONY: ipython
ipython: requirements_tools
	poetry run ipython
