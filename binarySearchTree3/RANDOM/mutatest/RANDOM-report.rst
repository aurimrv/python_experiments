Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 116
 - Location sample coverage: 8.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:27.726793
 - Clean trial 2 run time: 0:00:01.902890
 - Mutation trials total run time: 0:07:45.812161

Overall mutation trial summary
==============================
 - SURVIVED: 23
 - TIMEOUT: 3
 - DETECTED: 1
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-03 15:55:26.854625


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 87, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 87, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 87, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 87, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 87, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 150, c: 19) - mutation from None to False
 - binarySearchTree3.py: (l: 159, c: 40) - mutation from None to True
 - binarySearchTree3.py: (l: 159, c: 40) - mutation from None to False
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 258, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 258, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Sub


TIMEOUT
-------
 - binarySearchTree3.py: (l: 70, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 95, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 228, c: 28) - mutation from None to True


DETECTED
--------
 - binarySearchTree3.py: (l: 150, c: 19) - mutation from None to True