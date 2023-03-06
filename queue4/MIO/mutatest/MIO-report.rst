Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
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
 - Clean trial 1 run time: 0:00:01.469955
 - Clean trial 2 run time: 0:00:01.422171
 - Mutation trials total run time: 0:00:26.990987

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 2
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-03-05 01:30:04.771637


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 97, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_False


DETECTED
--------
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 64, c: 24) - mutation from None to False
 - queue4.py: (l: 64, c: 24) - mutation from None to True
 - queue4.py: (l: 73, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 73, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 89, c: 24) - mutation from None to False
 - queue4.py: (l: 89, c: 24) - mutation from None to True
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 97, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 99, c: 47) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - queue4.py: (l: 101, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>