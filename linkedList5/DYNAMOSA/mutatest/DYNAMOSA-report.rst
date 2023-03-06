Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 55
 - Location sample coverage: 18.18 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:02.416108
 - Clean trial 2 run time: 0:00:01.285179
 - Mutation trials total run time: 0:00:35.452050

Overall mutation trial summary
==============================
 - DETECTED: 12
 - SURVIVED: 6
 - TOTAL RUNS: 18
 - RUN DATETIME: 2023-03-05 01:14:31.517984


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 33, c: 19) - mutation from None to False
 - linkedList5.py: (l: 33, c: 19) - mutation from None to True
 - linkedList5.py: (l: 45, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 46, c: 19) - mutation from None to True
 - linkedList5.py: (l: 46, c: 19) - mutation from None to False
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 13, c: 28) - mutation from None to True
 - linkedList5.py: (l: 13, c: 28) - mutation from None to False
 - linkedList5.py: (l: 35, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 35, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 39, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 45, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 48, c: 31) - mutation from None to False
 - linkedList5.py: (l: 48, c: 31) - mutation from None to True
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 88, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>