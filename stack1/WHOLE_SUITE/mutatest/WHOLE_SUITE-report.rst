Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:01.024775
 - Clean trial 2 run time: 0:00:01.172161
 - Mutation trials total run time: 0:00:32.484589

Overall mutation trial summary
==============================
 - SURVIVED: 15
 - DETECTED: 13
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-05 01:57:02.407870


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 23) - mutation from None to False
 - stack1.py: (l: 15, c: 23) - mutation from None to True
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Sub'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Add'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Pow'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Mod'>
 - stack1.py: (l: 96, c: 29) - mutation from <class 'ast.Mult'> to <class 'ast.Div'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Div'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Mod'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Sub'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Add'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Mult'>
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_False


DETECTED
--------
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack1.py: (l: 29, c: 23) - mutation from None to False
 - stack1.py: (l: 29, c: 23) - mutation from None to True
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_False
 - stack1.py: (l: 66, c: 16) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 73, c: 15) - mutation from False to None
 - stack1.py: (l: 73, c: 15) - mutation from False to True
 - stack1.py: (l: 106, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_True