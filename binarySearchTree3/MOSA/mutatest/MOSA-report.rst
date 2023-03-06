Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './MOSA']
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
 - Clean trial 1 run time: 0:00:02.003047
 - Clean trial 2 run time: 0:00:01.440236
 - Mutation trials total run time: 0:00:46.651651

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 11
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-05 01:36:06.733503


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 83, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 249, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 249, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 273, c: 17) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 397, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 397, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree3.py: (l: 83, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 97, c: 49) - mutation from None to True
 - binarySearchTree3.py: (l: 97, c: 49) - mutation from None to False
 - binarySearchTree3.py: (l: 98, c: 21) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree3.py: (l: 247, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 247, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 249, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 249, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 249, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 325, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 325, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 374, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 374, c: 28) - mutation from None to False