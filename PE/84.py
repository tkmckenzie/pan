import numpy as np
import scipy.stats as sps

num_sides = 4 #Number of sides on the dice

possible_rolls = list(range(2, num_sides * 2 + 1))
frequency = list(range(1, num_sides + 1))
frequency += frequency[-2::-1]
pmf = {possible_rolls[i]: frequency[i] / (num_sides**2) for i in range(len(possible_rolls))}

double_prob = 1 / (num_sides)
jail_roll_prob = double_prob**3
jail_roll_prob_comp = 1 - jail_roll_prob

pos_dict = {0: 'GO', 1: 'A1', 2: 'CC1', 3: 'A2', 4: 'T1',
            5: 'R1', 6: 'B1', 7: 'CH1', 8: 'B2', 9: 'B3',
            10: 'JAIL', 11: 'C1', 12: 'U1', 13: 'C2', 14: 'C3',
            15: 'R2', 16: 'D1', 17: 'CC2', 18: 'D2', 19: 'D3',
            20: 'FP', 21: 'E1', 22: 'CH2', 23: 'E2', 24: 'E3',
            25: 'R3', 26: 'F1', 27: 'F2', 28: 'U2', 29: 'F3',
            30: 'G2J', 31: 'G1', 32: 'G2', 33: 'CC3', 34: 'G3',
            35: 'R4', 36: 'CH3', 37: 'H1', 38: 'T2', 39: 'H2'}
id_dict = {value: key for (key, value) in pos_dict.items()}

num_spaces = len(pos_dict)

r_pos = sorted([id_dict[key] for key in id_dict.keys() if 'R' in key])
u_pos = sorted([id_dict[key] for key in id_dict.keys() if 'U' in key])
cc_pos = sorted([id_dict[key] for key in id_dict.keys() if 'CC' in key])
ch_pos = sorted([id_dict[key] for key in id_dict.keys() if 'CH' in key])
g2j_pos = id_dict['G2J']

num_r = len(r_pos)
num_u = len(u_pos)

#Construct transition probabilities after landing on CC or CH
def CC(pos):
    if not pos in cc_pos: raise ValueError('pos is not a CC square.')
    row = np.zeros(num_spaces)
    row[id_dict['GO']] += 1 / 16
    row[id_dict['JAIL']] += 1 / 16
    row[pos] += 7 / 8
    
    if not sum(row) == 1: raise ValueError('CC row does not sum to one.')
    
    return row
def CH(pos):
    if not pos in ch_pos: raise ValueError('pos is not a CH square.')
    row = np.zeros(num_spaces)
    
    next_r = r_pos[np.searchsorted(r_pos, pos) % num_r]
    next_u = u_pos[np.searchsorted(u_pos, pos) % num_u]
    
    row[id_dict['GO']] += 1 / 16
    row[id_dict['JAIL']] += 1 / 16
    row[id_dict['C1']] += 1 / 16
    row[id_dict['E3']] += 1 / 16
    row[id_dict['H2']] += 1 / 16
    row[id_dict['R1']] += 1 / 16
    row[next_r] += 1 / 8
    row[next_u] += 1 / 16
    row[pos - 3] += 1 / 16
    row[pos] += 3 / 8
    
    if not sum(row) == 1: raise ValueError('CH row does not sum to one.')
    
    return row

#Construct transition matrix
T = np.zeros((num_spaces, num_spaces))
for pos in range(num_spaces):
    row = np.zeros(num_spaces)
    
    for roll in pmf.keys():
        space = (pos + roll) % num_spaces
        base_prob = pmf[roll]
        
        if space == g2j_pos:
            row[id_dict['JAIL']] += base_prob
        elif space in cc_pos:
            row += base_prob * CC(space)
        elif space in ch_pos:
            row += base_prob * CH(space)
        else:
            row[space] += base_prob
    
    row *= jail_roll_prob_comp
    row[id_dict['JAIL']] += jail_roll_prob
    
    T[pos,:] = row


#T = np.matrix([[0.9, 0.075, 0.025],
#               [0.15, 0.8, 0.05],
#               [0.25, 0.25, 0.5]])
#T = np.linalg.matrix_power(T, 3)
#x = np.matrix([[0, 1, 0]])
#
#np.matmul(x, T)

#Steady state
#tol = 1e-8
#eigvals = np.linalg.eigvals(T.transpose())
#unit_index = np.where(np.abs(eigvals - 1) < tol)[0]
#
#if len(unit_index) > 1: raise ValueError('More than one unit eigenvalue found.')
#
#unit_index = unit_index[0]
#eigvec = np.linalg.eig(T.transpose())

T_inf = np.linalg.matrix_power(T, 100000)
init = np.ones(num_spaces) / num_spaces
#init = np.zeros(num_spaces)
#init[id_dict['GO']] = 1

steady_state = np.matmul(init, T_inf)
#print(list(zip(id_dict.keys(), steady_state)))

rankings = sps.rankdata(-steady_state)
top_ranked = [(pos_dict[np.where(rankings == i)[0][0]], steady_state[np.where(rankings == i)[0][0]]) for i in range(1, 6)]
print(top_ranked)

print([id_dict[top_ranked[i][0]] for i in range(3)])
