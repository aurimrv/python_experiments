Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 44
 - Location sample coverage: 22.73 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.197025
 - Clean trial 2 run time: 0:00:01.274557
 - Mutation trials total run time: 0:00:29.007255

Overall mutation trial summary
==============================
 - SURVIVED: 12
 - DETECTED: 11
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-05 01:29:32.827431


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 11, c: 20) - mutation from None to False
 - queue3.py: (l: 11, c: 20) - mutation from None to True
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 88, c: 35) - mutation from None to False
 - queue3.py: (l: 88, c: 35) - mutation from None to True
 - queue3.py: (l: 97, c: 28) - mutation from None to True
 - queue3.py: (l: 97, c: 28) - mutation from None to False


DETECTED
--------
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 66, c: 32) - mutation from None to False
 - queue3.py: (l: 66, c: 32) - mutation from None to True
 - queue3.py: (l: 74, c: 32) - mutation from None to True
 - queue3.py: (l: 74, c: 32) - mutation from None to False
 - queue3.py: (l: 83, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 83, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 87, c: 32) - mutation from None to True
 - queue3.py: (l: 87, c: 32) - mutation from None to False
 - queue3.py: (l: 106, c: 15) - mutation from True to False
 - queue3.py: (l: 106, c: 15) - mutation from True to None