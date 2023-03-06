Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
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
 - Clean trial 1 run time: 0:00:01.055934
 - Clean trial 2 run time: 0:00:00.969632
 - Mutation trials total run time: 0:00:28.480794

Overall mutation trial summary
==============================
 - DETECTED: 14
 - SURVIVED: 11
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-05 01:31:46.031719


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 15, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Sub'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Pow'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mod'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Add'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mult'>
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>


DETECTED
--------
 - stack1.py: (l: 29, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 29, c: 23) - mutation from None to False
 - stack1.py: (l: 29, c: 23) - mutation from None to True
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack1.py: (l: 61, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 73, c: 15) - mutation from False to None
 - stack1.py: (l: 73, c: 15) - mutation from False to True
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 106, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>