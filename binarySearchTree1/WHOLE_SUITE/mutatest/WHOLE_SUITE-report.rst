Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:01.242347
 - Clean trial 2 run time: 0:00:01.215799
 - Mutation trials total run time: 0:00:28.583156

Overall mutation trial summary
==============================
 - DETECTED: 15
 - SURVIVED: 7
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-05 01:47:42.887578


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 20, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 72, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 72, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 78, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 78, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 156, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 20, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 37, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 90, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 90, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 102, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 102, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 114, c: 25) - mutation from None to True
 - binarySearchTree1.py: (l: 114, c: 25) - mutation from None to False
 - binarySearchTree1.py: (l: 156, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 161, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>