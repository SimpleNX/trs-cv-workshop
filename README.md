# trs-cv-workshop
For CV Workshop

Day 1 :

Session 1:

    Command Line Interfaces :
        Listing all files in a directory : ls
        Making a directory : mkdir <mkdir> <dir_name>
        Accesing or moving into a directory : cd <dir_name>
        Absolute path :
            Adress from the root directory.
            Moving directly to root : cd/
            Remove directory : rmdir <dir_name> //The directory should be empty.
        Clear Terminal : clear

    File Hierarchy :
    /root is the parent directory

    Python :
        Open Basic > test.py

Session 2:

    NumPy:
        Usage of NumPy as a library for scientific calculations and higher dimensional matrices.
        For installation: pip install numpy
        Open Basic > npbase.py

Day 2:


Session 1:

    Digital Images:
        Images are collection of pixels and pixels are a point on the image which can have some properties.
        They are different types of images.
        Storing Digital Images : 8 bit color format and 16 bit color format.
        Different Color Channels : 
            BGR (0-255)
            HSV 
            CYMK
    OpenCV:
        Installation : pip install opencv-python
        Arithmetic Operations on image and bitwise operations on image
        Open cvproj > cvtry.py

Session 2:

    Using NumPy and OpenCV:
        NumPy to make digital images, by use of numpy arrays to create frames.
        Using the frame as the image to perform image functions from OpenCV
        Open CV to animate by constant frames.
        Open cvproj > npb.py
        Open cvproj > pacman.py
        Open cvproj > loading.py

Day 3:

Session 1:

    Image Smoothing:
        Filtering and Blurring:
        Digital Images are 3D array of integers representing pixels of the image with different integers representing different attributes of the image.
        Images are 3D array of BGR functions
        Filtering is a process that tranforms the pixels of the input image with respect to a function and outputs a filtered image with the funtion applied.
        Examples of Filters:
            1. Moving(weighted) Average: Sets the value of the current pixel as the average of its neighbouring pixel wich blurs/smooths out the sharper edges of the image.
                 Image Segmentation : This filter is used to segment the image by based on simple threshold image, by setting pixel regions with some high or low values to create bright and dark regions.
            2. Gaussian Filter:
                    The gaussian function is used to binarize the nearby points.
                    It's a bell shaped curve from -infinity to infinity
            
        Kernel:
            Kernel is a matrix of values that specifies the operation to be applied on each pixel of the image. Matrix of weights of the nearby pixels.
            Weighted.
            Filters can applied by using Kernel.
        Convolution:
            Convolution in Calculus Form.
            Another way of applying filters.
            Hospital Patient-Dose Treatment Analysis
            The filter kernel is flipped in this and then multiplied.
        Cross-Correlation:
            Same as Convolution but the filter kernel is not flipped.
            Can be used to find known features between two images.
        The images can be crisper and sharper, by smoothing we use weighted average and blur the image edges which reduces the noises in the image.
        It blurs the image.
        Open cvproj > smooth.py
        Open cvproj > Smoothing and Blur

        Edge Detection :
             We detect images by detecing the rapid change in image color intensity.
             Plotting the intensity function and then taking its derivative function.
             The usage of Lagrange's Identity:
                Backward, Forward, Central derivatives.
            This derivatives are convoluted kernels.
            We use the correlated kernels upon the function values.
            [a,b,c] [x+1,x,x-1] This is convoluted kernel which formed by flipping the above kernel horizontally.
        
        Gradient of an image is : (nabla)f
        The gradient vector points in the direction of change in maximun intensity

        Reducing Noise :
            Let f be the image and g be the smoohing kernel and calculate the smoothed gradient.
            d/dx(f*g) *means convolution
            =>f*(d/dx(g)) As the image f is constant.
        
        Sobel Noise Detector :
        =>Gx:[[1,0,-1],[2,0,-2],[1,0,-1]] #Central Derivatives, convoluted kernels
        =>Gy : (Gx)T
        Open cvproj > edgedetection.py
        

Session 2:

    Hough Transforms:
        It is used to detect what the set of points that make up the edge make
        It uses a specific parameter which matches the specific image dataset.
        In this, we pick all the points along the edge or required surface and plot it in the Hough Space.
        There can be multiple interesection points where points don't come in a line,
        we approximate the region with the most intersections by diving the axes into grids(regions) and voting for the region with the most intersections.
        The Algorithm for Hough Transform:
            Line :

            Circle :
                The parameters, x,y, centre coordinates, theta
                In 3D plane, we get a cone as if a point is taken on the circumference of the circle, with increasing radius it forms a cone with axis along the radius axis.
                If we find a point on the circumference and find the gradient at the point we restrict the centre of the original circle as the circle will stay on the normal at the point extended infinitely.
                And then again by voting we find the region of the centre.    
            Open cvproj > hough.py
            The above file contains the lane detection code.


Day 4:
Session 1:

    Template Detection:
        Matching the template with a target image.
        Open cvproj > template.py
        We detected the template in the image where the sqdiff is lowest and the ccorr is highest.
        For drawing the rectangle, we find the coordinates of the max and min values in the template and image matching region.

    Blob Detection :
        Similiar to template detection but here the blob and solid circles are detected using different functions.

Session 2:

    Image Contours:
        Contours are curves joining all points with same color, intensity, where all the points are continuous.(Along the boundary)
        These are done in binary image.
        Open cvproj > Contours
        Contour Heirarchy:
            The way shapes/objects are relatively stored with respect to each other.
            The way how contour image relate to each other.
        Matching contours :
            Similiar thing to matching for similiar images, by matching contours as they are curves joining points of similiar values.
        There are functions to find the features of the contour, area, perimeter etc.
        Also there is contour approximation.

        For gesture recogniton, look for mediapipe documentation
            https://github.com/google/mediapipe


Day 5:

Session 1:

    Path detection Algorithm:
        Detecting nodes to determine the shortest path or the available paths or the path problem required.

        Data Structures :
            Stacks :
                A basic data strcture which works with the LIFO method.
                Similiar to how you would access a stack of books.
                Push and Pop are common functions here.
                Basically one window for pushing and poppping data
            Queue :
                Works with FIFO method.
                Analogous to real life queues.
                Analogous to stack,
                    enqueue and dequeue are common functions here.
                Here there is one window for accessing data and one window for pushing data.
            Linked List :
                Discrete nodes linked to each other.
            Graphs :
                Look for Graph data structure Documentation
                Set of vertices or nodes are joined to form edges and formed an graph, sort of mapping an area by joining the nodes or vertices.
                They can also contain functions on the link or edge joining the vertices, by which the requirements of the problem can be met, or be checked.
                Trees :
                    Look for Tree Data Structure.
                Graphs are represented using :
                    Adjacency Matrix : A n*n matrix which contains 0 or 1 where 1 for a (i,j)
                    would mean that there exists a edge between ith and jth nodes.
                    Adjacency List: A list which has all the edges that a singular node has.
                    Basically all the edge connections a node has.

                Graph Traversal Methods:
                    Bread First Search:
                        We traverse from the root and move to its child and then to the child and then after them their child and so on.
                        Searching and moving generation-wise.
                        The search used by BFS is same as implementing the queue data structure.(FIFO)
                        Breadth-wise :
                            Checking data at the same breadth.
                            All of them store breadth wise in the queue.
                            The nodes with same distance from the root are checked first and then to the next set of nodes with increasing distance from the root.
                    Depth-First Search:
                        Here we start with one vertex and go to as much depth we can go from that vertex.
                        The one down of using this algorithm is that it can only explore nodes that be explored from the source node.
                        The above can be bypassed or solved by using a main loop that loops through all the nodes and consider them as the source node and then checks all the visited nodes and accessed nodes and then the algorithm proceeds with the search.
                        Its the implementation of stack data structure.
                        
                Open Path-Detection-Algorithm

             

                



        