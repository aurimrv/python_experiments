Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 35
 - Location sample coverage: 28.57 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.060139
 - Clean trial 2 run time: 0:00:01.015082
 - Mutation trials total run time: 0:00:32.258371

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 11
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-05 01:18:46.727915


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - stack1.py: (l: 9, c: 20) - mutation from None to False
 - stack1.py: (l: 9, c: 20) - mutation from None to True
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 67, c: 27) - mutation from False to True
 - stack1.py: (l: 67, c: 27) - mutation from False to None
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 73, c: 15) - mutation from False to None
 - stack1.py: (l: 73, c: 15) - mutation from False to True
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_True