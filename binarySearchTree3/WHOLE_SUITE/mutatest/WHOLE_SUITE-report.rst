Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:01.516741
 - Clean trial 2 run time: 0:00:01.526166
 - Mutation trials total run time: 0:00:56.539995

Overall mutation trial summary
==============================
 - DETECTED: 23
 - SURVIVED: 13
 - TOTAL RUNS: 36
 - RUN DATETIME: 2023-03-05 01:49:13.049437


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 177, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 177, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 313, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 370, c: 8) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree3.py: (l: 49, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 49, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 49, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 263, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 271, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 310, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 310, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 313, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 370, c: 8) - mutation from If_Statement to If_False