##
# @file Makefile
#
# @brief runs or compiles necesarry files 
#
# @author Adam Nezbeda
# @date 2024-04-09
#

ZIP_FILE = xhajekp00_xkodajj00_xnezbea00_xnovott00.zip
INTERPRETER = python3
DEPS_LIST_FILEPATH = python_requirements.txt
PIP = pip3
CLEAN_DIRS = __pycache__
# Generated files
CLEAN_FILES = t1.txt t2.txt t3.txt profiling_stats

.PHONY: all test doc run pack clean profile

# Installs dependencies and runs the program
all: run

# Runs the program
run: deps
	$(INTERPRETER) calculator.py

# Installs needed dependencies to run the program
deps:
	$(PIP) install -r $(DEPS_LIST_FILEPATH)

# runs test for the calculator_mathlib
# TODO add test for standard deviation
test: 
	$(INTERPRETER) -m unittest calculator_tests.py

gen:    
	$(INTERPRETER) generate_nums.py 10 > t1.txt
	$(INTERPRETER) generate_nums.py 1000 > t2.txt
	$(INTERPRETER) generate_nums.py 1000000 > t3.txt

profile: deps profile-run clean

profile-run: gen
	$(INTERPRETER) standard_deviation.py < t1.txt
	$(INTERPRETER) standard_deviation.py < t2.txt
	$(INTERPRETER) standard_deviation.py < t3.txt
# NUMPY OPTIMIZED
# $(INTERPRETER) ../np_standard_deviation.py < t1.txt
# $(INTERPRETER) ../np_standard_deviation.py < t2.txt
# $(INTERPRETER) ../np_standard_deviation.py < t3.txt
# CONTROL USING statistics.stdev()
# $(INTERPRETER) check_std_correctness.py < t1.txt
# $(INTERPRETER) check_std_correctness.py < t2.txt
# $(INTERPRETER) check_std_correctness.py < t3.txt
# 100 MILION VALUES TESTS (takes a long time)
# $(INTERPRETER) generate_nums.py 100000000 > t5.txt
# $(INTERPRETER) ../standard_deviation.py < t5.txt
# $(INTERPRETER) ../np_standard_deviation.py < t5.txt
# $(INTERPRETER) check_std_correctness.py < t5.txt

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

# Removes ./__pychache__ directory
clean:
	-rm -r $(CLEAN_DIRS)
	-rm $(CLEAN_FILES)

# uses `make all` when `make` is used
.DEFAULT_GOAL := all
