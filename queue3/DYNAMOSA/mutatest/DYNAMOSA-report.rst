Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 44
 - Location sample coverage: 22.73 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.467717
 - Clean trial 2 run time: 0:00:01.058151
 - Mutation trials total run time: 0:00:39.927627

Overall mutation trial summary
==============================
 - DETECTED: 24
 - SURVIVED: 7
 - TOTAL RUNS: 31
 - RUN DATETIME: 2023-03-05 01:16:21.716367


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 44, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 84, c: 19) - mutation from None to True
 - queue3.py: (l: 84, c: 19) - mutation from None to False
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 44, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 87, c: 32) - mutation from None to True
 - queue3.py: (l: 87, c: 32) - mutation from None to False
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 112, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 112, c: 8) - mutation from If_Statement to If_True