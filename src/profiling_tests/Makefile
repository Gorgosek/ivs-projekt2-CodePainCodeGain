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

profile: profile-run clean
profile-run: gen
	$(INTERPRETER) ../standard_deviation.py < t1.txt
	$(INTERPRETER) ../standard_deviation.py < t2.txt
	$(INTERPRETER) ../standard_deviation.py < t3.txt
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

run-profiler-vystup: profiler-vystup-gen clean
profiler-vystup-gen: gen
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


.DEFAULT_GOAL := all
