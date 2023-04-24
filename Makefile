help:
	@echo "The following make targets are available:"
	@echo "install	install all python dependencies"
	@echo "lint-comment	ensures fixme comments are grepable"
	@echo "lint-emptyinit	main inits must be empty"
	@echo "lint-flake8	run flake8 checker to deteck missing trailing comma"
	@echo "lint-forgottenformat	ensures format strings are used"
	@echo "lint-indent	run indent format check"
	@echo "lint-pycodestyle	run linter check using pycodestyle standard"
	@echo "lint-pycodestyle-debug	run linter in debug mode"
	@echo "lint-pyi	Ensure no regular python files exist in stubs"
	@echo "lint-pylint	run linter check using pylint standard"
	@echo "lint-requirements	run requirements check"
	@echo "lint-stringformat	run string format check"
	@echo "lint-type-check	run type check"
	@echo "lint-all	run all lints"
	@echo "pre-commit 	sort python package imports using isort"
	@echo "name	generate a unique permanent name for the current commit"
	@echo "git-check	ensures no git visible files have been altered"
	@echo "pytest	run all test with pytest (requires a running test redis server)"
	@echo "requirements-check	check whether the env differs from the requirements file"
	@echo "requirements-complete	check whether the requirements file is complete"
	@echo "run-api	start api server"
	@echo "coverage-report	show the coverage report for python"
	@echo "stubgen	create stubs for a package"

export LC_ALL=C
export LANG=C

PYTHON=python3
NS=default

lint-comment:
	! ./findpy.sh \
	| xargs grep --color=always -nE \
	  '#.*(todo|xxx|fixme|n[oO][tT][eE]:|Note:|nopep8\s*$$)|.\"^s%'

lint-emptyinit:
	[ ! -s app/__init__.py ]

lint-pyi:
	./pyi.sh

lint-stringformat:
	! ./findpy.sh \
	| xargs grep --color=always -nE "%[^'\"]*\"\\s*%\\s*"

lint-indent:
	! ./findpy.sh \
	| xargs grep --color=always -nE "^(\s{4})*\s{1,3}\S.*$$"

lint-forgottenformat:
	! PYTHON=$(PYTHON) ./forgottenformat.sh

lint-requirements:
	locale
	cat requirements.txt
	sort -ufc requirements.txt

lint-pycodestyle:
	./findpy.sh | sort
	./findpy.sh | sort | xargs pycodestyle --show-source

lint-pycodestyle-debug:
	./findpy.sh | sort
	./findpy.sh \
	| sort | xargs pycodestyle -v --show-source

lint-pylint:
	./findpy.sh | sort
	./findpy.sh | sort | xargs pylint -j 6 -v

lint-type-check:
	mypy --exclude=^venv/ --config-file mypy.ini .

lint-flake8:
	flake8 --verbose --select C812,C815,I001,I002,I003,I004,I005 --exclude \
	venv,.git,.mypy_cache --show-source ./

lint-all: \
	lint-comment \
	lint-emptyinit \
	lint-pyi \
	lint-stringformat \
	lint-indent \
	lint-forgottenformat \
	lint-requirements \
	requirements-complete \
	lint-pycodestyle \
	lint-pylint \
	lint-type-check \
	lint-flake8

install:
	PYTHON=$(PYTHON) ./install.sh

requirements-check:
	PYTHON=$(PYTHON) ./requirements_check.sh $(FILE)

requirements-complete:
	PYTHON=$(PYTHON) ./requirements_complete.sh $(FILE)

name:
	git describe --abbrev=10 --tags HEAD

git-check:
	./git_check.sh

pre-commit:
	pre-commit install
	isort .

pytest:
	PYTHON=$(PYTHON) RESULT_FNAME=$(RESULT_FNAME) ./run_pytest.sh $(FILE)

run-api:
	API_SERVER_NAMESPACE=$(NS) $(PYTHON) -m app

coverage-report:
	cd coverage/reports/html_report && open index.html

stubgen:
	PYTHON=$(PYTHON) FORCE=$(FORCE) ./stubgen.sh $(PKG)

allapps:
	./findpy.sh \
	| xargs grep '__name__ == "__main__"' \
	| cut -d: -f1 \
	| sed -e 's/^.\///' -e 's/\/__main__.py$$//' -e 's/.py$$//'
