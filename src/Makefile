##
# @file Makefile
#
# @brief runs or compiles necesarry files 
#
# @author Adam Nezbeda
# @date 2024-04-09
#


ZIP_FILE = xhajekp00_xkodajj00_xnezbea00_xnovott00.zip

.PHONY: all test doc run pack clean profile

# Installs dependencies and runs the program
all: run

# Runs the program
run: deps
	python calculator.py

# Installs needed dependencies to run the program
deps:
	pip install -r python_requirements.txt

# runs test for the calculator_mathlib
# TODO add test for standard deviation
test: 
	python -m unittest calculator_tests.py

# TODO FIGURE IT OUT add later when needed to be used
# Specification from the assignment: "For scripting languages use to install dependencies"
profile: deps
	###

# TODO also add later
help:
	###

# FIXME make it according to the assignment
pack:
	cd .. && \
	zip -r $(ZIP_FILE) . # creates a zip of everything inside the repo

# Generates program documentation
doc:
	doxygen Doxyfile

# uses `make all` when `make` is used
.DEFAULT_GOAL := all
