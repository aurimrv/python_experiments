Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 59
 - Location sample coverage: 16.95 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:33.973510
 - Clean trial 2 run time: 0:00:02.132799
 - Mutation trials total run time: 0:14:41.418263

Overall mutation trial summary
==============================
 - SURVIVED: 11
 - TIMEOUT: 5
 - DETECTED: 1
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-03-03 17:41:04.641381


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 15, c: 35) - mutation from None to True
 - queue2.py: (l: 15, c: 35) - mutation from None to False
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 66, c: 24) - mutation from None to True
 - queue2.py: (l: 66, c: 24) - mutation from None to False
 - queue2.py: (l: 107, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 107, c: 8) - mutation from If_Statement to If_False


TIMEOUT
-------
 - queue2.py: (l: 16, c: 26) - mutation from None to False
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 91, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 91, c: 24) - mutation from None to False
 - queue2.py: (l: 99, c: 28) - mutation from None to False


DETECTED
--------
 - queue2.py: (l: 120, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>