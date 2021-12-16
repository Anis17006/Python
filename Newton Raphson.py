import math
def nraphson(fn, x, tol=0.0001, maxiter=1000):
	for i in range(100):
		xnew = x - fn[0](x)/fn[1](x)
		if abs(xnew-x)< 0.001:
			break
		x=xnew
	return xnew, i	
y=[lambda x:x**1.5+0.5*x-6, lambda x:1.5*x**0.5+0.5]
x,n=nraphson(y,3)
print("The root is %f at %d iteration" %(x,n))