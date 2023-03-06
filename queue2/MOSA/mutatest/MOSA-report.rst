Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './MOSA']
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
 - Clean trial 1 run time: 0:00:01.482858
 - Clean trial 2 run time: 0:00:01.095807
 - Mutation trials total run time: 0:00:44.583640

Overall mutation trial summary
==============================
 - DETECTED: 21
 - SURVIVED: 7
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-05 01:41:56.180776


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 21, c: 32) - mutation from True to False
 - queue2.py: (l: 21, c: 32) - mutation from True to None
 - queue2.py: (l: 66, c: 24) - mutation from None to True
 - queue2.py: (l: 66, c: 24) - mutation from None to False
 - queue2.py: (l: 107, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 107, c: 24) - mutation from None to True
 - queue2.py: (l: 107, c: 24) - mutation from None to False


DETECTED
--------
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 16, c: 26) - mutation from None to True
 - queue2.py: (l: 16, c: 26) - mutation from None to False
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 99, c: 28) - mutation from None to False
 - queue2.py: (l: 99, c: 28) - mutation from None to True