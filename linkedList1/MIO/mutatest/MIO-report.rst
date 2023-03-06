Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 53
 - Location sample coverage: 18.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.230154
 - Clean trial 2 run time: 0:00:01.115979
 - Mutation trials total run time: 0:00:48.742884

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 26
 - TOTAL RUNS: 33
 - RUN DATETIME: 2023-03-05 01:25:30.974387


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>


DETECTED
--------
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 53, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - linkedList1.py: (l: 130, c: 24) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Div