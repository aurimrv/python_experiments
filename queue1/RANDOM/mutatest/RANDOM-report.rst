Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue1/queue1.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 17
 - Location sample coverage: 58.82 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:02.577436
 - Clean trial 2 run time: 0:00:00.431260
 - Mutation trials total run time: 0:01:22.147434

Overall mutation trial summary
==============================
 - DETECTED: 6
 - SURVIVED: 4
 - TIMEOUT: 5
 - TOTAL RUNS: 15
 - RUN DATETIME: 2023-03-03 17:25:46.855116


Mutations by result status
==========================


SURVIVED
--------
 - queue1.py: (l: 11, c: 14) - mutation from None to False
 - queue1.py: (l: 11, c: 14) - mutation from None to True
 - queue1.py: (l: 45, c: 10) - mutation from None to True
 - queue1.py: (l: 45, c: 10) - mutation from None to False


TIMEOUT
-------
 - queue1.py: (l: 10, c: 15) - mutation from None to False
 - queue1.py: (l: 23, c: 5) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue1.py: (l: 44, c: 2) - mutation from If_Statement to If_False
 - queue1.py: (l: 44, c: 5) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue1.py: (l: 44, c: 19) - mutation from None to False


DETECTED
--------
 - queue1.py: (l: 35, c: 2) - mutation from If_Statement to If_False
 - queue1.py: (l: 35, c: 2) - mutation from If_Statement to If_True
 - queue1.py: (l: 35, c: 5) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue1.py: (l: 35, c: 19) - mutation from None to False
 - queue1.py: (l: 35, c: 19) - mutation from None to True
 - queue1.py: (l: 44, c: 2) - mutation from If_Statement to If_True