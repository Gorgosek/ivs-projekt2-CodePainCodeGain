# Stats

## GOOGLE TABLE
[](https://docs.google.com/spreadsheets/d/1IYO5rM8VRftpOit8__mbqtAXBnHD48psSik66RdWGAE/edit?usp=sharing) 

**test6-tenmillionNONROUNDED**
- my: 577213.8724766021
- statistics.stdev: 577213.8724765829
- time
    - *DEFAULT 40045584 function calls in 11.406 seconds*
    ```
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    3.813    3.813    5.140    5.140 standard_deviation.py:9(read_stdin)
            1    2.823    2.823    4.201    4.201 standard_deviation.py:32(sum_of_squared_differences)
     20000000    1.293    0.000    1.293    0.000 calculatormathlib.py:24(add)
            1    1.273    1.273    1.886    1.886 standard_deviation.py:23(sum)
     10000000    0.698    0.000    0.698    0.000 calculatormathlib.py:75(pow2)
            1    0.640    0.640    0.640    0.640 {method 'split' of 'str' objects}
     10000000    0.478    0.000    0.478    0.000 {method 'append' of 'list' objects}
            1    0.179    0.179   11.406   11.406 standard_deviation.py:53(main)
            1    0.102    0.102    0.102    0.102 {method 'strip' of 'str' objects}
        22784    0.100    0.000    0.100    0.000 {built-in method _codecs.utf_8_decode}
        22784    0.008    0.000    0.107    0.000 codecs.py:319(decode)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
            1    0.000    0.000   11.406   11.406 {built-in method builtins.exec}
            1    0.000    0.000    6.087    6.087 standard_deviation.py:40(standard_deviation)
            1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
            2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
            1    0.000    0.000   11.406   11.406 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    ```
    - *numpy arr, quick read: 30000019 function calls in 11.397 seconds*
    ```
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    3.613    3.613    5.544    5.544 standard_deviation.py:28(sum_of_squared_differences)
            1    2.268    2.268    2.268    2.268 {built-in method numpy.array}
     20000000    1.828    0.000    1.828    0.000 calculatormathlib.py:24(add)
            1    1.675    1.675    2.546    2.546 standard_deviation.py:19(sum)
     10000000    0.973    0.000    0.973    0.000 calculatormathlib.py:75(pow2)
            1    0.651    0.651    0.651    0.651 {method 'split' of 'str' objects}
            1    0.184    0.184    3.297    3.297 standard_deviation.py:9(read_stdin)
            1    0.104    0.104    0.104    0.104 {built-in method _codecs.utf_8_decode}
            1    0.089    0.089    0.194    0.194 {method 'read' of '_io.TextIOWrapper' objects}
            1    0.009    0.009   11.396   11.396 standard_deviation.py:49(main)
            1    0.000    0.000   11.397   11.397 <string>:1(<module>)
            1    0.000    0.000   11.397   11.397 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
            1    0.000    0.000    8.090    8.090 standard_deviation.py:36(standard_deviation)
            1    0.000    0.000    0.104    0.104 codecs.py:319(decode)
            2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
            1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
            1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
    ```

## NEW TESTS STANDARDIZED

### RUN no.1

```log
python3 ../standard_deviation.py < test1-10to1.txt
563285339.6970111
Sat Apr 20 00:59:53 2024    profiling_stats

         60 function calls in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:9(read_stdin)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:32(sum_of_squared_differences)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:40(standard_deviation)
        2    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:23(sum)
       20    0.000    0.000    0.000    0.000 calculatormathlib.py:24(add)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:53(main)
        2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       10    0.000    0.000    0.000    0.000 calculatormathlib.py:75(pow2)
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)


python3 ../standard_deviation.py < test2-10to3.txt
576589468.806305
Sat Apr 20 00:59:53 2024    profiling_stats

         4024 function calls in 0.002 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 standard_deviation.py:9(read_stdin)
        1    0.000    0.000    0.001    0.001 standard_deviation.py:32(sum_of_squared_differences)
        1    0.000    0.000    0.000    0.000 standard_deviation.py:23(sum)
     2000    0.000    0.000    0.000    0.000 calculatormathlib.py:24(add)
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
     1000    0.000    0.000    0.000    0.000 calculatormathlib.py:75(pow2)
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.002    0.002 standard_deviation.py:53(main)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        1    0.000    0.000    0.001    0.001 standard_deviation.py:40(standard_deviation)
        4    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)


python3 ../standard_deviation.py < test3-10to6.txt
577408887.7060071
Sat Apr 20 00:59:54 2024    profiling_stats

         4004576 function calls in 1.130 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.370    0.370    0.500    0.500 standard_deviation.py:9(read_stdin)
        1    0.285    0.285    0.422    0.422 standard_deviation.py:32(sum_of_squared_differences)
  2000000    0.129    0.000    0.129    0.000 calculatormathlib.py:24(add)
        1    0.128    0.128    0.189    0.189 standard_deviation.py:23(sum)
  1000000    0.070    0.000    0.070    0.000 calculatormathlib.py:75(pow2)
        1    0.061    0.061    0.061    0.061 {method 'split' of 'str' objects}
  1000000    0.046    0.000    0.046    0.000 {method 'append' of 'list' objects}
        1    0.019    0.019    1.130    1.130 standard_deviation.py:53(main)
     2280    0.011    0.000    0.011    0.000 {built-in method _codecs.utf_8_decode}
        1    0.011    0.011    0.011    0.011 {method 'strip' of 'str' objects}
     2280    0.001    0.000    0.012    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    1.130    1.130 {built-in method builtins.exec}
        1    0.000    0.000    0.611    0.611 standard_deviation.py:40(standard_deviation)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    1.130    1.130 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


python3 ../standard_deviation.py < test4-10to7.txt
577367520.9076962
Sat Apr 20 01:00:06 2024    profiling_stats

         40045586 function calls in 11.263 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.658    3.658    4.956    4.956 standard_deviation.py:9(read_stdin)
        1    2.805    2.805    4.204    4.204 standard_deviation.py:32(sum_of_squared_differences)
 20000000    1.344    0.000    1.344    0.000 calculatormathlib.py:24(add)
        1    1.266    1.266    1.920    1.920 standard_deviation.py:23(sum)
 10000000    0.710    0.000    0.710    0.000 calculatormathlib.py:75(pow2)
        1    0.632    0.632    0.632    0.632 {method 'split' of 'str' objects}
 10000000    0.459    0.000    0.459    0.000 {method 'append' of 'list' objects}
        1    0.182    0.182   11.263   11.263 standard_deviation.py:53(main)
        1    0.103    0.103    0.103    0.103 {method 'strip' of 'str' objects}
    22785    0.097    0.000    0.097    0.000 {built-in method _codecs.utf_8_decode}
    22785    0.008    0.000    0.105    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    6.125    6.125 standard_deviation.py:40(standard_deviation)
        1    0.000    0.000   11.263   11.263 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000   11.263   11.263 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


python3 ../np_standard_deviation.py < test1-10to1.txt
563285339.6970111
Sat Apr 20 01:00:06 2024    profiling_stats

         45 function calls in 0.001 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 {method 'reduce' of 'numpy.ufunc' objects}
        1    0.000    0.000    0.000    0.000 np_standard_deviation.py:20(sum_of_squared_differences)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.001    0.001 np_standard_deviation.py:28(standard_deviation)
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 np_standard_deviation.py:9(read_stdin)
        1    0.000    0.000    0.001    0.001 np_standard_deviation.py:40(main)
       10    0.000    0.000    0.000    0.000 calculatormathlib.py:24(add)
       10    0.000    0.000    0.000    0.000 calculatormathlib.py:75(pow2)
        1    0.000    0.000    0.001    0.001 fromnumeric.py:71(_wrapreduction)
        1    0.000    0.000    0.001    0.001 fromnumeric.py:2177(sum)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 fromnumeric.py:72(<dictcomp>)
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2172(_sum_dispatcher)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


python3 ../np_standard_deviation.py < test2-10to3.txt
576589468.806305
Sat Apr 20 01:00:06 2024    profiling_stats

         2025 function calls in 0.001 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 np_standard_deviation.py:20(sum_of_squared_differences)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
     1000    0.000    0.000    0.000    0.000 calculatormathlib.py:75(pow2)
     1000    0.000    0.000    0.000    0.000 calculatormathlib.py:24(add)
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 np_standard_deviation.py:9(read_stdin)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.001    0.001 np_standard_deviation.py:28(standard_deviation)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:71(_wrapreduction)
        1    0.000    0.000    0.001    0.001 np_standard_deviation.py:40(main)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2177(sum)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:72(<dictcomp>)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2172(_sum_dispatcher)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)


python3 ../np_standard_deviation.py < test3-10to6.txt
577408887.7060071
Sat Apr 20 01:00:07 2024    profiling_stats

         2000025 function calls in 0.874 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.359    0.359    0.552    0.552 np_standard_deviation.py:20(sum_of_squared_differences)
        1    0.215    0.215    0.215    0.215 {built-in method numpy.array}
  1000000    0.097    0.000    0.097    0.000 calculatormathlib.py:75(pow2)
  1000000    0.096    0.000    0.096    0.000 calculatormathlib.py:24(add)
        1    0.067    0.067    0.067    0.067 {method 'split' of 'str' objects}
        1    0.018    0.018    0.319    0.319 np_standard_deviation.py:9(read_stdin)
        1    0.011    0.011    0.011    0.011 {built-in method _codecs.utf_8_decode}
        1    0.009    0.009    0.020    0.020 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.001    0.001    0.874    0.874 np_standard_deviation.py:40(main)
        1    0.001    0.001    0.001    0.001 {method 'reduce' of 'numpy.ufunc' objects}
        1    0.000    0.000    0.874    0.874 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.553    0.553 np_standard_deviation.py:28(standard_deviation)
        1    0.000    0.000    0.011    0.011 codecs.py:319(decode)
        1    0.000    0.000    0.001    0.001 fromnumeric.py:71(_wrapreduction)
        1    0.000    0.000    0.001    0.001 fromnumeric.py:2177(sum)
        1    0.000    0.000    0.874    0.874 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 fromnumeric.py:72(<dictcomp>)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2172(_sum_dispatcher)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


python3 ../np_standard_deviation.py < test4-10to7.txt
577367520.9076962
Sat Apr 20 01:00:16 2024    profiling_stats

         20000025 function calls in 8.494 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.464    3.464    5.331    5.331 np_standard_deviation.py:20(sum_of_squared_differences)
        1    2.145    2.145    2.145    2.145 {built-in method numpy.array}
 10000000    0.940    0.000    0.940    0.000 calculatormathlib.py:75(pow2)
 10000000    0.927    0.000    0.927    0.000 calculatormathlib.py:24(add)
        1    0.635    0.635    0.635    0.635 {method 'split' of 'str' objects}
        1    0.177    0.177    3.146    3.146 np_standard_deviation.py:9(read_stdin)
        1    0.103    0.103    0.103    0.103 {built-in method _codecs.utf_8_decode}
        1    0.086    0.086    0.189    0.189 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.009    0.009    8.493    8.493 np_standard_deviation.py:40(main)
        1    0.007    0.007    0.007    0.007 {method 'reduce' of 'numpy.ufunc' objects}
        1    0.001    0.001    8.494    8.494 <string>:1(<module>)
        1    0.000    0.000    8.494    8.494 {built-in method builtins.exec}
        1    0.000    0.000    5.338    5.338 np_standard_deviation.py:28(standard_deviation)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.103    0.103 codecs.py:319(decode)
        1    0.000    0.000    0.007    0.007 fromnumeric.py:2177(sum)
        1    0.000    0.000    0.007    0.007 fromnumeric.py:71(_wrapreduction)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 fromnumeric.py:72(<dictcomp>)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2172(_sum_dispatcher)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

```
#### CONTROL READSTDIN OPTIMIZED
```
python3 check_std_correctness.py < test1-10to1.txt
563285339.6970111
Sat Apr 20 01:27:20 2024    profiling_stats

         239 function calls (237 primitive calls) in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 check_std_correctness.py:13(read_stdin)
       18    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
        1    0.000    0.000    0.000    0.000 statistics.py:150(_sum)
        1    0.000    0.000    0.000    0.000 statistics.py:697(_ss)
        8    0.000    0.000    0.000    0.000 fractions.py:451(_add)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       26    0.000    0.000    0.000    0.000 {built-in method math.gcd}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       20    0.000    0.000    0.000    0.000 {method 'as_integer_ratio' of 'float' objects}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
       20    0.000    0.000    0.000    0.000 statistics.py:240(_exact_ratio)
        8    0.000    0.000    0.000    0.000 fractions.py:356(forward)
        1    0.000    0.000    0.000    0.000 statistics.py:725(variance)
        2    0.000    0.000    0.000    0.000 codecs.py:319(decode)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
        5    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
        1    0.000    0.000    0.000    0.000 statistics.py:816(stdev)
       10    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
       18    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x5a8a544409a0}
       17    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
        1    0.000    0.000    0.000    0.000 check_std_correctness.py:24(main)
        5    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
       17    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
        2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       10    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 check_std_correctness.py:8(compute_std)
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}


python3 check_std_correctness.py < test2-10to3.txt
576589468.8063052
Sat Apr 20 01:27:20 2024    profiling_stats

         6400 function calls (6398 primitive calls) in 0.003 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 check_std_correctness.py:13(read_stdin)
        1    0.001    0.001    0.002    0.002 statistics.py:697(_ss)
        1    0.001    0.001    0.001    0.001 statistics.py:150(_sum)
     2000    0.001    0.000    0.001    0.000 {method 'as_integer_ratio' of 'float' objects}
     2000    0.000    0.000    0.001    0.000 statistics.py:240(_exact_ratio)
     1000    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       46    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
       22    0.000    0.000    0.000    0.000 fractions.py:451(_add)
       68    0.000    0.000    0.000    0.000 {built-in method math.gcd}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        4    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.003    0.003 check_std_correctness.py:24(main)
       22    0.000    0.000    0.000    0.000 fractions.py:356(forward)
        4    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       12    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
        1    0.000    0.000    0.002    0.002 statistics.py:725(variance)
       46    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x5b62088469a0}
       24    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       12    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
       45    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
        1    0.000    0.000    0.002    0.002 statistics.py:816(stdev)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
       45    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
        1    0.000    0.000    0.002    0.002 check_std_correctness.py:8(compute_std)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
       11    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
        1    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}


python3 check_std_correctness.py < test3-10to6.txt
577408887.7060004
Sat Apr 20 01:27:23 2024    profiling_stats

         6005572 function calls (6005570 primitive calls) in 2.113 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.570    0.570    1.599    1.599 statistics.py:697(_ss)
        1    0.367    0.367    0.495    0.495 check_std_correctness.py:13(read_stdin)
  2000000    0.355    0.000    0.355    0.000 {method 'as_integer_ratio' of 'float' objects}
        1    0.325    0.325    0.714    0.714 statistics.py:150(_sum)
  2000000    0.276    0.000    0.632    0.000 statistics.py:240(_exact_ratio)
  1000000    0.072    0.000    0.072    0.000 {method 'get' of 'dict' objects}
        1    0.060    0.060    0.060    0.060 {method 'split' of 'str' objects}
  1000000    0.046    0.000    0.046    0.000 {method 'append' of 'list' objects}
        1    0.019    0.019    2.113    2.113 check_std_correctness.py:24(main)
        1    0.011    0.011    0.011    0.011 {method 'strip' of 'str' objects}
     2280    0.010    0.000    0.010    0.000 {built-in method _codecs.utf_8_decode}
     2280    0.001    0.000    0.011    0.000 codecs.py:319(decode)
      126    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
       62    0.000    0.000    0.000    0.000 fractions.py:451(_add)
      188    0.000    0.000    0.000    0.000 {built-in method math.gcd}
        2    0.000    0.000    0.001    0.000 {built-in method builtins.sum}
       62    0.000    0.000    0.000    0.000 fractions.py:356(forward)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       32    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
       32    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
      126    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x6303a37c89a0}
        1    0.000    0.000    1.599    1.599 statistics.py:725(variance)
        1    0.000    0.000    2.113    2.113 {built-in method builtins.exec}
       64    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      125    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
      125    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    1.599    1.599 statistics.py:816(stdev)
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
       31    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
        1    0.000    0.000    1.599    1.599 check_std_correctness.py:8(compute_std)
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    2.113    2.113 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}


python3 check_std_correctness.py < test4-10to7.txt
577367520.9077069
Sat Apr 20 01:27:44 2024    profiling_stats

         60046703 function calls (60046701 primitive calls) in 21.735 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    5.881    5.881   16.500   16.500 statistics.py:697(_ss)
        1    3.748    3.748    5.056    5.056 check_std_correctness.py:13(read_stdin)
 20000000    3.619    0.000    3.619    0.000 {method 'as_integer_ratio' of 'float' objects}
        1    3.391    3.391    7.395    7.395 statistics.py:150(_sum)
 20000000    2.872    0.000    6.491    0.000 statistics.py:240(_exact_ratio)
 10000000    0.737    0.000    0.737    0.000 {method 'get' of 'dict' objects}
        1    0.640    0.640    0.640    0.640 {method 'split' of 'str' objects}
 10000000    0.462    0.000    0.462    0.000 {method 'append' of 'list' objects}
        1    0.180    0.180   21.735   21.735 check_std_correctness.py:24(main)
        1    0.102    0.102    0.102    0.102 {method 'strip' of 'str' objects}
    22785    0.096    0.000    0.096    0.000 {built-in method _codecs.utf_8_decode}
    22785    0.008    0.000    0.103    0.000 codecs.py:319(decode)
      142    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
       70    0.000    0.000    0.000    0.000 fractions.py:451(_add)
      209    0.000    0.000    0.000    0.000 {built-in method math.gcd}
        2    0.000    0.000    0.001    0.000 {built-in method builtins.sum}
       70    0.000    0.000    0.000    0.000 fractions.py:356(forward)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       36    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
       36    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
      142    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x63a73bfe69a0}
        1    0.000    0.000   16.500   16.500 statistics.py:725(variance)
       72    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000   21.735   21.735 {built-in method builtins.exec}
      141    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
      141    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000   16.500   16.500 statistics.py:816(stdev)
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
       35    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
        1    0.000    0.000   16.500   16.500 check_std_correctness.py:8(compute_std)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000   21.735   21.735 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)


#python3 ../standard_deviation.py < test5-10to8.txt
```

#### CONTROL READSTDIN OPTIMIZED

```
python3 check_std_correctness.py < test1-10to1.txt
563285339.6970111
Sat Apr 20 01:30:01 2024    profiling_stats

         228 function calls (226 primitive calls) in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       18    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
        1    0.000    0.000    0.000    0.000 statistics.py:150(_sum)
        1    0.000    0.000    0.000    0.000 statistics.py:697(_ss)
        8    0.000    0.000    0.000    0.000 fractions.py:451(_add)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
       26    0.000    0.000    0.000    0.000 {built-in method math.gcd}
       20    0.000    0.000    0.000    0.000 {method 'as_integer_ratio' of 'numpy.float64' objects}
       20    0.000    0.000    0.000    0.000 statistics.py:240(_exact_ratio)
        1    0.000    0.000    0.000    0.000 check_std_correctness.py:13(read_stdin)
        8    0.000    0.000    0.000    0.000 fractions.py:356(forward)
        1    0.000    0.000    0.000    0.000 statistics.py:725(variance)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        5    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 statistics.py:816(stdev)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
       10    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       18    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x5a6c63fa09a0}
       17    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
        5    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.000    0.000 check_std_correctness.py:18(main)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
       17    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
        1    0.000    0.000    0.000    0.000 check_std_correctness.py:8(compute_std)
       10    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        4    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}


python3 check_std_correctness.py < test2-10to3.txt
576589468.8063052
Sat Apr 20 01:30:01 2024    profiling_stats

         5395 function calls (5393 primitive calls) in 0.002 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.002    0.002 statistics.py:697(_ss)
        1    0.000    0.000    0.001    0.001 statistics.py:150(_sum)
     2000    0.000    0.000    0.000    0.000 {method 'as_integer_ratio' of 'numpy.float64' objects}
     2000    0.000    0.000    0.001    0.000 statistics.py:240(_exact_ratio)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
     1000    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       46    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
       22    0.000    0.000    0.000    0.000 fractions.py:451(_add)
       68    0.000    0.000    0.000    0.000 {built-in method math.gcd}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 check_std_correctness.py:13(read_stdin)
        1    0.000    0.000    0.002    0.002 check_std_correctness.py:8(compute_std)
       22    0.000    0.000    0.000    0.000 fractions.py:356(forward)
       12    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
        1    0.000    0.000    0.002    0.002 statistics.py:725(variance)
       46    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x64d677b9e9a0}
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.002    0.002 statistics.py:816(stdev)
       45    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
       12    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
       24    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       45    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
        1    0.000    0.000    0.002    0.002 check_std_correctness.py:18(main)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
       11    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}


python3 check_std_correctness.py < test3-10to6.txt
577408887.7060004
Sat Apr 20 01:30:03 2024    profiling_stats

         5001015 function calls (5001013 primitive calls) in 1.972 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.593    0.593    1.658    1.658 statistics.py:697(_ss)
  2000000    0.368    0.000    0.368    0.000 {method 'as_integer_ratio' of 'numpy.float64' objects}
        1    0.348    0.348    0.749    0.749 statistics.py:150(_sum)
  2000000    0.278    0.000    0.646    0.000 statistics.py:240(_exact_ratio)
        1    0.213    0.213    0.213    0.213 {built-in method numpy.array}
  1000000    0.071    0.000    0.071    0.000 {method 'get' of 'dict' objects}
        1    0.063    0.063    0.063    0.063 {method 'split' of 'str' objects}
        1    0.018    0.018    0.313    0.313 check_std_correctness.py:13(read_stdin)
        1    0.011    0.011    0.011    0.011 {built-in method _codecs.utf_8_decode}
        1    0.009    0.009    0.020    0.020 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.001    0.001    1.972    1.972 check_std_correctness.py:18(main)
      126    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
       62    0.000    0.000    0.000    0.000 fractions.py:451(_add)
      188    0.000    0.000    0.000    0.000 {built-in method math.gcd}
        2    0.000    0.000    0.001    0.000 {built-in method builtins.sum}
       62    0.000    0.000    0.000    0.000 fractions.py:356(forward)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    1.972    1.972 {built-in method builtins.exec}
       32    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
        1    0.000    0.000    0.011    0.011 codecs.py:319(decode)
        1    0.000    0.000    1.658    1.658 statistics.py:725(variance)
       32    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
      126    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x58f1b7ed89a0}
      125    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
       64    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      125    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    1.658    1.658 statistics.py:816(stdev)
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    1.658    1.658 check_std_correctness.py:8(compute_std)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
       31    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
        1    0.000    0.000    1.972    1.972 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}


python3 check_std_correctness.py < test4-10to7.txt
577367520.9077069
Sat Apr 20 01:30:23 2024    profiling_stats

         50001136 function calls (50001134 primitive calls) in 19.740 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    6.105    6.105   16.560   16.560 statistics.py:697(_ss)
 20000000    3.665    0.000    3.665    0.000 {method 'as_integer_ratio' of 'numpy.float64' objects}
        1    3.432    3.432    7.314    7.314 statistics.py:150(_sum)
 20000000    2.700    0.000    6.365    0.000 statistics.py:240(_exact_ratio)
        1    2.167    2.167    2.167    2.167 {built-in method numpy.array}
 10000000    0.656    0.000    0.656    0.000 {method 'get' of 'dict' objects}
        1    0.641    0.641    0.641    0.641 {method 'split' of 'str' objects}
        1    0.175    0.175    3.171    3.171 check_std_correctness.py:13(read_stdin)
        1    0.102    0.102    0.102    0.102 {built-in method _codecs.utf_8_decode}
        1    0.086    0.086    0.188    0.188 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.008    0.008   19.739   19.739 check_std_correctness.py:18(main)
        1    0.001    0.001   19.740   19.740 <string>:1(<module>)
      142    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
       70    0.000    0.000    0.000    0.000 fractions.py:451(_add)
      209    0.000    0.000    0.000    0.000 {built-in method math.gcd}
        2    0.000    0.000    0.001    0.000 {built-in method builtins.sum}
       70    0.000    0.000    0.000    0.000 fractions.py:356(forward)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.102    0.102 codecs.py:319(decode)
       36    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
        1    0.000    0.000   16.560   16.560 statistics.py:725(variance)
      142    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x61a6c089a9a0}
        1    0.000    0.000   19.740   19.740 {built-in method builtins.exec}
       36    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
      141    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
       72    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      141    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
        1    0.000    0.000   16.560   16.560 statistics.py:816(stdev)
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
       35    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
        1    0.000    0.000   16.560   16.560 check_std_correctness.py:8(compute_std)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)


#python3 ../standard_deviation.py < test5-10to8.txt
```

#### test5-10to8

```
python3 ../standard_deviation.py < test5-10to8.txt
577373407.7003834
Sat Apr 20 01:56:05 2024    profiling_stats

         400455692 function calls in 111.798 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   36.455   36.455   49.292   49.292 standard_deviation.py:9(read_stdin)
        1   28.173   28.173   41.942   41.942 standard_deviation.py:32(sum_of_squared_differences)
200000000   13.028    0.000   13.028    0.000 calculatormathlib.py:24(add)
        1   12.550   12.550   18.759   18.759 standard_deviation.py:23(sum)
100000000    6.950    0.000    6.950    0.000 calculatormathlib.py:75(pow2)
        1    6.327    6.327    6.327    6.327 {method 'split' of 'str' objects}
100000000    4.485    0.000    4.485    0.000 {method 'append' of 'list' objects}
        1    1.805    1.805  111.798  111.798 standard_deviation.py:53(main)
        1    1.016    1.016    1.016    1.016 {method 'strip' of 'str' objects}
   227838    0.938    0.000    0.938    0.000 {built-in method _codecs.utf_8_decode}
   227838    0.072    0.000    1.010    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000  111.798  111.798 {built-in method builtins.exec}
        1    0.000    0.000   60.702   60.702 standard_deviation.py:40(standard_deviation)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000  111.798  111.798 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)


python3 ../np_standard_deviation.py < test5-10to8.txt
577373407.7003833
Sat Apr 20 01:57:34 2024    profiling_stats

         200000025 function calls in 85.871 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   35.723   35.723   54.673   54.673 np_standard_deviation.py:20(sum_of_squared_differences)
        1   21.206   21.206   21.206   21.206 {built-in method numpy.array}
100000000    9.632    0.000    9.632    0.000 calculatormathlib.py:75(pow2)
100000000    9.318    0.000    9.318    0.000 calculatormathlib.py:24(add)
        1    6.286    6.286    6.286    6.286 {method 'split' of 'str' objects}
        1    1.728    1.728   31.054   31.054 np_standard_deviation.py:9(read_stdin)
        1    1.018    1.018    1.018    1.018 {built-in method _codecs.utf_8_decode}
        1    0.815    0.815    1.833    1.833 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.077    0.077   85.868   85.868 np_standard_deviation.py:40(main)
        1    0.064    0.064    0.064    0.064 {method 'reduce' of 'numpy.ufunc' objects}
        1    0.003    0.003   85.871   85.871 <string>:1(<module>)
        1    0.000    0.000   54.738   54.738 np_standard_deviation.py:28(standard_deviation)
        1    0.000    0.000   85.871   85.871 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    1.018    1.018 codecs.py:319(decode)
        1    0.000    0.000    0.064    0.064 fromnumeric.py:2177(sum)
        1    0.000    0.000    0.064    0.064 fromnumeric.py:71(_wrapreduction)
        2    0.000    0.000    0.000    0.000 calculatormathlib.py:60(div)
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:102(sqrt)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2172(_sum_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:72(<dictcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 calculatormathlib.py:36(sub)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


python3 check_std_correctness.py < test5-10to8.txt
577373407.7004517
Sat Apr 20 02:00:49 2024    profiling_stats

         500001323 function calls (500001321 primitive calls) in 195.118 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   59.358   59.358  163.919  163.919 statistics.py:697(_ss)
200000000   36.157    0.000   36.157    0.000 {method 'as_integer_ratio' of 'numpy.float64' objects}
        1   33.940   33.940   73.202   73.202 statistics.py:150(_sum)
200000000   27.401    0.000   63.558    0.000 statistics.py:240(_exact_ratio)
        1   21.274   21.274   21.274   21.274 {built-in method numpy.array}
100000000    7.062    0.000    7.062    0.000 {method 'get' of 'dict' objects}
        1    6.276    6.276    6.276    6.276 {method 'split' of 'str' objects}
        1    1.740    1.740   31.121   31.121 check_std_correctness.py:13(read_stdin)
        1    1.015    1.015    1.015    1.015 {built-in method _codecs.utf_8_decode}
        1    0.816    0.816    1.831    1.831 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.075    0.075  195.115  195.115 check_std_correctness.py:18(main)
        1    0.003    0.003  195.118  195.118 <string>:1(<module>)
      246    0.000    0.000    0.000    0.000 {built-in method math.gcd}
      166    0.000    0.000    0.000    0.000 fractions.py:62(__new__)
       82    0.000    0.000    0.000    0.000 fractions.py:451(_add)
        2    0.000    0.000    0.001    0.000 {built-in method builtins.sum}
       82    0.000    0.000    0.000    0.000 fractions.py:356(forward)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       42    0.000    0.000    0.000    0.000 statistics.py:198(<genexpr>)
       42    0.000    0.000    0.000    0.000 statistics.py:721(<genexpr>)
        1    0.000    0.000    1.015    1.015 codecs.py:319(decode)
        1    0.000    0.000  163.919  163.919 statistics.py:725(variance)
        1    0.000    0.000  195.118  195.118 {built-in method builtins.exec}
      166    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x5effacd4f9a0}
      165    0.000    0.000    0.000    0.000 fractions.py:256(numerator)
       84    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      165    0.000    0.000    0.000    0.000 fractions.py:260(denominator)
        1    0.000    0.000  163.919  163.919 statistics.py:816(stdev)
        1    0.000    0.000    0.000    0.000 statistics.py:264(_convert)
       41    0.000    0.000    0.000    0.000 __init__.py:579(__missing__)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        2    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        2    0.000    0.000    0.000    0.000 fractions.py:368(reverse)
        1    0.000    0.000  163.919  163.919 check_std_correctness.py:8(compute_std)
        1    0.000    0.000    0.000    0.000 __init__.py:565(__init__)
        2    0.000    0.000    0.000    0.000 fractions.py:499(_div)
        2    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
        1    0.000    0.000    0.000    0.000 numbers.py:283(__float__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
      2/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 statistics.py:209(_coerce)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 __init__.py:640(update)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
        1    0.000    0.000    0.000    0.000 fractions.py:193(as_integer_ratio)

```


