Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree4/binarySearchTree4.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 21
 - Location sample coverage: 47.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.154414
 - Clean trial 2 run time: 0:00:01.072730
 - Mutation trials total run time: 0:00:25.599493

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 1
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-03-05 01:23:56.266612


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree4.py: (l: 37, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree4.py: (l: 5, c: 20) - mutation from None to False
 - binarySearchTree4.py: (l: 5, c: 20) - mutation from None to True
 - binarySearchTree4.py: (l: 6, c: 21) - mutation from None to False
 - binarySearchTree4.py: (l: 6, c: 21) - mutation from None to True
 - binarySearchTree4.py: (l: 20, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree4.py: (l: 20, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree4.py: (l: 20, c: 24) - mutation from None to False
 - binarySearchTree4.py: (l: 20, c: 24) - mutation from None to True
 - binarySearchTree4.py: (l: 27, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 27, c: 19) - mutation from None to False
 - binarySearchTree4.py: (l: 27, c: 19) - mutation from None to True
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - binarySearchTree4.py: (l: 30, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 30, c: 28) - mutation from None to True
 - binarySearchTree4.py: (l: 30, c: 28) - mutation from None to False
 - binarySearchTree4.py: (l: 37, c: 12) - mutation from If_Statement to If_False