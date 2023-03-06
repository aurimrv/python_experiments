Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree4/binarySearchTree4.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:01.126959
 - Clean trial 2 run time: 0:00:00.998000
 - Mutation trials total run time: 0:00:20.377441

Overall mutation trial summary
==============================
 - DETECTED: 16
 - SURVIVED: 1
 - TOTAL RUNS: 17
 - RUN DATETIME: 2023-03-05 01:49:37.910776


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree4.py: (l: 30, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree4.py: (l: 6, c: 21) - mutation from None to False
 - binarySearchTree4.py: (l: 6, c: 21) - mutation from None to True
 - binarySearchTree4.py: (l: 14, c: 28) - mutation from None to False
 - binarySearchTree4.py: (l: 14, c: 28) - mutation from None to True
 - binarySearchTree4.py: (l: 18, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree4.py: (l: 18, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree4.py: (l: 18, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 20, c: 24) - mutation from None to True
 - binarySearchTree4.py: (l: 20, c: 24) - mutation from None to False
 - binarySearchTree4.py: (l: 27, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 27, c: 19) - mutation from None to False
 - binarySearchTree4.py: (l: 27, c: 19) - mutation from None to True
 - binarySearchTree4.py: (l: 30, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree4.py: (l: 30, c: 28) - mutation from None to True
 - binarySearchTree4.py: (l: 30, c: 28) - mutation from None to False
 - binarySearchTree4.py: (l: 37, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>