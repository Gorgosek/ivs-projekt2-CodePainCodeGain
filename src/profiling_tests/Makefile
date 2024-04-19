INTERPRETER = python3
DEPS_LIST_FILEPATH = python_requirements.txt
PIP = pip3
CLEAN_DIRS = __pycache__

.PHONY: all test doc run pack clean profile

# Installs dependencies and runs the program
all: profile

# Runs the program
run: deps
	$(INTERPRETER) calculator.py
deps:
	$(PIP) install -r $(DEPS_LIST_FILEPATH)

test: 
	$(INTERPRETER) -m unittest calculator_tests.py

profile: clean
	# ORIGINAL
	$(INTERPRETER) ../standard_deviation.py < test1-10to1.txt
	$(INTERPRETER) ../standard_deviation.py < test2-10to3.txt
	$(INTERPRETER) ../standard_deviation.py < test3-10to6.txt
	$(INTERPRETER) ../standard_deviation.py < test4-10to7.txt
	# NUMPY OPTIMIZED
	$(INTERPRETER) ../np_standard_deviation.py < test1-10to1.txt
	$(INTERPRETER) ../np_standard_deviation.py < test2-10to3.txt
	$(INTERPRETER) ../np_standard_deviation.py < test3-10to6.txt
	$(INTERPRETER) ../np_standard_deviation.py < test4-10to7.txt
	# CONTROL USING statistics.stdev()
	$(INTERPRETER) check_std_correctness.py < test1-10to1.txt
	$(INTERPRETER) check_std_correctness.py < test2-10to3.txt
	$(INTERPRETER) check_std_correctness.py < test3-10to6.txt
	$(INTERPRETER) check_std_correctness.py < test4-10to7.txt
	# $(INTERPRETER) ../standard_deviation.py < test5-10to8.txt




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
	-rm -r ../__pycache__/

# uses `make all` when `make` is used
.DEFAULT_GOAL := all
