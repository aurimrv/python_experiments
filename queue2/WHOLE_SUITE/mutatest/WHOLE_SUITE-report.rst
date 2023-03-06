Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 59
 - Location sample coverage: 16.95 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.303054
 - Clean trial 2 run time: 0:00:01.113504
 - Mutation trials total run time: 0:00:30.019654

Overall mutation trial summary
==============================
 - SURVIVED: 11
 - DETECTED: 14
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-05 01:53:55.966330


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 15, c: 35) - mutation from None to False
 - queue2.py: (l: 15, c: 35) - mutation from None to True
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 21, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 37, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 120, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 120, c: 24) - mutation from None to False
 - queue2.py: (l: 120, c: 24) - mutation from None to True


DETECTED
--------
 - queue2.py: (l: 16, c: 26) - mutation from None to True
 - queue2.py: (l: 16, c: 26) - mutation from None to False
 - queue2.py: (l: 37, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 90, c: 36) - mutation from None to True
 - queue2.py: (l: 90, c: 36) - mutation from None to False
 - queue2.py: (l: 91, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 120, c: 8) - mutation from If_Statement to If_True