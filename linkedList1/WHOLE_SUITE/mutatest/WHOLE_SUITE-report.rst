Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:01.529013
 - Clean trial 2 run time: 0:00:01.132958
 - Mutation trials total run time: 0:00:25.973443

Overall mutation trial summary
==============================
 - DETECTED: 10
 - SURVIVED: 8
 - ERROR: 1
 - TOTAL RUNS: 19
 - RUN DATETIME: 2023-03-05 01:50:41.285771


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 95, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 134, c: 12) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 134, c: 12) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>


DETECTED
--------
 - linkedList1.py: (l: 10, c: 20) - mutation from None to False
 - linkedList1.py: (l: 10, c: 20) - mutation from None to True
 - linkedList1.py: (l: 21, c: 11) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList1.py: (l: 65, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 95, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 113, c: 18) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList1.py: (l: 123, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 123, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_False


ERROR
-----
 - linkedList1.py: (l: 180, c: 0) - mutation from If_Statement to If_True