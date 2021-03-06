import numpy as np
import sys
from sklearn.cluster import mean_shift
from utility import revert

def __euc(p,c):
    sum = (p[0]-c[0])**2 + (p[1]-c[1])**2 + (p[2]-c[2])**2
    return np.sqrt(sum)

def kmeans(k, pixels):
    means = np.random.uniform(0,255,k*3).reshape([k, 3]) #cluster centers/ hardcoded for pixels
    membership = np.zeros(len(pixels))
    #changed = True
    #i = 0
    for i in range(0, 50): #iteration loop / set to membership change
    #while changed:
        #for each point, assign to nearest cluster
        #changed = False
        #print 'iter: ', i
        for j in range(0, len(pixels)): #each pixel
            mindex = -1
            min = sys.maxint
            #find closest mean
            for m in range(len(means)): #each mean
                dist = __euc(pixels[j],means[m])
                if dist < min:
                    #changed = True
                    min = dist
                    mindex = m
            membership[j] = mindex #pixel j is in mindex cluster

        #find new cluster centers
        for m in range(len(means)):
            tmp = np.zeros(3)
            count = 0.0
            for j in range(len(membership)):
                if membership[j] == m:
                    count += 1
                    tmp[0] += pixels[j][0]
                    tmp[1] += pixels[j][1]
                    tmp[2] += pixels[j][2]
            if count != 0: #if no members in cluster, pass
                means[m] = tmp / count

    out = []

    for i in range(len(membership)):
        out.append(means[int(membership[i])])
    return out

def winner_take_all(k, eps, pixels):
    means = np.random.uniform(0, 255, k * 3).reshape([k, 3])  # cluster centers/ hardcoded for pixels
    membership = np.zeros(len(pixels))

    for i in range(0, 50):  # iteration loop / set to membership change
        # for each point, assign to nearest cluster
        #print 'iter: ', i
        for j in range(0, len(pixels)):  # each pixel
            mindex = -1
            min = sys.maxint
            # find closest mean
            for m in range(len(means)):  # each mean
                dist = __euc(pixels[j], means[m])
                if dist < min:
                    min = dist
                    mindex = m
            membership[j] = mindex  # pixel j is in mindex cluster

            #update cluster center
            means[mindex][0] = means[mindex][0] + eps * (pixels[j][0] - means[mindex][0])
            means[mindex][1] = means[mindex][1] + eps * (pixels[j][1] - means[mindex][1])
            means[mindex][2] = means[mindex][2] + eps * (pixels[j][2] - means[mindex][2])

        # find new cluster centers
        for m in range(len(means)):
            tmp = np.zeros(3)
            count = 0.0
            for j in range(len(membership)):
                if membership[j] == m:
                    count += 1
                    tmp[0] += pixels[j][0]
                    tmp[1] += pixels[j][1]
                    tmp[2] += pixels[j][2]
            if count != 0:  # if no members in cluster, pass
                means[m] = tmp / count

    #final set
    out = []
    for j in range(0, len(pixels)):  # each pixel
        mindex = -1
        min = sys.maxint
        # find closest mean
        for m in range(len(means)):  # each mean
            dist = __euc(pixels[j], means[m])
            if dist < min:
                min = dist
                mindex = m
        membership[j] = mindex  # pixel j is in mindex cluster

    for i in range(len(membership)):
        out.append(means[int(membership[i])])
    return out

#not done
def kohonen_map():
    means = np.random.uniform(0,255,k*3).reshape([k, 3]) #cluster centers/ hardcoded for pixels
    membership = np.zeros(len(pixels))

    for i in range(0, 10): #iteration loop / set to membership change
        #for each point, assign to nearest cluster
        print 'iter: ', i
        for j in range(0, len(pixels)): #each pixel
            mindex = -1
            min = sys.maxint
            #find closest mean
            for m in range(len(means)): #each mean
                dist = __euc(pixels[j],means[m])
                if dist < min:
                    min = dist
                    mindex = m
            membership[j] = mindex #pixel j is in mindex cluster

        #find new cluster centers
        for m in range(len(means)):
            tmp = np.zeros(3)
            count = 0.0
            for j in range(len(membership)):
                if membership[j] == m:
                    count += 1
                    tmp[0] += pixels[j][0]
                    tmp[1] += pixels[j][1]
                    tmp[2] += pixels[j][2]
            if count != 0: #if no members in cluster, pass
                means[m] = tmp / count

    out = []

    for i in range(len(membership)):
        out.append(means[int(membership[i])])
    return out

def meanshift(bw, pixels):
    pixels = np.array(revert(pixels))
    c,ind = mean_shift(pixels, bandwidth=bw, n_jobs=-1)

    out = []
    for i in ind:
        out.append(c[i].astype(np.int))
        #print c[i].astype(np.int)
    return out
