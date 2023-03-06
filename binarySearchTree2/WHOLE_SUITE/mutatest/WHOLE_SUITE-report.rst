Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:01.301968
 - Clean trial 2 run time: 0:00:01.088015
 - Mutation trials total run time: 0:00:23.729314

Overall mutation trial summary
==============================
 - DETECTED: 7
 - SURVIVED: 12
 - TOTAL RUNS: 19
 - RUN DATETIME: 2023-03-05 01:48:11.253665


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 28, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 35, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 81, c: 38) - mutation from None to False
 - binarySearchTree2.py: (l: 81, c: 38) - mutation from None to True
 - binarySearchTree2.py: (l: 86, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree2.py: (l: 89, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 89, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 102, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 102, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 145, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 157, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 157, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to None
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to True
 - binarySearchTree2.py: (l: 28, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 35, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to True
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to False
 - binarySearchTree2.py: (l: 145, c: 12) - mutation from If_Statement to If_True