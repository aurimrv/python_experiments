Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 59
 - Location sample coverage: 16.95 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.547344
 - Clean trial 2 run time: 0:00:00.317144
 - Mutation trials total run time: 0:00:09.909542

Overall mutation trial summary
==============================
 - SURVIVED: 6
 - DETECTED: 13
 - TOTAL RUNS: 19
 - RUN DATETIME: 2023-03-06 08:11:14.954750


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 21, c: 32) - mutation from True to None
 - queue2.py: (l: 21, c: 32) - mutation from True to False
 - queue2.py: (l: 37, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 49, c: 16) - mutation from If_Statement to If_True
 - queue2.py: (l: 107, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 120, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - queue2.py: (l: 37, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 49, c: 16) - mutation from If_Statement to If_False
 - queue2.py: (l: 75, c: 19) - mutation from None to False
 - queue2.py: (l: 75, c: 19) - mutation from None to True
 - queue2.py: (l: 90, c: 36) - mutation from None to True
 - queue2.py: (l: 90, c: 36) - mutation from None to False
 - queue2.py: (l: 91, c: 24) - mutation from None to True
 - queue2.py: (l: 91, c: 24) - mutation from None to False
 - queue2.py: (l: 120, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 129, c: 19) - mutation from None to False
 - queue2.py: (l: 129, c: 19) - mutation from None to True