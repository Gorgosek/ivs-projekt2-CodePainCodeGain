# Profiler outputfile:

## Output for 10 numbers:
```
712605522.8932176
Sat Apr 20 17:07:09 2024    profiling_stats

         60 function calls in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:9(read_stdin)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 standard_deviation.py:32(sum_of_squared_differences)
        2    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:40(standard_deviation)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:23(sum)
       20    0.000    0.000    0.000    0.000 calculatormathlib.py:24(add)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:53(main)
        2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       10    0.000    0.000    0.000    0.000 calculatormathlib.py:75(pow2)
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)


```

## Output for 1 000 numbers:
```
576195138.6245586
Sat Apr 20 17:07:09 2024    profiling_stats

         4024 function calls in 0.001 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 standard_deviation.py:9(read_stdin)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:32(sum_of_squared_differences)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:23(sum)
     2000    0.000    0.000    0.000    0.000 calculatormathlib.py:24(add)
     1000    0.000    0.000    0.000    0.000 calculatormathlib.py:75(pow2)
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.001    0.001 standard_deviation.py:53(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        4    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.001    0.001 standard_deviation.py:40(standard_deviation)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)


```

## Output for 1 000 000 numbers:
```
577743573.4479498
Sat Apr 20 17:07:11 2024    profiling_stats

         4004576 function calls in 1.153 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.366    0.366    0.499    0.499 standard_deviation.py:9(read_stdin)
        1    0.296    0.296    0.442    0.442 standard_deviation.py:32(sum_of_squared_differences)
  2000000    0.135    0.000    0.135    0.000 calculatormathlib.py:24(add)
        1    0.129    0.129    0.192    0.192 standard_deviation.py:23(sum)
  1000000    0.074    0.000    0.074    0.000 calculatormathlib.py:75(pow2)
        1    0.067    0.067    0.067    0.067 {method 'split' of 'str' objects}
  1000000    0.045    0.000    0.045    0.000 {method 'append' of 'list' objects}
        1    0.019    0.019    1.153    1.153 standard_deviation.py:53(main)
        1    0.011    0.011    0.011    0.011 {method 'strip' of 'str' objects}
     2280    0.010    0.000    0.010    0.000 {built-in method _codecs.utf_8_decode}
     2280    0.001    0.000    0.011    0.000 codecs.py:319(decode)
        1    0.000    0.000    1.153    1.153 {built-in method builtins.exec}
        1    0.000    0.000    0.634    0.634 standard_deviation.py:40(standard_deviation)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    1.153    1.153 <string>:1(<module>)


```
