Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:01.820137
 - Clean trial 2 run time: 0:00:01.171819
 - Mutation trials total run time: 0:00:22.961500

Overall mutation trial summary
==============================
 - DETECTED: 12
 - SURVIVED: 6
 - TOTAL RUNS: 18
 - RUN DATETIME: 2023-03-05 01:52:56.727758


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 33, c: 19) - mutation from None to True
 - linkedList5.py: (l: 33, c: 19) - mutation from None to False
 - linkedList5.py: (l: 46, c: 19) - mutation from None to False
 - linkedList5.py: (l: 46, c: 19) - mutation from None to True
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 32, c: 19) - mutation from None to False
 - linkedList5.py: (l: 32, c: 19) - mutation from None to True
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 57, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 64, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 72, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 74, c: 24) - mutation from None to False
 - linkedList5.py: (l: 74, c: 24) - mutation from None to True
 - linkedList5.py: (l: 81, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 81, c: 12) - mutation from If_Statement to If_True