Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 53
 - Location sample coverage: 18.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:37.846537
 - Clean trial 2 run time: 0:00:01.920558
 - Mutation trials total run time: 0:17:46.698167

Overall mutation trial summary
==============================
 - TIMEOUT: 5
 - DETECTED: 4
 - SURVIVED: 6
 - TOTAL RUNS: 15
 - RUN DATETIME: 2023-03-03 16:27:50.066158


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 21, c: 28) - mutation from None to False
 - linkedList1.py: (l: 21, c: 28) - mutation from None to True
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 134, c: 12) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 134, c: 12) - mutation from If_Statement to If_True


TIMEOUT
-------
 - linkedList1.py: (l: 53, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 65, c: 24) - mutation from None to False
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 113, c: 35) - mutation from None to False
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Div


DETECTED
--------
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 95, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 125, c: 24) - mutation from None to True
 - linkedList1.py: (l: 125, c: 24) - mutation from None to False