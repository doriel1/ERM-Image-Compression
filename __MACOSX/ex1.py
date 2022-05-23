import matplotlib.pyplot as plt
import numpy as np
import sys

image_fname,centroids_fname,out_fname=sys.argv[1],sys.argv[2],sys.argv[3]
z=np.loadtxt(centroids_fname)#arrey centroid

orig_pixels=plt.imread(image_fname)
pixels=orig_pixels.astype(float)/255
#reshape the image(128x128x3)into an Nx3 matrix where N = number of pixels
pixels=pixels.reshape(-1,3)
map={}
wasChanged=True
zBackup=z

for i in z:
    map[i]=[]

for pixel in pixels:
    comaprisonCent = []
    closestCentr=-1
    for centroid in z:
        x=np.power(np.linalg.norm(centroid,pixel))
        if closestCentr==-1 or x<closestCentr:
            closestCentr=x
    map[closestCentr].append(pixel)

for centroid in z:
    sum=0
    for i in map[centroid]:
        sum+=i
    avg=sum/len(map[i])





