import matplotlib.pyplot as plt
import numpy as np
import sys

from numpy import ndarray

image_fname,centroids_fname,out_fname=sys.argv[1],sys.argv[2],sys.argv[3]
z=np.loadtxt(centroids_fname)#arrey centroid
orig_pixels=plt.imread(image_fname)
pixels=orig_pixels.astype(float)/255
#reshape the image(128x128x3)into an Nx3 matrix where N = number of pixels
pixels=pixels.reshape(-1,3)

# # importing the required module
#
# import matplotlib.pyplot as plt
# def drowGraph(graphlist,iter):
#     x =[]
#     for i in range(iter):
#         x.append(i)
#     # corresponding y axis values
#     y = graphlist
#     # plotting the points
#     plt.plot(x, y)
#     # naming the x axis
#     plt.xlabel('itaration - axis')
#     # naming the y axis
#     plt.ylabel('loss - axis')
#     # giving a title to my graph
#     plt.title('')
#     # function to show the plot
#     plt.show()
#
# def loss(cents_map, cents):
#     dist_sum = 0
#     pixels_num = 0
#     for cent in cents_map:
#         for pixel in cents_map[cent]:
#             dist_sum += dist(pixel, cents[cent])
#         pixels_num += len(cents_map[cent])
#     return dist_sum / pixels_num
#
# def dist(pixel, cent):
#     return (pixel[0] - cent[0]) * 2 + (pixel[1] - cent[1]) * 2 + (pixel[2] - cent[2]) ** 2
#
# # graph_list=[]
fileName = open(out_fname,'w')
iteration=0
was_change=True
while iteration<20 and was_change==True:
    backup_z = z.copy()
    map={}
    #initialize map
    for i in range(len(z)):
        map[i]=[]
    #            step 1
    for pixel in pixels :
        closest_centroid=np.inf
        #find the closest pixel to centroid:
        for i in range(len(z)):
            x = np.linalg.norm(z[i] - pixel)
            if x < closest_centroid:
                closest_centroid = x
                closest_centroid_idx=i
            #append pixel to specified centroid
        map[closest_centroid_idx].append(pixel)
    #             step1

    #             step2
    #update centroids
    for key in map.keys():
        new_centroid=0
        for pixel in map[key]:
            new_centroid=new_centroid+pixel
        if len(map[key])!=0:
            new_centroid= new_centroid / len(map[key])
        z[key]=new_centroid.round(4)


    #check if was change
    if str(z)!=str(backup_z):
        was_change=True
    else:
        was_change=False
    #graph_list.append(loss(map,z))
    fileName.write(f"[iter {iteration}]:{','.join([str(i) for i in z.round(4)])}\n")
    iteration += 1
#drowGraph(graphlist=graph_list,iter=iteration)
fileName.close()



