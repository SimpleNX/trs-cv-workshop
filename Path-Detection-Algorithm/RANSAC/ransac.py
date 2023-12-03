import cv2 as cv
import numpy as np
import math

#The image frame
image = np.array((500,500,3), np.uint8)

cov = np.array([[1,500], [-500,500]])#Covariance
mean = np.array([250,250])#Mean

coordinate = []#It stores the coordinates of the white pixel.
inliers = []#The number of inliers for the random two points.
in_count = 0#Number of inliers for a given set of points
maxinliers = []#List of coordinates that are inliers for the data set with maximum inliers.
maxin_count = 0#The count of max inliers
threshold = 10#Threshold distance from the line to consider for inliers.


#Genearation of gaussian distribution similiarity between the points
#Generation of coordinates of x and y where all the points have gaussian distribution relation b/w them.
def gaussian_sampling(mean,cov):
    rand = np.random.multivariate_normal(mean,cov)
    rand = (int(rand[0])), (int(rand[1]))
    return rand

#For marking the points on the image
for i in range(100):
    rand = gaussian_sampling(mean,cov)
    if rand[0] in range(0,500) and rand[1] in range(0,500):
        coordinate.append(rand)
        image[rand[0],rand[1]] = 255
    cv.circle(image, rand, 1, (255,255,255),-1)

#Showing the image with all points marked in white
cv.imshow("Image",image)
if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()

#Finding perpendicular distance between the neighbouring points and the line formed between the current set of two points.
def disline (a, b, pt):
    num = abs((b[1]-a[1])*pt[0] + (a[0]-b[0])*pt[1] + b[0]*a[1] - b[1]*a[0])
    den = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    distance = num/den if distance !=0 else 0
    return distance

#Finding and counting the number of inliers for the current data set.
def inliers(a,b):
    in_count = 0
    inliers = [a, b]
    for pt in coordinate:
        dis = disline(a,b,pt)
        if dis == threshold:
            in_count += 1
            inliers.append(pt)
        else : 
            continue
    return in_count, inliers


#Finding the best fitting line for the set of points.
def least_squared_fit(x, y):
    N = len(x)
    sum_x = np.add(x)
    sum_x_sq = np.add(x*x)
    sum_y = np.add(y)
    sum_xy = np.add(np.multiply(x,y))
    m = (N*sum_xy - sum_x*sum_y)/(N*(sum_x_sq) - (sum_x**2))
    b = (sum_y - m*sum_x)/N
    return m, b

#Finding two random points for formation of line.
for i in range(set):
    #Coordinates of the random two points
    a_index = random.randint(len(coordinates))
    b_index = random.randint(len(coordinates))

    #The random two points
    a = coordinates[a_index]
    b = coordinates[b_index]

    count, inliers = inliers(a,b)

    if(count>maxin_count):
        maxin_count = count
        maxinliers = inliers

#Marking the inlier points with blue.
for point in maxinliers:
    cv.circle(image, point, 1, (255,0,0), -1)

#Making the best fit line for the given inliers.
m, b = least_squared_fit(maxinliers[0:][0:1], maxinliers[0:][1:2])




