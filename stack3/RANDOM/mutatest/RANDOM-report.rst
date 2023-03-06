Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 24
 - Location sample coverage: 41.67 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:07.668640
 - Clean trial 2 run time: 0:00:01.804544
 - Mutation trials total run time: 0:03:51.143990

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 5
 - TIMEOUT: 5
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-03-03 18:32:00.298735


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 19, c: 31) - mutation from None to True
 - stack3.py: (l: 19, c: 31) - mutation from None to False
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 42, c: 35) - mutation from None to False
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 103, c: 32) - mutation from None to True
 - stack3.py: (l: 103, c: 32) - mutation from None to False


TIMEOUT
-------
 - stack3.py: (l: 24, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 39, c: 19) - mutation from None to False
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 75, c: 45) - mutation from False to None


DETECTED
--------
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 42, c: 35) - mutation from None to True
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Add