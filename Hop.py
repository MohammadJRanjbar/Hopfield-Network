"""
Created on Tue Nov 12 17:06:21 2019

@author: Mohammad
"""
import numpy as np
import cv2 
 
p1=np.array([[1,-1]
             ,[-1,-1]
             ,[1,-1]])
def sgn(number):
    res = np.sign(number)
    for i in range (res.shape[0]):
        if (res[i,0]==0):
            res[i,0]=-1
    return res        

def asynchornise (v1,v2):
    p = v1.copy()
    for  i in  range(v1.shape[0]):
        if(v1[i,0]!=v2[i,0]):
            p[i,0]=v2[i,0]
            return p
    return p
        
m=p1.shape[1]
W=np.dot(p1,np.transpose(p1))-m*np.eye(p1.shape[0])
v1=p1[:,1:2]
while(True):
    v2=sgn(np.dot(W,v1))
    v2=asynchornise(v1,v2)
    if(np.allclose(v2,v1)):
            break
    v1 = v2

print(p1)    
print(v2)

