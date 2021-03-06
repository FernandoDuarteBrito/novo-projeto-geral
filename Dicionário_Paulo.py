# (ok) {'SBase': 1.0,
# (ok)(setado)  'Buses': ['A', 'B', 'C', 'D', 'E', 'NEWSOURCE'],
# (ok)  'PriBuses': ['A', 'B', 'C', 'D', 'E', 'NEWSOURCE'],
# (inativo)  'BusDist': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'NEWSOURCE': 0},
# (ok)(setado)  'Branches': {('D', 'B'), ('B', 'A'), ('C', 'B'), ('A', 'NEWSOURCE'), ('B', 'C'), ('NEWSOURCE', 'A'), ('D', 'E'), ('B', 'D'), ('A', 'B'), ('E', 'D')},
# (ok)(setado)  'Phases': ['a', 'b', 'c'],
# (ok)  'BranchPhase': {('B', 'D', 'c'), ('C', 'B', 'b'), ('A', 'B', 'b'), ('A', 'B', 'c'), ('A', 'NEWSOURCE', 'c'), ('B', 'A', 'a'), ('A', 'NEWSOURCE', 'b'), ('A', 'NEWSOURCE', 'a'), ('E', 'D', 'b'), ('C', 'B', 'c'), ('B', 'D', 'b'), ('B', 'A', 'c'), ('NEWSOURCE', 'A', 'a'), ('A', 'B', 'a'), ('B', 'C', 'c'), ('B', 'C', 'a'), ('NEWSOURCE', 'A', 'c'), ('D', 'B', 'c'), ('D', 'E', 'b'), ('C', 'B', 'a'), ('B', 'C', 'b'), ('D', 'B', 'b'), ('NEWSOURCE', 'A', 'b'), ('B', 'A', 'b')},
# (ok)(setado)  'BusPhase': [('A', 'a'), ('A', 'b'), ('A', 'c'), ('B', 'a'), ('B', 'b'), ('B', 'c'), ('C', 'a'), ('C', 'b'), ('C', 'c'), ('D', 'b'), ('D', 'c'), ('E', 'b'), ('NEWSOURCE', 'a'), ('NEWSOURCE', 'b'), ('NEWSOURCE', 'c')],
# (ok)  'SourceBus': ['NEWSOURCE'],
# (ok)  'DSSSourceBus': ['A'],
# (ok)(setado)  'CapBus': [],
# (ok)(setado)  'PVBus': ['C'],
# (ok)  'CapBusCont': [],
# (ok)(setado)  'RegBranch': [],
# (ok)(setado)  'RegGanged': [],
# (ok)(parametrizado)  'G': {(('A', 'a'), ('B', 'a')): -3.153153153153154,
#  (('A', 'b'), ('B', 'b')): -3.153153153153154,
#  (('A', 'c'), ('B', 'c')): -3.153153153153154,
#  (('B', 'a'), ('A', 'a')): -3.1531531531531525,
#  (('B', 'a'), ('C', 'a')): -14.20875677573627,
#  (('B', 'a'), ('C', 'b')): 4.4738547717942385,
#  (('B', 'a'), ('C', 'c')): 4.473854771794237,
#  (('B', 'b'), ('A', 'b')): -3.1531531531531525,
#  (('B', 'b'), ('C', 'a')): 4.4738547717942385,
#  (('B', 'b'), ('C', 'b')): -14.20875677573627,
#  (('B', 'b'), ('C', 'c')): 4.473854771794236,
#  (('B', 'b'), ('D', 'b')): -6.401281244199422,
#  (('B', 'b'), ('D', 'c')): 2.9400245295658323,
#  (('B', 'c'), ('A', 'c')): -3.1531531531531525,
#  (('B', 'c'), ('C', 'a')): 4.473854771794237,
#  (('B', 'c'), ('C', 'b')): 4.473854771794236,
#  (('B', 'c'), ('C', 'c')): -14.20875677573627,
#  (('B', 'c'), ('D', 'b')): 2.9400245295658323,
#  (('B', 'c'), ('D', 'c')): -6.401281244199422,
#  (('C', 'a'), ('B', 'a')): -14.20875677573627,
#  (('C', 'a'), ('B', 'b')): 4.4738547717942385,
#  (('C', 'a'), ('B', 'c')): 4.473854771794237,
#  (('C', 'b'), ('B', 'a')): 4.4738547717942385,
#  (('C', 'b'), ('B', 'b')): -14.20875677573627,
#  (('C', 'b'), ('B', 'c')): 4.473854771794236,
#  (('C', 'c'), ('B', 'a')): 4.473854771794237,
#  (('C', 'c'), ('B', 'b')): 4.473854771794236,
#  (('C', 'c'), ('B', 'c')): -14.20875677573627
#  , (('D', 'b'), ('B', 'b')): -6.401281244199422,
#  (('D', 'b'), ('B', 'c')): 2.9400245295658323,
#  (('D', 'b'), ('E', 'b')): -6.922513429267178,
#  (('D', 'c'), ('B', 'b')): 2.9400245295658323,
#  (('D', 'c'), ('B', 'c')): -6.401281244199422,
#  (('E', 'b'), ('D', 'b')): -6.922513429267178,
#  (('NEWSOURCE', 'a'), ('A', 'a')): -189.60959830294485,
#  (('A', 'a'), ('NEWSOURCE', 'a')): -189.60959830294485,
#  (('NEWSOURCE', 'a'), ('A', 'b')): -27.91918161205617,
#  (('A', 'b'), ('NEWSOURCE', 'a')): -27.91918161205617,
#  (('NEWSOURCE', 'a'), ('A', 'c')): -27.91918161205617,
#  (('A', 'c'), ('NEWSOURCE', 'a')): -27.91918161205617,
#  (('NEWSOURCE', 'b'), ('A', 'a')): -27.91918161205617,
#  (('A', 'a'), ('NEWSOURCE', 'b')): -27.91918161205617,
#  (('NEWSOURCE', 'b'), ('A', 'b')): -189.60959830294485,
#  (('A', 'b'), ('NEWSOURCE', 'b')): -189.60959830294485,
#  (('NEWSOURCE', 'b'), ('A', 'c')): -27.91918161205617,
#  (('A', 'c'), ('NEWSOURCE', 'b')): -27.91918161205617,
#  (('NEWSOURCE', 'c'), ('A', 'a')): -27.91918161205617,
#  (('A', 'a'), ('NEWSOURCE', 'c')): -27.91918161205617,
#  (('NEWSOURCE', 'c'), ('A', 'b')): -27.91918161205617,
#  (('A', 'b'), ('NEWSOURCE', 'c')): -27.91918161205617,
#  (('NEWSOURCE', 'c'), ('A', 'c')): -189.60959830294485,
#  (('A', 'c'), ('NEWSOURCE', 'c')): -189.60959830294485},
# (ok)(parametrizado)  'B': {(('A', 'a'), ('B', 'a')): 2.252252418918919,
#  (('A', 'b'), ('B', 'b')): 2.252252418918919,
#  (('A', 'c'), ('B', 'c')): 2.252252418918919,
#  (('B', 'a'), ('A', 'a')): 2.2522524189189186,
#  (('B', 'a'), ('C', 'a')): 29.87618958946942,
#  (('B', 'a'), ('C', 'b')): -8.97075786970609,
#  (('B', 'a'), ('C', 'c')): -8.970757869706086,
#  (('B', 'b'), ('A', 'b')): 2.2522524189189186,
#  (('B', 'b'), ('C', 'a')): -8.97075786970609,
#  (('B', 'b'), ('C', 'b')): 29.87618958946942,
#  (('B', 'b'), ('C', 'c')): -8.970757869706086,
#  (('B', 'b'), ('D', 'b')): 13.59188241036914,
#  (('B', 'b'), ('D', 'c')): -5.831591319218615,
#  (('B', 'c'), ('A', 'c')): 2.2522524189189186,
#  (('B', 'c'), ('C', 'a')): -8.970757869706086,
#  (('B', 'c'), ('C', 'b')): -8.970757869706086,
#  (('B', 'c'), ('C', 'c')): 29.876189589469412,
#  (('B', 'c'), ('D', 'b')): -5.831591319218615,
#  (('B', 'c'), ('D', 'c')): 13.59188241036914,
#  (('C', 'a'), ('B', 'a')): 29.87618958946942,
#  (('C', 'a'), ('B', 'b')): -8.97075786970609,
#  (('C', 'a'), ('B', 'c')): -8.970757869706086,
#  (('C', 'b'), ('B', 'a')): -8.97075786970609,
#  (('C', 'b'), ('B', 'b')): 29.87618958946942,
#  (('C', 'b'), ('B', 'c')): -8.970757869706086,
#  (('C', 'c'), ('B', 'a')): -8.970757869706086,
#  (('C', 'c'), ('B', 'b')): -8.970757869706086,
#  (('C', 'c'), ('B', 'c')): 29.876189589469412,
#  (('D', 'b'), ('B', 'b')): 13.59188241036914,
#  (('D', 'b'), ('B', 'c')): -5.831591319218615,
#  (('D', 'b'), ('E', 'b')): 15.52058218230105,
#  (('D', 'c'), ('B', 'b')): -5.831591319218615,
#  (('D', 'c'), ('B', 'c')): 13.59188241036914,
#  (('E', 'b'), ('D', 'b')): 15.52058218230105,
#  (('NEWSOURCE', 'a'), ('A', 'a')): 676.6224060360938,
#  (('A', 'a'), ('NEWSOURCE', 'a')): 676.6224060360938,
#  (('NEWSOURCE', 'a'), ('A', 'b')): 29.860739272538964,
#  (('A', 'b'), ('NEWSOURCE', 'a')): 29.860739272538964,
#  (('NEWSOURCE', 'a'), ('A', 'c')): 29.860739272538964,
#  (('A', 'c'), ('NEWSOURCE', 'a')): 29.860739272538964,
#  (('NEWSOURCE', 'b'), ('A', 'a')): 29.860739272538964,
#  (('A', 'a'), ('NEWSOURCE', 'b')): 29.860739272538964,
#  (('NEWSOURCE', 'b'), ('A', 'b')): 676.6224060360938,
#  (('A', 'b'), ('NEWSOURCE', 'b')): 676.6224060360938,
#  (('NEWSOURCE', 'b'), ('A', 'c')): 29.860739272538957,
#  (('A', 'c'), ('NEWSOURCE', 'b')): 29.860739272538957,
#  (('NEWSOURCE', 'c'), ('A', 'a')): 29.860739272538964,
#  (('A', 'a'), ('NEWSOURCE', 'c')): 29.860739272538964,
#  (('NEWSOURCE', 'c'), ('A', 'b')): 29.860739272538957,
#  (('A', 'b'), ('NEWSOURCE', 'c')): 29.860739272538957,
#  (('NEWSOURCE', 'c'), ('A', 'c')): 676.6224060360937,
#  (('A', 'c'), ('NEWSOURCE', 'c')): 676.6224060360937},
# (inativo)  'LSp': {'DEFAULT': [0.677, 0.6256, 0.6087, 0.5833, 0.58028, 0.6025, 0.657, 0.7477, 0.832, 0.88, 0.94, 0.989, 0.985, 0.98, 0.9898, 0.999, 1.0, 0.958, 0.936, 0.913, 0.876, 0.876, 0.828, 0.756],
# (inativo)  'NOLS': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
# (inativo)  'LSq': {'DEFAULT': [0.677, 0.6256, 0.6087, 0.5833, 0.58028, 0.6025, 0.657, 0.7477, 0.832, 0.88, 0.94, 0.989, 0.985, 0.98, 0.9898, 0.999, 1.0, 0.958, 0.936, 0.913, 0.876, 0.876, 0.828, 0.756],
# (inativo)  'NOLS': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},
# (ok)(parametrizado)  'Pload': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.04, ('B', 'b'): 0.04, ('B', 'c'): 0.04, ('C', 'a'): 0.04, ('C', 'b'): 0.04, ('C', 'c'): 0.04, ('D', 'b'): 0.06, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (ok)(parametrizado)  'Qload': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.013333333333333334, ('B', 'b'): 0.013333333333333334, ('B', 'c'): 0.013333333333333334, ('C', 'a'): 0.013333333333333334, ('C', 'b'): 0.013333333333333334, ('C', 'c'): 0.013333333333333334, ('D', 'b'): 0.01, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (inativo)  'LoadLS': {'A': 'NOLS', 'B': 'NOLS', 'C': 'NOLS', 'D': 'NOLS', 'E': 'NOLS', 'NEWSOURCE': 'NOLS'},
# (inativo)  'PloadZ': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'NEWSOURCE': 0.0},
# (inativo)  'PloadI': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'NEWSOURCE': 0.0},
# (inativo)  'PloadP': {'A': 0.0, 'B': 1.0, 'C': 1.0, 'D': 1.0, 'E': 0.0, 'NEWSOURCE': 0.0},
# (inativo)  'QloadZ': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'NEWSOURCE': 0.0},
# (inativo)  'QloadI': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'NEWSOURCE': 0.0},
# (inativo)  'QloadP': {'A': 0.0, 'B': 1.0, 'C': 1.0, 'D': 1.0, 'E': 0.0, 'NEWSOURCE': 0.0},
# (ok)(parametrizado)  'Pgen': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.0, ('B', 'b'): 0.0, ('B', 'c'): 0.0, ('C', 'a'): 0.0, ('C', 'b'): 0.0, ('C', 'c'): 0.0, ('D', 'b'): 0.0, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (ok)(parametrizado)  'Qgen': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.0, ('B', 'b'): 0.0, ('B', 'c'): 0.0, ('C', 'a'): 0.0, ('C', 'b'): 0.0, ('C', 'c'): 0.0, ('D', 'b'): 0.0, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (ok)(parametrizado)  'Qcap': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.0, ('B', 'b'): 0.0, ('B', 'c'): 0.0, ('C', 'a'): 0.0, ('C', 'b'): 0.0, ('C', 'c'): 0.0, ('D', 'b'): 0.0, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (ok)(parametrizado)  'Ppv': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.0, ('B', 'b'): 0.0, ('B', 'c'): 0.0, ('C', 'a'): 0.06666666666666667, ('C', 'b'): 0.06666666666666667, ('C', 'c'): 0.06666666666666667, ('D', 'b'): 0.0, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (ok)(parametrizado)  'Qpv': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.0, ('B', 'b'): 0.0, ('B', 'c'): 0.0, ('C', 'a'): 0.0, ('C', 'b'): 0.0, ('C', 'c'): 0.0, ('D', 'b'): 0.0, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (inativo)  'PVLS': {'A': 'NOLS', 'B': 'NOLS', 'C': 'NOLS', 'D': 'NOLS', 'E': 'NOLS', 'NEWSOURCE': 'NOLS'}, 'Pinjinit': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): -0.04, ('B', 'b'): -0.04, ('B', 'c'): -0.04, ('C', 'a'): 0.026666666666666665, ('C', 'b'): 0.026666666666666665, ('C', 'c'): 0.026666666666666665, ('D', 'b'): -0.06, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (??)  'Qinjinit': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): -0.013333333333333334, ('B', 'b'): -0.013333333333333334, ('B', 'c'): -0.013333333333333334, ('C', 'a'): -0.013333333333333334, ('C', 'b'): -0.013333333333333334, ('C', 'c'): -0.013333333333333334, ('D', 'b'): -0.01, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (??)(Vari??vel)  'Vminit': {('A', 'a'): 0.9999603397044746, ('A', 'b'): 0.9999174082525754, ('A', 'c'): 0.999951813427195, ('B', 'a'): 0.9931029016301428, ('B', 'b'): 0.9784826321964685, ('B', 'c'): 0.9930958794110943, ('C', 'a'): 0.9930974464523464, ('C', 'b'): 0.9784748316827919, ('C', 'c'): 0.9930762850047355, ('D', 'b'): 0.9756178665321784, ('D', 'c'): 0.995316107763967, ('E', 'b'): 0.975618368210616, ('NEWSOURCE', 'a'): 1.0, ('NEWSOURCE', 'b'): 1.0, ('NEWSOURCE', 'c'): 1.0},
# (??)  'Vainit': {('A', 'a'): -1.2382964434195546e-05, ('A', 'b'): -2.094485421247861, ('A', 'c'): 2.094382670715315, ('B', 'a'): 0.003613814242716233, ('B', 'b'): -2.0978210120600145, ('B', 'c'): 2.098005892266548, ('C', 'a'): 0.004307994165041325, ('C', 'b'): -2.097090422200299, ('C', 'c'): 2.0987058591925014, ('D', 'b'): -2.1021567756162227, ('D', 'c'): 2.097886431962292, ('E', 'b'): -2.102157004967684, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): -2.0943951023931953, ('NEWSOURCE', 'c'): 2.0943951023931953},
# (??)  'Capinit': {},
# (??)  'Tapinit': {},
# (ok)(parametrizado)  'BranchIRat': {('D', 'B'): 0, ('B', 'A'): 0, ('C', 'B'): 0, ('A', 'NEWSOURCE'): 0, ('B', 'C'): 0.9607108479315374, ('NEWSOURCE', 'A'): 0, ('D', 'E'): 0.9607108479315374, ('B', 'D'): 0.9607108479315374, ('A', 'B'): 0, ('E', 'D'): 0},
# (ok)  'BranchSRat': {('D', 'B'): 0, ('B', 'A'): 0, ('C', 'B'): 0, ('A', 'NEWSOURCE'): 0, ('B', 'C'): 0, ('NEWSOURCE', 'A'): 0, ('D', 'E'): 0, ('B', 'D'): 0, ('A', 'B'): 1.0, ('E', 'D'): 0},
# (ok)  'PVSrat': {'C': 0.22},
# (ok)  'PVPlimit': {'C': 0.2},
# (inativo)  'Transmission Cost P': 10,
# (inativo)  'Transmission Cost Q': 0,
# (inativo)  'Gen Costs P': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.0, ('B', 'b'): 0.0, ('B', 'c'): 0.0, ('C', 'a'): 10, ('C', 'b'): 10, ('C', 'c'): 10, ('D', 'b'): 0.0, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0},
# (inativo)  'Gen Costs Q': {('A', 'a'): 0.0, ('A', 'b'): 0.0, ('A', 'c'): 0.0, ('B', 'a'): 0.0, ('B', 'b'): 0.0, ('B', 'c'): 0.0, ('C', 'a'): 0, ('C', 'b'): 0, ('C', 'c'): 0, ('D', 'b'): 0.0, ('D', 'c'): 0.0, ('E', 'b'): 0.0, ('NEWSOURCE', 'a'): 0.0, ('NEWSOURCE', 'b'): 0.0, ('NEWSOURCE', 'c'): 0.0}}