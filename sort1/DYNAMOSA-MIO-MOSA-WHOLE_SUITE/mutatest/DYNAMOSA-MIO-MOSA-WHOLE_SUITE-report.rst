Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.255786
 - Clean trial 2 run time: 0:00:00.251530
 - Mutation trials total run time: 0:00:07.953304

Overall mutation trial summary
==============================
 - DETECTED: 10
 - SURVIVED: 14
 - TIMEOUT: 1
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-06 08:11:50.185749


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_True
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_False
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 92, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 92, c: 12) - mutation from If_Statement to If_False
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>


TIMEOUT
-------
 - sort1.py: (l: 66, c: 16) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>