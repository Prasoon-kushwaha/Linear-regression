import matplotlib.pyplot as plt
import numpy as np
# Linear regression
def mean(x):
    s = 0
    le = len(x)
    for A in range(le):
        s += x[A]
    return s / le

def variance(x):
    s = 0
    le = len(x)
    for A in range(le):
        s += (x[A])**2

    y=mean(x)
    return s/le-y**2

def covariance(x,y):
    s = 0
    le = len(x)
    for A in range(le):
        s += (x[A])*y[A]


    return s/le-mean(x)*mean(y)




X = (8, 2, 11, 6, 5, 2, 12, 9, 6, 1,)
Y = (4, 12, 2, 5, 8, 12, 1, 3, 5, 17)
# trying to find best slope from thr data we have using m= (x-xmn)(y-ymn)/(x-xmn)
mnX = mean(X)
mnY = mean(Y)

N = 0
D = 0
for a in range(len(X)):
    xm = X[a] - mnX
    D += xm ** 2
    N += xm * (Y[a] - mnY)
m = N / D
m = round(m, 3)
# now we have slope
# we'll now find Y intercept
c = mnY - m * mnX
# print("y=" + str(m) + "x +" + str(c))

#ERROR FUNCTION / COST FUNCTION / LOSS FUNCTION
#USING RMS

x1 = np.linspace(min(X), max(X), 100)
y1 = m * x1 + c
plt.plot(x1, y1,color="blue" ,label="Without using covariance")  # plotting line

x2 = np.linspace(min(X), max(X), 100)
y2 = covariance(X,Y)*(x2-mnX)/variance(X)+mnY
plt.plot(x2, y2,color='r',linestyle="dashed",label="Using covariance Y in term of X")  # Using covariance and variance plotting line

y3 = np.linspace(min(Y), max(Y), 100)
x3 = covariance(X,Y)*(y3-mnY)/variance(Y)+mnX
plt.plot(x3, y3,color='green',linestyle="dotted",label="Using covariance X in term of Y")  # Using covariance and variance plotting line

plt.scatter(X, Y, color="r")  # plotting dataset

plt.scatter(mnX, mnY, color="black",marker="s",label="mean x , mean y")  # plotting dataset
plt.title("LINE THAT BEST FITS [Linear Regression]")
plt.legend()
plt.show()

