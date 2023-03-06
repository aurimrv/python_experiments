Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
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
 - Clean trial 1 run time: 0:00:01.597624
 - Clean trial 2 run time: 0:00:01.050096
 - Mutation trials total run time: 0:00:31.747194

Overall mutation trial summary
==============================
 - DETECTED: 16
 - SURVIVED: 6
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-05 01:28:59.293228


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 15, c: 20) - mutation from None to False
 - queue2.py: (l: 15, c: 20) - mutation from None to True
 - queue2.py: (l: 21, c: 32) - mutation from True to False
 - queue2.py: (l: 21, c: 32) - mutation from True to None
 - queue2.py: (l: 37, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 120, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue2.py: (l: 37, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 120, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 120, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 129, c: 19) - mutation from None to False
 - queue2.py: (l: 129, c: 19) - mutation from None to True
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Div