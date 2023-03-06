Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './RANDOM']
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
 - Clean trial 1 run time: 0:00:08.668412
 - Clean trial 2 run time: 0:00:02.074238
 - Mutation trials total run time: 0:04:21.521140

Overall mutation trial summary
==============================
 - SURVIVED: 16
 - TIMEOUT: 5
 - DETECTED: 1
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-03 15:32:16.698659


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 72, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 72, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 78, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 78, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - binarySearchTree1.py: (l: 140, c: 23) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 147, c: 17) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>


TIMEOUT
-------
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - binarySearchTree1.py: (l: 68, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - binarySearchTree1.py: (l: 86, c: 20) - mutation from None to False
 - binarySearchTree1.py: (l: 111, c: 24) - mutation from None to False


DETECTED
--------
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_False