Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 36
 - Location sample coverage: 27.78 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:24.730454
 - Clean trial 2 run time: 0:00:01.916690
 - Mutation trials total run time: 0:13:56.723727

Overall mutation trial summary
==============================
 - TIMEOUT: 5
 - SURVIVED: 8
 - DETECTED: 2
 - TOTAL RUNS: 15
 - RUN DATETIME: 2023-03-03 16:42:13.703398


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - linkedList2.py: (l: 16, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 21, c: 32) - mutation from True to None
 - linkedList2.py: (l: 21, c: 32) - mutation from True to False
 - linkedList2.py: (l: 22, c: 15) - mutation from False to True
 - linkedList2.py: (l: 22, c: 15) - mutation from False to None
 - linkedList2.py: (l: 37, c: 24) - mutation from None to True
 - linkedList2.py: (l: 37, c: 24) - mutation from None to False


TIMEOUT
-------
 - linkedList2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 16, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 27, c: 21) - mutation from None to False
 - linkedList2.py: (l: 37, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 66, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>


DETECTED
--------
 - linkedList2.py: (l: 53, c: 23) - mutation from True to False
 - linkedList2.py: (l: 53, c: 23) - mutation from True to None