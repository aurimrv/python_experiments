Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
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
 - Clean trial 1 run time: 0:00:01.479732
 - Clean trial 2 run time: 0:00:01.210636
 - Mutation trials total run time: 0:00:31.962755

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 6
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-05 01:08:55.820367


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 35, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 47, c: 19) - mutation from False to None
 - binarySearchTree2.py: (l: 102, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 102, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree2.py: (l: 11, c: 21) - mutation from None to False
 - binarySearchTree2.py: (l: 11, c: 21) - mutation from None to True
 - binarySearchTree2.py: (l: 15, c: 20) - mutation from None to True
 - binarySearchTree2.py: (l: 15, c: 20) - mutation from None to False
 - binarySearchTree2.py: (l: 19, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 19, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 35, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 47, c: 19) - mutation from False to True
 - binarySearchTree2.py: (l: 48, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 48, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 59, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Div