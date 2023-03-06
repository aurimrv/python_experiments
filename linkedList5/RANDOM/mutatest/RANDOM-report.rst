Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
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
 - Clean trial 1 run time: 0:00:38.348320
 - Clean trial 2 run time: 0:00:01.860979
 - Mutation trials total run time: 0:18:04.454168

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 5
 - TIMEOUT: 5
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-03-03 17:24:21.438452


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


TIMEOUT
-------
 - linkedList5.py: (l: 3, c: 34) - mutation from None to False
 - linkedList5.py: (l: 25, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 64, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 74, c: 24) - mutation from None to False


DETECTED
--------
 - linkedList5.py: (l: 33, c: 19) - mutation from None to True
 - linkedList5.py: (l: 33, c: 19) - mutation from None to False
 - linkedList5.py: (l: 39, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_True