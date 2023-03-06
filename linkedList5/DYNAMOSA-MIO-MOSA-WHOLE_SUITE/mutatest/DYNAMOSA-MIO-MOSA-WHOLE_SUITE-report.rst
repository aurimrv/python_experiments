Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.978186
 - Clean trial 2 run time: 0:00:00.351256
 - Mutation trials total run time: 0:00:09.819454

Overall mutation trial summary
==============================
 - DETECTED: 12
 - SURVIVED: 5
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-03-06 08:10:57.083616


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 26, c: 19) - mutation from None to True
 - linkedList5.py: (l: 26, c: 19) - mutation from None to False
 - linkedList5.py: (l: 33, c: 19) - mutation from None to False
 - linkedList5.py: (l: 33, c: 19) - mutation from None to True
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 32, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 32, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 39, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 39, c: 36) - mutation from None to True
 - linkedList5.py: (l: 39, c: 36) - mutation from None to False
 - linkedList5.py: (l: 52, c: 15) - mutation from None to True
 - linkedList5.py: (l: 52, c: 15) - mutation from None to False
 - linkedList5.py: (l: 57, c: 24) - mutation from None to False
 - linkedList5.py: (l: 57, c: 24) - mutation from None to True
 - linkedList5.py: (l: 64, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 74, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>