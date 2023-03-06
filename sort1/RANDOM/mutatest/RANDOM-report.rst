Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
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
 - Clean trial 1 run time: 0:00:03.095356
 - Clean trial 2 run time: 0:00:01.729755
 - Mutation trials total run time: 0:01:39.849859

Overall mutation trial summary
==============================
 - DETECTED: 3
 - SURVIVED: 24
 - TIMEOUT: 3
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-03 18:08:52.362630


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_False
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_True
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 92, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 92, c: 12) - mutation from If_Statement to If_False
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>


TIMEOUT
-------
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>


DETECTED
--------
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>