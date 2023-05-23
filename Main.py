import csv
import random 
import math

with open("./coordinates.csv", 'r') as file:
    csvreader = list(csv.reader(file))
    x = 0.0
    y = 1
    for row in csvreader:
        x += (float(row[0]) - float(row[1])) ** 2
        y += 1
    print(x)
    print(y)
    cluster1 = random.randint(0, 10)
    cluster2 = random.randint(0, 10)
    while cluster1 == cluster2:
        cluster2 = random.randint(0, 10)
    print(csvreader[cluster1])
    print("Cluster A equals %f" % float((csvreader[cluster1])[0]) + ", %f" % float((csvreader[cluster1])[1]))
    print(csvreader[cluster2])
    print("Cluster B equals %f" % float((csvreader[cluster2])[0]) + ", %f" % float((csvreader[cluster2])[1]))
    
    cluster1 = [float((csvreader[cluster1])[0]), float((csvreader[cluster1])[1])]
    cluster2 = [float((csvreader[cluster2])[0]), float((csvreader[cluster2])[1])]
    change = True
    sumdistances1 = 0
    sumdistances2 = 0
    while change is True:
        numcluster1 = 0
        numcluster2 = 0
        sumx1 = 0
        sumy1 = 0
        sumx2 = 0
        sumy2 = 0
        sumdistancesinloop1 = 0
        sumdistancesinloop2 = 0
        sumsquareddistances1 = 0
        sumsquareddistances2 = 0
        for row in csvreader:
            p = [float((row)[0]), float((row)[1])]
            if math.dist(p, cluster1) < math.dist(p, cluster2):
                numcluster1 += 1
                sumdistancesinloop1 += math.dist(p, cluster1)
                sumsquareddistances1 += (math.dist(p, cluster1) ** 2)
                sumx1 += p[0]
                sumy1 += p[1]
            else:
                numcluster2 += 1
                sumdistancesinloop2 += math.dist(p, cluster2)
                sumsquareddistances2 += (math.dist(p, cluster2) ** 2)
                sumx2 += p[0]
                sumy2 += p[1]
        if (numcluster1 != 0):
            if (numcluster2 != 0):
                cluster1 = [sumx1/numcluster1, sumy1/numcluster1]
                cluster2 = [sumx2/numcluster2, sumy2/numcluster2]
        print(numcluster1)
        print('The squared summed distance for cluster 1 is %f' % sumsquareddistances1)
        print('Centroid one is %f' % cluster1[0] + ', %f' % cluster1[1]) 
        print('Centroid two is %f' % cluster2[0] + ', %f' % cluster2[1]) 
        print('The squared summed distance for cluster 2 is %f' % sumsquareddistances2)
        print(numcluster2)
        if(sumdistancesinloop1 == sumdistances1):
            change = False
        if(sumdistancesinloop2 == sumdistances2):
            change = False
        sumdistances1 = sumdistancesinloop1
        sumdistances2 = sumdistancesinloop2
    print('Centroid one is %f' % cluster1[0] + ', %f' % cluster1[1]) 
    print('Centroid two is %f' % cluster2[0] + ', %f' % cluster2[1]) 
    print('Sum of squared distances is %f' % (sumsquareddistances1 + sumsquareddistances2))
    
