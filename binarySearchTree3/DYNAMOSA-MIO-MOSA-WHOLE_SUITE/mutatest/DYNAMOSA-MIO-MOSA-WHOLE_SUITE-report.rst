Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.695264
 - Clean trial 2 run time: 0:00:00.404939
 - Mutation trials total run time: 0:00:14.242883

Overall mutation trial summary
==============================
 - DETECTED: 18
 - SURVIVED: 6
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-06 08:09:54.040217


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 159, c: 27) - mutation from None to False
 - binarySearchTree3.py: (l: 159, c: 27) - mutation from None to True
 - binarySearchTree3.py: (l: 169, c: 20) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - binarySearchTree3.py: (l: 177, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - binarySearchTree3.py: (l: 358, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 358, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree3.py: (l: 32, c: 20) - mutation from None to True
 - binarySearchTree3.py: (l: 32, c: 20) - mutation from None to False
 - binarySearchTree3.py: (l: 38, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 38, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 47, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 47, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 247, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 310, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 310, c: 8) - mutation from If_Statement to If_False