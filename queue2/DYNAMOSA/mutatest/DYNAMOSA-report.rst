Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
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
 - Clean trial 1 run time: 0:00:01.834833
 - Clean trial 2 run time: 0:00:01.080326
 - Mutation trials total run time: 0:00:33.363636

Overall mutation trial summary
==============================
 - SURVIVED: 5
 - DETECTED: 18
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-05 01:15:37.105137


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 66, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 66, c: 24) - mutation from None to False
 - queue2.py: (l: 66, c: 24) - mutation from None to True
 - queue2.py: (l: 103, c: 24) - mutation from None to False
 - queue2.py: (l: 103, c: 24) - mutation from None to True


DETECTED
--------
 - queue2.py: (l: 22, c: 15) - mutation from False to None
 - queue2.py: (l: 22, c: 15) - mutation from False to True
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 66, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 90, c: 36) - mutation from None to True
 - queue2.py: (l: 90, c: 36) - mutation from None to False
 - queue2.py: (l: 91, c: 24) - mutation from None to True
 - queue2.py: (l: 91, c: 24) - mutation from None to False
 - queue2.py: (l: 103, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 114, c: 19) - mutation from None to True
 - queue2.py: (l: 114, c: 19) - mutation from None to False
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Sub