Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList4/linkedList4.py
 - Test commands: ['python', '-m', 'pytest', './MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 21
 - Location sample coverage: 47.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.255447
 - Clean trial 2 run time: 0:00:01.084175
 - Mutation trials total run time: 0:00:35.907523

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 11
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-05 01:40:00.260952


Mutations by result status
==========================


SURVIVED
--------
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList4.py: (l: 64, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 77, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 77, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 77, c: 16) - mutation from AugAssign_Sub to AugAssign_Add


DETECTED
--------
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 49, c: 8) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 49, c: 8) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 64, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded