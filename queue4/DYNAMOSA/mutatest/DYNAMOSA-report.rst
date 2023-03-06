Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 50
 - Location sample coverage: 20.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.301454
 - Clean trial 2 run time: 0:00:01.026005
 - Mutation trials total run time: 0:00:28.088071

Overall mutation trial summary
==============================
 - DETECTED: 16
 - SURVIVED: 5
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-03-05 01:16:54.518844


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 7, c: 55) - mutation from None to False
 - queue4.py: (l: 30, c: 28) - mutation from None to False
 - queue4.py: (l: 59, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 102, c: 59) - mutation from None to False
 - queue4.py: (l: 102, c: 59) - mutation from None to True


DETECTED
--------
 - queue4.py: (l: 7, c: 44) - mutation from None to True
 - queue4.py: (l: 7, c: 44) - mutation from None to False
 - queue4.py: (l: 7, c: 55) - mutation from None to True
 - queue4.py: (l: 30, c: 28) - mutation from None to True
 - queue4.py: (l: 59, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 98, c: 43) - mutation from None to False
 - queue4.py: (l: 98, c: 43) - mutation from None to True
 - queue4.py: (l: 98, c: 49) - mutation from None to True
 - queue4.py: (l: 98, c: 49) - mutation from None to False
 - queue4.py: (l: 99, c: 21) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue4.py: (l: 101, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>