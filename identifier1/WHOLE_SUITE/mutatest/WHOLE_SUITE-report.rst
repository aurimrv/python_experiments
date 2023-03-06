Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/identifier1/identifier1.py
 - Test commands: ['python', '-m', 'pytest', './WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 39
 - Location sample coverage: 25.64 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.910181
 - Clean trial 2 run time: 0:00:01.022061
 - Mutation trials total run time: 0:00:28.576592

Overall mutation trial summary
==============================
 - DETECTED: 17
 - TIMEOUT: 1
 - SURVIVED: 5
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-05 01:50:10.566907


Mutations by result status
==========================


SURVIVED
--------
 - identifier1.py: (l: 14, c: 8) - mutation from If_Statement to If_True
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 78) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>


TIMEOUT
-------
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - identifier1.py: (l: 7, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - identifier1.py: (l: 7, c: 45) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 8, c: 19) - mutation from True to None
 - identifier1.py: (l: 8, c: 19) - mutation from True to False
 - identifier1.py: (l: 14, c: 8) - mutation from If_Statement to If_False
 - identifier1.py: (l: 14, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Div
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Sub
 - identifier1.py: (l: 35, c: 23) - mutation from True to None
 - identifier1.py: (l: 35, c: 23) - mutation from True to False