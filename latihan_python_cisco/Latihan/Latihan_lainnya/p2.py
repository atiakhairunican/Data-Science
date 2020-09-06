# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 10

#netacad email cth: 'abcd@gmail.com'
email='atiakhairunican@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded

def isPointInCircle(x,y,r,center=(0,0)):
    # MULAI KODEMU DI SINI
    x0 = center[0]
    y0 = center[1]
    if (x-x0) ** 2 + (y-y0) ** 2 <= (r ** 2):
        return True
    else:
        return False
    

#Graded
import random

def generateRandomSquarePoints(n,length,center=(0,0)):
    # MULAI KODEMU DI SINI
    minx = center[0]-length/2
    miny = center[1]-length/2
  
    # Gunakan list comprehension dengan variable minx, miny, length, dan n
    points = [[random.uniform(minx,(minx+length)), random.uniform(miny,(miny+length))] for i in range(n)]
    return points


#Graded
import random

def MCCircleArea(r,n=100,center=(0,0)):
    # MULAI KODEMU DI SINI
    minx = center[0]-r
    miny = center[1]-r
    x0 = center[0]
    y0 = center[1]
    
    points = [[random.uniform(minx,(minx+(2*r))), random.uniform(miny,(miny+(2*r)))] for i in range(n)]
    count = 0
    
    for k in range(n):
        x = points[k][0]
        y = points[k][1]
        
        if (x-x0) ** 2 + (y-y0) ** 2 <= (r ** 2):
            count += 1
        
    lk = (count / n) * ((2*r) ** 2)
    return lk


#Graded
import random

def LLNPiMC(nsim,nsample):
    lk = 0
    for j in range(nsim):
        k = MCCircleArea(1,nsample)
        lk += k
        
    meanPi = lk / nsim
    return meanPi


# Graded

import math
est = LLNPiMC(10000,500)
act = math.pi

def relativeError(act,est):
    E = abs(((est - act) / act) * 100)
    return E