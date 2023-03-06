Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.480242
 - Clean trial 2 run time: 0:00:00.320530
 - Mutation trials total run time: 0:00:13.092559

Overall mutation trial summary
==============================
 - SURVIVED: 5
 - DETECTED: 20
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-06 08:09:27.923767


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 142, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 142, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 156, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 18, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 18, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 18, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 18, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 18, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 40, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 40, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 58, c: 15) - mutation from None to False
 - binarySearchTree1.py: (l: 58, c: 15) - mutation from None to True
 - binarySearchTree1.py: (l: 97, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 97, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 105, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 105, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 136, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree1.py: (l: 156, c: 8) - mutation from If_Statement to If_True