Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './MOSA']
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
 - Clean trial 1 run time: 0:00:01.425947
 - Clean trial 2 run time: 0:00:01.140672
 - Mutation trials total run time: 0:00:29.240609

Overall mutation trial summary
==============================
 - SURVIVED: 8
 - DETECTED: 14
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-05 01:35:14.729633


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 29, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 86, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree2.py: (l: 102, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 102, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to True
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to False
 - binarySearchTree2.py: (l: 186, c: 0) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 186, c: 0) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 21, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to False
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to True
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 29, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 29, c: 28) - mutation from None to False
 - binarySearchTree2.py: (l: 29, c: 28) - mutation from None to True
 - binarySearchTree2.py: (l: 59, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>