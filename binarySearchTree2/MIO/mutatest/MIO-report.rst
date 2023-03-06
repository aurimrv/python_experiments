Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 77
 - Location sample coverage: 12.99 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.307176
 - Clean trial 2 run time: 0:00:01.040351
 - Mutation trials total run time: 0:00:46.366374

Overall mutation trial summary
==============================
 - DETECTED: 27
 - SURVIVED: 4
 - TOTAL RUNS: 31
 - RUN DATETIME: 2023-03-05 01:22:38.765245


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to True
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to False


DETECTED
--------
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to None
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to True
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 31, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 31, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 31, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 46, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 49, c: 19) - mutation from True to None
 - binarySearchTree2.py: (l: 49, c: 19) - mutation from True to False
 - binarySearchTree2.py: (l: 59, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree2.py: (l: 124, c: 11) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 124, c: 11) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 124, c: 11) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 124, c: 11) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 124, c: 11) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 127, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - binarySearchTree2.py: (l: 127, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - binarySearchTree2.py: (l: 127, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - binarySearchTree2.py: (l: 127, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - binarySearchTree2.py: (l: 127, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - binarySearchTree2.py: (l: 127, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>