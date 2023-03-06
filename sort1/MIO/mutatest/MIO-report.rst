Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
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
 - Clean trial 1 run time: 0:00:01.056063
 - Clean trial 2 run time: 0:00:01.078107
 - Mutation trials total run time: 0:00:36.767896

Overall mutation trial summary
==============================
 - DETECTED: 3
 - SURVIVED: 25
 - TIMEOUT: 1
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-05 01:31:13.446969


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>


TIMEOUT
-------
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Sub