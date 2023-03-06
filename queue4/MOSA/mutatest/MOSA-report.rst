Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './MOSA']
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
 - Clean trial 1 run time: 0:00:01.357420
 - Clean trial 2 run time: 0:00:00.962477
 - Mutation trials total run time: 0:00:32.177095

Overall mutation trial summary
==============================
 - DETECTED: 15
 - SURVIVED: 9
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-05 01:43:11.115321


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 46, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 59, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 60, c: 28) - mutation from None to True
 - queue4.py: (l: 60, c: 28) - mutation from None to False
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 135, c: 28) - mutation from None to False


DETECTED
--------
 - queue4.py: (l: 46, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 59, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 64, c: 24) - mutation from None to False
 - queue4.py: (l: 64, c: 24) - mutation from None to True
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 97, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 97, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 135, c: 28) - mutation from None to True