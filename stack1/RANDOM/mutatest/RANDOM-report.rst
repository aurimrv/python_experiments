Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
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
 - Clean trial 1 run time: 0:00:34.735866
 - Clean trial 2 run time: 0:00:01.949681
 - Mutation trials total run time: 0:18:05.323374

Overall mutation trial summary
==============================
 - TIMEOUT: 6
 - SURVIVED: 17
 - DETECTED: 2
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-03 18:27:34.640655


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Sub'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Add'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Pow'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mod'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mult'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Mult'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Sub'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Div'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Add'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.FloorDiv'>


TIMEOUT
-------
 - stack1.py: (l: 9, c: 20) - mutation from None to False
 - stack1.py: (l: 26, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 61, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 76, c: 15) - mutation from True to False


DETECTED
--------
 - stack1.py: (l: 70, c: 23) - mutation from False to True
 - stack1.py: (l: 70, c: 23) - mutation from False to None