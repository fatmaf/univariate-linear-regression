#Harish's code
import sys
import numpy as np
import matplotlib.pyplot as plt

#data = [ [-10,91], [-3,7], [0,1], [1,3], [2,7], [3,13], [4,21], [10,111] ]
data = [ [-100,9901],[-10,91], [-3,7], [0,1], [1,3], [2,7], [3,13], [4,21], [10,111] ,[100,10101] ]

## xa contains all the values of x in a list, ya of y.
xa    = [ i[0] for i in data ]
ya    = [ i[1] for i in data ]

## For graphs - ignore.
x = np.linspace( min( xa ), max( xa ) )


w0 = 0
w1 = 0
w2 = 0 
alpha  = 0.000001

epochs =1 #1000
for i in range( epochs ):

    ## Plot the current fit.
    plt.clf()
    plt.scatter(xa, ya)
    plt.plot( x, w2*x*x + w1*x + w0 )
    plt.ion()
    plt.show()
    plt.pause(0.001)
    ## End of plot
        
    cost = 0
    for index in range( len( xa ) ) :
        
        y_this = (w2 * xa[ index ] * xa[ index ]) + (w1 * xa[ index ]) + w0

        cost    += ( ya[ index ] - y_this ) ** 2

        w2      += alpha * ( ya[ index ] - y_this ) * xa[index] * xa[index] 
        w1      += alpha * ( ya[ index ] - y_this ) * xa[index]
        w0      += alpha * ( ya[ index ] - y_this )
        
        print( "Cost, w0, w1, w2: ", cost, w0, w1, w2 )
        
    print( "Cost, w0, w1, w2: ", (float(cost)/len(xa)), w0, w1, w2 )    

sys.exit()
