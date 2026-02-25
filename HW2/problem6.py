#!/usr/bin/env python3
#Helena Berens 

# given 
CIPHERTEXT = "1100101011101101101000100110010101011111101101110011100001110011"
KEY        = "0100110001001111010101100100010101000011010100110100111001000100"

# all the tables we need from the reading 
pc1_table = [
  57, 49, 41, 33, 25, 17, 9,
   1, 58, 50, 42, 34, 26, 18,
  10,  2, 59, 51, 43, 35, 27,
  19, 11,  3, 60, 52, 44, 36,
  63, 55, 47, 39, 31, 23, 15,
   7, 62, 54, 46, 38, 30, 22,
  14,  6, 61, 53, 45, 37, 29,
  21, 13,  5, 28, 20, 12,  4
]
pc2_table = [
  14, 17, 11, 24,  1,  5,  
  3,  28, 15,  6, 21, 10, 
  23, 19, 12,  4, 26,  8, 
  16,  7, 27, 20, 13,  2,
  41, 52, 31, 37, 47, 55, 
  30, 40, 51, 45, 33, 48, 
  44, 49, 39, 56, 34, 53, 
  46, 42, 50, 36, 29, 32
]

ls_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

IP_TABLE = [
  58, 50, 42, 34, 26, 18, 10, 2,
  60, 52, 44, 36, 28, 20, 12, 4,
  62, 54, 46, 38, 30, 22, 14, 6,
  64, 56, 48, 40, 32, 24, 16, 8,
  57, 49, 41, 33, 25, 17, 9, 1,
  59, 51, 43, 35, 27, 19, 11, 3,
  61, 53, 45, 37, 29, 21, 13, 5,
  63, 55, 47, 39, 31, 23, 15, 7
] 
E_BIT_TABLE = [
  32, 1, 2, 3, 4, 5,
  4, 5, 6, 7, 8, 9,
  8, 9, 10, 11, 12, 13,
  12, 13, 14, 15, 16, 17,
  16, 17, 18, 19, 20, 21,
  20, 21, 22, 23, 24, 25,
  24, 25, 26, 27, 28, 29,
  28, 29, 30, 31, 32, 1
]
S_TABLE = [
    # S1 
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2 
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3 
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4 
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5 
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6 
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7 
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8 
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

P_TABLE = [
  16, 7, 20, 21,
  29, 12, 28, 17,
  1, 15, 23, 26,
  5, 18, 31, 10,
  2, 8, 24, 14,
  32, 27, 3, 9,
  19, 13, 30, 6,
  22, 11, 4, 25
]

IP_INVERSE_TABLE = [
  40, 8, 48, 16, 56, 24, 64, 32,
  39, 7, 47, 15, 55, 23, 63, 31,
  38, 6, 46, 14, 54, 22, 62, 30,
  37, 5, 45, 13, 53, 21, 61, 29,
  36, 4, 44, 12, 52, 20, 60, 28,
  35, 3, 43, 11, 51, 19, 59, 27,
  34, 2, 42, 10, 50, 18, 58, 26,
  33, 1, 41, 9, 49, 17, 57, 25
]

# generate 16 keys 
# take oriingal key, and permute it with the pc1 table 
KEY_P1 = []
for i in range(56): 
  bit_wanted = pc1_table[i]-1
  permuted_bit = KEY[bit_wanted]
  KEY_P1.append(permuted_bit)
KEY_P1 = "".join(KEY_P1)


# Initialize a dictionary to hold C, D, and K values for each round (1-16)
key_storage = {"C": [None] * 17, "D": [None] * 17, "K": [None] * 17}

# Divide the key into C and D at the 28th bit
key_storage["C"][0] = KEY_P1[:28]
key_storage["D"][0] = KEY_P1[28:]


# Function to perform left shift on C and D values
def left_shift(bits: str, shift_amount):
    return bits[shift_amount:] + bits[:shift_amount]

# do this 16 times for the 16 keys 
for i in range(16):
  # left shift both C and D using the ls_table
  key_storage["C"][i+1] = left_shift(key_storage["C"][i], ls_table[i])
  key_storage["D"][i+1] = left_shift(key_storage["D"][i], ls_table[i])

  # recombine both parts and then permute with the pc2 table to get the key 
  combined = key_storage["C"][i+1] + key_storage["D"][i+1]

  key_storage["K"][i+1] = ""
  # for each bit in the pc2 table, add the corresponding bit from the combined C and D to the key
  for t in range(48): 
    combined_bit_wanted = pc2_table[t]-1
    key_storage["K"][i+1] += combined[combined_bit_wanted]

  print(f"Key {i+1:02d}: {key_storage['K'][i+1]}\n")

def XOR(a, b):
  return format(int(a, 2) ^ int(b, 2), f'0{len(a)}b')


# Decrypt 

# permute by the IP_table 
dec = [] 
for i in range(64): 
    bit_wanted = IP_TABLE[i]-1
    permuted_bit = CIPHERTEXT[bit_wanted]
    dec.append(permuted_bit)
dec = "".join(dec)

# initialize L and R for each key and split string in half 
L = [None]*17
R = [None]*17
L[0] = dec[:32]
R[0] = dec[32:]


# get the first R
R[1] = ""
for i in range(48): 
   bit = R[0][E_BIT_TABLE[i]-1]
   R[1] += bit

# compute f(R, K) xor L for each round, and then swap L and R
for i in range(16):
  
  # E bit thing
  R_48 = "".join([R[i][E_BIT_TABLE[s]-1] for s in range(48)])
  # xor with the key 
  Rk = XOR(key_storage["K"][16-i], R_48)

  # split into 6 bits each to use the 8 tables 
  splits = []
  for j in range(0, 48, 6):
    # row- first and last bit 
    row_bits = Rk[j] + Rk[j+5]
    row = int(row_bits, 2)

    # column: middle 4 bits
    col_bits = Rk[j+1:j+5]
    col = int(col_bits, 2)

    # lookup in S-box
    value = S_TABLE[j // 6][row][col]

    splits.append(value)
  
  # convert back to binary and concatenate to get S 
  S = "".join(f"{s:04b}" for s in splits)

  # permuate with P table all 32 bits 
  P = "".join(S[P_TABLE[j]-1] for j in range(32))

  # take the output of f (P) can xor with L to get the next R
  R[i+1] = XOR(P, L[i])
  L[i+1] = R[i] # next L is previous R 
  
  print(f"f{i+1:02d}: {P}")
  print(f"L{i+1:02d}: {L[i+1]}")
  print(f"R{i+1:02d}: {R[i+1]}")

# combine the final 2 
IP = R[16] + L[16]

# use IP inverse table to permute one last time to get our final output 
temp = []
for i in range(64):
    index = IP_INVERSE_TABLE[i] - 1
    temp.append(IP[index])
decrypted = "".join(temp)
print(decrypted)

print("\nResult:", int(decrypted,2).to_bytes(8, byteorder="big").decode())