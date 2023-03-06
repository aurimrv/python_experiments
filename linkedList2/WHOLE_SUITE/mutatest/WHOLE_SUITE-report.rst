Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 36
 - Location sample coverage: 27.78 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.142032
 - Clean trial 2 run time: 0:00:01.086682
 - Mutation trials total run time: 0:00:26.200651

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 2
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-05 01:51:11.842485


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 21, c: 32) - mutation from True to None
 - linkedList2.py: (l: 21, c: 32) - mutation from True to False


DETECTED
--------
 - linkedList2.py: (l: 7, c: 37) - mutation from None to False
 - linkedList2.py: (l: 7, c: 37) - mutation from None to True
 - linkedList2.py: (l: 16, c: 26) - mutation from None to True
 - linkedList2.py: (l: 16, c: 26) - mutation from None to False
 - linkedList2.py: (l: 22, c: 15) - mutation from False to True
 - linkedList2.py: (l: 22, c: 15) - mutation from False to None
 - linkedList2.py: (l: 37, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 53, c: 23) - mutation from True to False
 - linkedList2.py: (l: 53, c: 23) - mutation from True to None
 - linkedList2.py: (l: 55, c: 15) - mutation from False to None
 - linkedList2.py: (l: 55, c: 15) - mutation from False to True
 - linkedList2.py: (l: 66, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub