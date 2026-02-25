#!/usr/bin/env python3
#Helena Berens 

from collections import defaultdict, Counter

# ciphertext given 
C = "TTEUM GQNDV EOIOL EDIRE MQTGS DAFDR CDYOX IZGZP PTAAI TUCSI XFBXY SUNFE SQRHI SAFHR TQRVS VQNBE EEAQG IBHDV SNARI DANSL EXESX EDSNJ AWEXA ODDHX EYPKS YEAES RYOET OXYZP PTAAI TUCRY BETHX UFINR"
C = "".join(C.split(" "))
l = len(C)

# function to get index of coincidence 
def IC(x):
  freq = dict(Counter(x))
  #print(freq)
  N = len(x)
  summation = 0
  IoC = 0

  # calculate for each letter - get frequencies an apply formula 
  for i in range(26):
    mult = freq.get(chr(i+65),0) * (freq.get(chr(i+65),0)-1)
    summation += mult

  IoC = summation/(N * (N - 1))
  return IoC

#print(IC(C)) # period of 2 

# test different period splits of the ciphertext into alphabets to find the max ICs
average_ICs = []
for i in range(1,26):
    split = [[] for _ in range(i)]

    for j in range(l):
        split[j%i].append(C[j])

    # calculate the IC for each alphabet and average them
    for k in range(i):
        split[k] = IC("".join(split[k]))

    average = sum(split) / len(split)
    print(f"IC average by splitting C into {i} alphabets: {average}")

    average_ICs.append((i, average))

sorted_ICS = sorted(average_ICs, key=lambda x: x[1])
#print(sorted_ICS[-6:])
  

# Gives us that periods of 5, 17, 18, 10, 20, 25 have high IC values 
# we will try 5 because that agrees with what we found from our repetition analysis

# Caesar Cipher on each alphabet split by period = 5

# table from class 
FREQUENCIES = [
  0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060, 0.065, 0.005, 
  0.005, 0.035, 0.030, 0.070, 0.080, 0.020, 0.002, 0.065, 0.060, 0.090, 
  0.030, 0.010, 0.015, 0.005, 0.020, 0.002
]

# split into 5 alphabets 
period = 5
split = [[] for _ in range(period)]
for j in range(l):
  split[j%period].append(C[j])

keyword = []
# for each alphabet, calculate the frequency of each letter
for c in range(5):
    f = [0]*26
    for s in split[c]:
        f[ord(s) - 65] += 1

    #calculate phi values for each possible i shift
    correlations = []
    for i in range(26):
        phi = 0
        for j in range(26):
            # phi formula 
            phi += (f[j%26]/ l) * FREQUENCIES[(j-i)%26]
        correlations.append((phi, i))
    
    #print(f"\nCorrelations for alphabet {c}: {correlations}")

    # sort them to find the most likely shifts
    correlations.sort()
    print()
    print(f"Best correlation for alphabet {c}:")
    best_i = correlations[-1:][0]
    print(f'phi = {best_i[0]}, shift = {best_i[1]}')

    # append to keyword to get the full word 
    keyword += (chr(best_i[1] + 65))

keyword = "".join(keyword)
print(f'key found = {keyword}')

# decryption function that shifts each letter back by the corresponding letter in the key
def decrypt(message, key):
  n = len(message)
  decrypted = []

  # for loop going through all letters in the ciphertext 
  for i in range(n):
    decrypted.append(chr((ord(message[i])-ord(key[i%5]))%26+65)) #shift modulo the key, then convert back to a letter
  return "".join(decrypted)


decrypted_string = decrypt(C, keyword)
print("Our decrypted string is: ", decrypted_string)

'''
Decrypted Text: THEVIGENERECIPHERISAMETHODOFENCRYPTINGALPHABETICTEXTBYUSINGASERIESOFINTERWOVENCAESARCIPHERSBASEDONTHELETTERSOFAKEYWORDITEMPLOYSAFORMOFPOLYALPHABETICSUBSTITUTION
'''


  