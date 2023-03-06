Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.223311
 - Clean trial 2 run time: 0:00:00.225931
 - Mutation trials total run time: 0:00:08.308651

Overall mutation trial summary
==============================
 - DETECTED: 9
 - SURVIVED: 20
 - TIMEOUT: 1
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-06 09:34:46.751841


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_False
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_True
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Sub


TIMEOUT
-------
 - sort1.py: (l: 34, c: 22) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>


DETECTED
--------
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Div'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Pow'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Mult'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Mod'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Sub'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Add'>
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_Unbounded
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_True