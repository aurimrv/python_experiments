Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
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
 - Clean trial 1 run time: 0:00:01.505857
 - Clean trial 2 run time: 0:00:01.132414
 - Mutation trials total run time: 0:00:52.033372

Overall mutation trial summary
==============================
 - DETECTED: 23
 - SURVIVED: 5
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-05 01:08:19.026011


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 78, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 78, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 156, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 20, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 25, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree1.py: (l: 64, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 64, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 90, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree1.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - binarySearchTree1.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 124, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 124, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 156, c: 8) - mutation from If_Statement to If_True