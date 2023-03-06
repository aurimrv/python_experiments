Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/identifier1/identifier1.py
 - Test commands: ['python', '-m', 'pytest', './MIO']
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
 - Clean trial 1 run time: 0:00:01.037880
 - Clean trial 2 run time: 0:00:00.948870
 - Mutation trials total run time: 0:00:37.516336

Overall mutation trial summary
==============================
 - DETECTED: 23
 - SURVIVED: 6
 - TIMEOUT: 1
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-05 01:24:37.765709


Mutations by result status
==========================


SURVIVED
--------
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 17, c: 19) - mutation from False to None
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 31, c: 20) - mutation from If_Statement to If_True
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>


TIMEOUT
-------
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - identifier1.py: (l: 7, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - identifier1.py: (l: 14, c: 45) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 17, c: 19) - mutation from False to True
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 31, c: 20) - mutation from If_Statement to If_False
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Sub
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 35, c: 23) - mutation from True to None
 - identifier1.py: (l: 35, c: 23) - mutation from True to False