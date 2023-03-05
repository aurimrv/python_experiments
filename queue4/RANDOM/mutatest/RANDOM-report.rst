Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
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
 - Clean trial 1 run time: 0:00:42.157458
 - Clean trial 2 run time: 0:00:02.109376
 - Mutation trials total run time: 0:14:28.975993

Overall mutation trial summary
==============================
 - SURVIVED: 9
 - TIMEOUT: 4
 - TOTAL RUNS: 13
 - RUN DATETIME: 2023-03-03 18:03:16.106514


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 99, c: 21) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - queue4.py: (l: 101, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 101, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 101, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 102, c: 59) - mutation from None to False
 - queue4.py: (l: 102, c: 59) - mutation from None to True
 - queue4.py: (l: 103, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 104, c: 59) - mutation from None to False
 - queue4.py: (l: 104, c: 59) - mutation from None to True


TIMEOUT
-------
 - queue4.py: (l: 33, c: 20) - mutation from None to True
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 135, c: 28) - mutation from None to True
 - queue4.py: (l: 152, c: 19) - mutation from None to True