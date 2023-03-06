Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 35
 - Location sample coverage: 28.57 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.303271
 - Clean trial 2 run time: 0:00:00.264933
 - Mutation trials total run time: 0:00:06.113484

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 1
 - TOTAL RUNS: 20
 - RUN DATETIME: 2023-03-06 08:11:57.148643


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>


DETECTED
--------
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack1.py: (l: 29, c: 23) - mutation from None to False
 - stack1.py: (l: 29, c: 23) - mutation from None to True
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack1.py: (l: 39, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 48, c: 20) - mutation from None to False
 - stack1.py: (l: 48, c: 20) - mutation from None to True
 - stack1.py: (l: 67, c: 27) - mutation from False to None
 - stack1.py: (l: 67, c: 27) - mutation from False to True
 - stack1.py: (l: 70, c: 23) - mutation from False to True
 - stack1.py: (l: 70, c: 23) - mutation from False to None
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 73, c: 15) - mutation from False to True
 - stack1.py: (l: 73, c: 15) - mutation from False to None