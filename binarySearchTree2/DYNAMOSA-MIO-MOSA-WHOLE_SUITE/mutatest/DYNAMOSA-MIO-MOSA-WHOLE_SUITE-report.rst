Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.431008
 - Clean trial 2 run time: 0:00:00.286037
 - Mutation trials total run time: 0:00:09.480391

Overall mutation trial summary
==============================
 - DETECTED: 14
 - SURVIVED: 11
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-06 08:09:38.409495


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 29, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 102, c: 17) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to True
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to False
 - binarySearchTree2.py: (l: 120, c: 40) - mutation from None to False
 - binarySearchTree2.py: (l: 129, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>


DETECTED
--------
 - binarySearchTree2.py: (l: 29, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 29, c: 28) - mutation from None to False
 - binarySearchTree2.py: (l: 29, c: 28) - mutation from None to True
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 120, c: 40) - mutation from None to True
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 129, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 163, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 163, c: 8) - mutation from If_Statement to If_False