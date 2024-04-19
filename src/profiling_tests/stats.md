# Stats

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
