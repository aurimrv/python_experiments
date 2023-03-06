Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
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
 - Clean trial 1 run time: 0:00:01.966902
 - Clean trial 2 run time: 0:00:01.358509
 - Mutation trials total run time: 0:00:46.194046

Overall mutation trial summary
==============================
 - SURVIVED: 8
 - DETECTED: 17
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-05 01:09:47.605993


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 102, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to True
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to False
 - binarySearchTree3.py: (l: 163, c: 20) - mutation from None to False
 - binarySearchTree3.py: (l: 179, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - binarySearchTree3.py: (l: 290, c: 27) - mutation from None to False
 - binarySearchTree3.py: (l: 310, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 310, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>


DETECTED
--------
 - binarySearchTree3.py: (l: 79, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 79, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 79, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 163, c: 20) - mutation from None to True
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 288, c: 39) - mutation from None to True
 - binarySearchTree3.py: (l: 288, c: 39) - mutation from None to False
 - binarySearchTree3.py: (l: 290, c: 27) - mutation from None to True
 - binarySearchTree3.py: (l: 310, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 310, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 310, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>