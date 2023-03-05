Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList4/linkedList4.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
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
 - Clean trial 1 run time: 0:00:20.548072
 - Clean trial 2 run time: 0:00:01.814249
 - Mutation trials total run time: 0:15:48.432572

Overall mutation trial summary
==============================
 - TIMEOUT: 8
 - DETECTED: 3
 - SURVIVED: 3
 - TOTAL RUNS: 14
 - RUN DATETIME: 2023-03-03 17:05:36.510348


Mutations by result status
==========================


SURVIVED
--------
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Add


TIMEOUT
-------
 - linkedList4.py: (l: 10, c: 39) - mutation from None to True
 - linkedList4.py: (l: 33, c: 20) - mutation from None to True
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 45, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList4.py: (l: 71, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded


DETECTED
--------
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Add