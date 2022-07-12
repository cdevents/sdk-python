include header.mk

PACKAGES = cli
export ABS_ROOT_PATH=$(shell pwd)

.PHONY: packages $(PACKAGES)

packages: $(PACKAGES)

$(PACKAGES):
		$(MAKE) -C $@

# the sets of directories to do various things in
INITPACKAGES = $(PACKAGES:%=init-%)
INSTALLPACKAGES = $(PACKAGES:%=package-install-%)
CLEANPACKAGES = $(PACKAGES:%=clean-%)
TESTPACKAGES = $(PACKAGES:%=test-%)
LINTPACKAGES = $(PACKAGES:%=lint-%)
FORMATPACKAGES = $(PACKAGES:%=format-%)
BUMPVERSIONPACKAGES = $(PACKAGES:%=bumpversion-%)

help: ## Prints this help text
	@python -c "$$PRINT_HELP_PYSCRIPT" < Makefile

init: $(INITPACKAGES) ## Installs all packages in editable mode including dev dependencies
$(INITPACKAGES):
	$(MAKE) -C $(@:init-%=%) init

package-install: $(INSTALLPACKAGES) ## Installs all packages without dev dependencies
$(INSTALLPACKAGES):
	$(MAKE) -C $(@:package-install-%=%) package-install

test: $(TESTPACKAGES) ## Run tests on all packages
$(TESTPACKAGES):
	$(MAKE) -C $(@:test-%=%) test

clean: $(CLEANPACKAGES) ## Remove all build, test, coverage and Python artifacts
$(CLEANPACKAGES):
	$(MAKE) -C $(@:clean-%=%) clean

bumpversion: ${BUMPVERSIONPACKAGES} ## Bumps the (default: patch) version of all release packages. To bump minor or major, add bump=minor or bump=major to the make call.
$(BUMPVERSIONPACKAGES):
	$(MAKE) -C $(@:bumpversion-%=%) bumpversion

lint: $(LINTPACKAGES)
$(LINTPACKAGES):
	$(MAKE) -C $(@:lint-%=%) lint

format: $(FORMATPACKAGES)
$(FORMATPACKAGES):
	$(MAKE) -C $(@:format-%=%) format

check: ## Runs pre-commit hooks on all files
	pre-commit run --all-files

docker-build: ## Build and package Docker container
	docker build -t cdevents -f Dockerfile .

docker-shell: ## Opens a bash
	docker run --rm --network host --volume $(pwd)/output/:/root/cdevents-client/ -it cdevents bash

.PHONY: packages $(PACKAGES)
.PHONY: packages $(INITPACKAGES)
.PHONY: packages $(INSTALLPACKAGES)
.PHONY: packages $(TESTPACKAGES)
.PHONY: packages $(CLEANPACKAGES)
.PHONY: packages $(BUMPVERSIONPACKAGES)
.PHONY: init test clean bumpversion install internal-install check docker-build docker-shell
