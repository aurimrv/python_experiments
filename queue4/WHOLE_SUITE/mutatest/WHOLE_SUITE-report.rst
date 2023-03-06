Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:01.230014
 - Clean trial 2 run time: 0:00:01.161124
 - Mutation trials total run time: 0:00:22.840510

Overall mutation trial summary
==============================
 - DETECTED: 7
 - SURVIVED: 12
 - TOTAL RUNS: 19
 - RUN DATETIME: 2023-03-05 01:55:06.354004


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 7, c: 55) - mutation from None to True
 - queue4.py: (l: 7, c: 55) - mutation from None to False
 - queue4.py: (l: 30, c: 28) - mutation from None to False
 - queue4.py: (l: 60, c: 28) - mutation from None to False
 - queue4.py: (l: 60, c: 28) - mutation from None to True
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 135, c: 28) - mutation from None to True
 - queue4.py: (l: 135, c: 28) - mutation from None to False
 - queue4.py: (l: 152, c: 19) - mutation from None to False
 - queue4.py: (l: 152, c: 19) - mutation from None to True


DETECTED
--------
 - queue4.py: (l: 30, c: 28) - mutation from None to True
 - queue4.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 99, c: 21) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue4.py: (l: 99, c: 47) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>