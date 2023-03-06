Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
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
 - Clean trial 1 run time: 0:00:01.753728
 - Clean trial 2 run time: 0:00:01.472706
 - Mutation trials total run time: 0:00:42.179889

Overall mutation trial summary
==============================
 - SURVIVED: 13
 - DETECTED: 12
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-05 01:23:26.156902


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 29, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 58, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 328, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 358, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 358, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 365, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 365, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 370, c: 8) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree3.py: (l: 29, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 47, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 47, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 58, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 88, c: 24) - mutation from None to True
 - binarySearchTree3.py: (l: 88, c: 24) - mutation from None to False
 - binarySearchTree3.py: (l: 95, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree3.py: (l: 328, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 365, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 365, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 365, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 370, c: 8) - mutation from If_Statement to If_False