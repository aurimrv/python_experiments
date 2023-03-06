Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 32
 - Location sample coverage: 31.25 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.965668
 - Clean trial 2 run time: 0:00:01.131686
 - Mutation trials total run time: 0:00:40.434184

Overall mutation trial summary
==============================
 - SURVIVED: 24
 - DETECTED: 9
 - TIMEOUT: 1
 - TOTAL RUNS: 34
 - RUN DATETIME: 2023-03-05 01:44:21.055842


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_False
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_True
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower


TIMEOUT
-------
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_Unbounded
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>