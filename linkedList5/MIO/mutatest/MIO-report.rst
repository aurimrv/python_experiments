Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
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
 - Clean trial 1 run time: 0:00:02.066647
 - Clean trial 2 run time: 0:00:01.146691
 - Mutation trials total run time: 0:00:30.073386

Overall mutation trial summary
==============================
 - SURVIVED: 3
 - DETECTED: 14
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-03-05 01:27:57.671340


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 45, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 45, c: 19) - mutation from None to False
 - linkedList5.py: (l: 45, c: 19) - mutation from None to True


DETECTED
--------
 - linkedList5.py: (l: 13, c: 28) - mutation from None to True
 - linkedList5.py: (l: 13, c: 28) - mutation from None to False
 - linkedList5.py: (l: 35, c: 24) - mutation from None to False
 - linkedList5.py: (l: 35, c: 24) - mutation from None to True
 - linkedList5.py: (l: 39, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 45, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 48, c: 31) - mutation from None to True
 - linkedList5.py: (l: 48, c: 31) - mutation from None to False
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 55, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 80, c: 36) - mutation from None to True
 - linkedList5.py: (l: 80, c: 36) - mutation from None to False
 - linkedList5.py: (l: 95, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>