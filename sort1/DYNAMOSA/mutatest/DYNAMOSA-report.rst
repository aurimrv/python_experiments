Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
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
 - Clean trial 1 run time: 0:00:01.051026
 - Clean trial 2 run time: 0:00:01.119845
 - Mutation trials total run time: 0:00:42.523479

Overall mutation trial summary
==============================
 - SURVIVED: 22
 - DETECTED: 15
 - TOTAL RUNS: 37
 - RUN DATETIME: 2023-03-05 01:18:09.996683


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Pow'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Mult'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Mod'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Add'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Div'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Sub'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_True