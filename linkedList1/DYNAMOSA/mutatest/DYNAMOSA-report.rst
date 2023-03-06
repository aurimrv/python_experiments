Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 53
 - Location sample coverage: 18.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.920455
 - Clean trial 2 run time: 0:00:01.107704
 - Mutation trials total run time: 0:00:38.805524

Overall mutation trial summary
==============================
 - DETECTED: 16
 - SURVIVED: 6
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-05 01:11:44.700605


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>


DETECTED
--------
 - linkedList1.py: (l: 24, c: 19) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 25, c: 27) - mutation from True to False
 - linkedList1.py: (l: 25, c: 27) - mutation from True to None
 - linkedList1.py: (l: 27, c: 15) - mutation from False to None
 - linkedList1.py: (l: 27, c: 15) - mutation from False to True
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 53, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 107, c: 24) - mutation from None to False
 - linkedList1.py: (l: 107, c: 24) - mutation from None to True
 - linkedList1.py: (l: 125, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 178, c: 20) - mutation from None to False
 - linkedList1.py: (l: 178, c: 20) - mutation from None to True