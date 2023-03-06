Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 67
 - Location sample coverage: 14.93 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.677761
 - Clean trial 2 run time: 0:00:01.172700
 - Mutation trials total run time: 0:00:47.768861

Overall mutation trial summary
==============================
 - SURVIVED: 9
 - DETECTED: 17
 - TOTAL RUNS: 26
 - RUN DATETIME: 2023-03-05 01:34:40.601690


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 147, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 147, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>


DETECTED
--------
 - binarySearchTree1.py: (l: 12, c: 23) - mutation from None to False
 - binarySearchTree1.py: (l: 12, c: 23) - mutation from None to True
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 40, c: 28) - mutation from None to True
 - binarySearchTree1.py: (l: 40, c: 28) - mutation from None to False
 - binarySearchTree1.py: (l: 64, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 64, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 102, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 102, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 129, c: 15) - mutation from False to True
 - binarySearchTree1.py: (l: 129, c: 15) - mutation from False to None
 - binarySearchTree1.py: (l: 137, c: 19) - mutation from None to True
 - binarySearchTree1.py: (l: 137, c: 19) - mutation from None to False