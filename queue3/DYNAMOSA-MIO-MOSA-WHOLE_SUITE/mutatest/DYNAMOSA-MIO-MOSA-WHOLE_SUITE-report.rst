Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 44
 - Location sample coverage: 22.73 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.439025
 - Clean trial 2 run time: 0:00:00.280345
 - Mutation trials total run time: 0:00:07.276549

Overall mutation trial summary
==============================
 - DETECTED: 13
 - SURVIVED: 9
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-06 08:11:23.235619


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 11, c: 20) - mutation from None to False
 - queue3.py: (l: 11, c: 20) - mutation from None to True
 - queue3.py: (l: 21, c: 37) - mutation from None to False
 - queue3.py: (l: 21, c: 37) - mutation from None to True
 - queue3.py: (l: 62, c: 19) - mutation from None to True
 - queue3.py: (l: 62, c: 19) - mutation from None to False
 - queue3.py: (l: 88, c: 35) - mutation from None to False
 - queue3.py: (l: 113, c: 19) - mutation from None to True
 - queue3.py: (l: 113, c: 19) - mutation from None to False


DETECTED
--------
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 66, c: 32) - mutation from None to False
 - queue3.py: (l: 66, c: 32) - mutation from None to True
 - queue3.py: (l: 75, c: 32) - mutation from None to True
 - queue3.py: (l: 75, c: 32) - mutation from None to False
 - queue3.py: (l: 88, c: 35) - mutation from None to True
 - queue3.py: (l: 112, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 112, c: 8) - mutation from If_Statement to If_True