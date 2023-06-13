# pip install numpy
import numpy as np
from collections import Counter
n = np.random.randint(1,50000)
major_element = np.random.randint(-1*10**9, 10**9)
sequence_2 = np.random.randint(-1*10**9, 10**9, n-n // 2-1) 
sequence_1 = np.full(n//2+1,major_element)
test_case = np.concatenate([sequence_1,sequence_2])
np.random.shuffle(test_case)
print("major element =",major_element)
print("result = ",Counter(test_case).most_common()[0][0] )
print("n=",n)
print("test case length =",len(test_case))
