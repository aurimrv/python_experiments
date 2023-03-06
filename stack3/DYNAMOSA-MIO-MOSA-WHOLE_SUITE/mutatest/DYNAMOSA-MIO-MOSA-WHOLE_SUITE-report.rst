Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.349061
 - Clean trial 2 run time: 0:00:00.263966
 - Mutation trials total run time: 0:00:07.621361

Overall mutation trial summary
==============================
 - DETECTED: 16
 - SURVIVED: 7
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-06 08:12:09.886142


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 19, c: 31) - mutation from None to False
 - stack3.py: (l: 19, c: 31) - mutation from None to True
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 50, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_False
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_True


DETECTED
--------
 - stack3.py: (l: 10, c: 20) - mutation from None to True
 - stack3.py: (l: 10, c: 20) - mutation from None to False
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack3.py: (l: 27, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 39, c: 19) - mutation from None to True
 - stack3.py: (l: 39, c: 19) - mutation from None to False
 - stack3.py: (l: 42, c: 35) - mutation from None to True
 - stack3.py: (l: 42, c: 35) - mutation from None to False
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 75, c: 45) - mutation from False to True
 - stack3.py: (l: 75, c: 45) - mutation from False to None