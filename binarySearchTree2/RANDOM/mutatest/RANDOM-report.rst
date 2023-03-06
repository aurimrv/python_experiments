Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
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
 - Clean trial 1 run time: 0:00:19.259922
 - Clean trial 2 run time: 0:00:02.099845
 - Mutation trials total run time: 0:14:32.833695

Overall mutation trial summary
==============================
 - SURVIVED: 3
 - TIMEOUT: 9
 - TOTAL RUNS: 12
 - RUN DATETIME: 2023-03-03 15:47:11.147483


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 34, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 67, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 67, c: 12) - mutation from If_Statement to If_False


TIMEOUT
-------
 - binarySearchTree2.py: (l: 34, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 46, c: 19) - mutation from None to False
 - binarySearchTree2.py: (l: 59, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to False
 - binarySearchTree2.py: (l: 120, c: 49) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 169, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>