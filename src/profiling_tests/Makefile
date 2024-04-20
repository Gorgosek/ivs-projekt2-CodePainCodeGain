INTERPRETER = python3
DEPS_LIST_FILEPATH = python_requirements.txt
PIP = pip3
CLEAN_DIRS = __pycache__
GENERATED_FILES = t1.txt t2.txt t3.txt profiling_stats
PROFILER_OUTPUTMD = vystup.md

.PHONY: all test doc run pack clean profile

# Installs dependencies and runs the program
all: profile

# Runs the program
run: deps
	$(INTERPRETER) calculator.py
deps:
	$(PIP) install -r $(DEPS_LIST_FILEPATH)
gen:    
	$(INTERPRETER) generate_nums.py 10 > t1.txt
	$(INTERPRETER) generate_nums.py 1000 > t2.txt
	$(INTERPRETER) generate_nums.py 1000000 > t3.txt

clean:
	-rm -r ../$(CLEAN_DIRS)
	-rm $(GENERATED_FILES)

profile: run-profiler clean

run-profiler: gen
	# ORIGINAL
	echo "# Profiler outputfile:" > $(PROFILER_OUTPUTMD)
	echo "" >> $(PROFILER_OUTPUTMD)
	echo "## Output for 10 numbers:" >> $(PROFILER_OUTPUTMD)
	echo '```' >> $(PROFILER_OUTPUTMD)
	$(INTERPRETER) ../standard_deviation.py < t1.txt >> $(PROFILER_OUTPUTMD)
	echo '```' >> $(PROFILER_OUTPUTMD)
	echo "" >> $(PROFILER_OUTPUTMD)
	echo "## Output for 1 000 numbers:" >> $(PROFILER_OUTPUTMD)
	echo '```' >> $(PROFILER_OUTPUTMD)
	$(INTERPRETER) ../standard_deviation.py < t2.txt >> $(PROFILER_OUTPUTMD)
	echo '```' >> $(PROFILER_OUTPUTMD)
	echo "" >> $(PROFILER_OUTPUTMD)
	echo "## Output for 1 000 000 numbers:" >> $(PROFILER_OUTPUTMD)
	echo '```' >> $(PROFILER_OUTPUTMD)
	$(INTERPRETER) ../standard_deviation.py < t3.txt >> $(PROFILER_OUTPUTMD)
	echo '```' >> $(PROFILER_OUTPUTMD)
# NUMPY OPTIMIZED
	# $(INTERPRETER) ../np_standard_deviation.py < t1.txt
	# $(INTERPRETER) ../np_standard_deviation.py < t2.txt
	# $(INTERPRETER) ../np_standard_deviation.py < t3.txt
# CONTROL USING statistics.stdev()
	# $(INTERPRETER) check_std_correctness.py < t1.txt
	# $(INTERPRETER) check_std_correctness.py < t2.txt
	# $(INTERPRETER) check_std_correctness.py < t3.txt
# 100 MILION VALUES TESTS (takes a long time)
	# $(INTERPRETER) ../standard_deviation.py < test5-10to8.txt
	# $(INTERPRETER) ../np_standard_deviation.py < test5-10to8.txt
	# $(INTERPRETER) check_std_correctness.py < test5-10to8.txt


.DEFAULT_GOAL := all
