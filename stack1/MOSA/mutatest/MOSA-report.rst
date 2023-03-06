Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './MOSA']
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
 - Clean trial 1 run time: 0:00:01.088935
 - Clean trial 2 run time: 0:00:01.039193
 - Mutation trials total run time: 0:00:44.469540

Overall mutation trial summary
==============================
 - DETECTED: 13
 - SURVIVED: 26
 - TOTAL RUNS: 39
 - RUN DATETIME: 2023-03-05 01:45:09.599961


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_False
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Sub'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Div'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Add'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Pow'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Mod'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Div'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Add'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Mult'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Sub'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Sub'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Div'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Mod'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Mult'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Add'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>


DETECTED
--------
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 72, c: 7) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 76, c: 15) - mutation from True to False
 - stack1.py: (l: 76, c: 15) - mutation from True to None
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>