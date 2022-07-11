help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-mypy ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	# N.B. line below removes editable intallation of package in venv
	# find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-mypy: ## remove MyPy cache files
	rm -fr .mypy_cache/


init: clean ## install the package in editable mode including dev dependencies
	pip install -e .[dev]
	pre-commit install

package-install: ## install the package without dev dependencies
	pip install .

test: ## run tests quickly with the default Python
	python -m pytest -m unit

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

format: ## format all Python code using black
	python -m black --line-length=100 .

.ONESHELL:
lint: ## run pylint
	python -m pylint $(SRC) --rcfile=$(ABS_ROOT_PATH)/.pylintrc
	exit_code=$$?
	python -m pylint \
		--disable duplicate-code \
		--disable missing-module-docstring \
		--disable missing-function-docstring \
		tests --rcfile=$(ABS_ROOT_PATH)/.pylintrc
	exit_code=`expr $${exit_code} + $$?`
	if [ "$${exit_code}" != 0 ]; then
		exit "$${exit_code}"
	fi

bump = patch
bumpversion: ## Bumps the (default: patch) version of this package. To bump minor or major, add bump=minor or bump=major to the make call.
	bumpversion --allow-dirty $(bump)
	- pre-commit run trailing-whitespace --file setup.cfg
	- pre-commit run remove-tabs --file setup.cfg


.ONESHELL:
pre-commit:
	pre-commit run --all-files
