#random number generation
#특정한 숫자가 나왔을 때 베르눌리 이벤트 카운트
#1000번 반복
#포아송 디스트리뷰서

import random
import math
import numpy as np
import matplotlib.pyplot as plt
ffile = open("C:/Users/admin/PoissonDistribution.txt", 'w')

#np.random.seed(seed=10)
array = [[0 for col in range(1000)] for row in range(1000)]
arrayForPoisson = np.zeros((1000,1000))


for repeat in range(1000):
    array[repeat] = np.random.normal(size=1000)

for printrepeat in range(2):
    print(array[printrepeat])
    printarray = str(array[printrepeat])
    ffile.write(printarray)
ffile.close

np.random.seed(seed=100)
randPois = np.random.poisson(lam = 5, size = 1000)

unique, counts = np.unique(randPois, return_counts=True)

np.asarray((unique, counts)).T

plt.bar(unique, counts, width=0.5, color="red", align ='center')

