import numpy as np 
import scipy as sc 
from sympy import *
import sys
sys.displayhook = pprint
init_printing()
print('\n\nInitial Setup Complete')





def batch_gradient_descent(c_f, f):	
	print "f(x) = ",c_f
	f_dash = diff(c_f,x)
	print "df(x)/dx = " , f_dash
	a = float(input("Enter initial approximation: "))
	x0=a
	n = float(input("Enter learning rate: "))
	err = float(input("Enter error tolerance : "))
	print "Starting Batch Gradient Descent"
	print "	x0 = ",a
	print "	f(x0) = ",f(a)
	iter_count = 0
	xk=x0
	while (True):
		iter_count = iter_count + 1
		#print "Iteration No. ", iter_count, ": "		
		fk_dash= (lambdify(x , f_dash , "numpy"))(xk)
		xk = xk - n*fk_dash
		#print "	x"+str(iter_count)+" = ",xk
		#print "	f(x"+str(iter_count)+") = ",f(xk)
		if abs(N(xk-x0)) < float(err):
			break
		x0 = xk
	print "Number of Iterations = ",iter_count
	print "	Minima is at = ",xk
	print "	Minimum value of Cost Function= ",f(xk)




#Syntax Constraints
print """		
	Syntax Constraints for entering function - 

	x**y means x raised to the power of y
	Function must be algebraic combination of one or more of - 

	p(x)      Polynomials
	exp(x)    Mathematical constant e (2.71828...) raised to power x
	pi        Mathematical constant 3.14159...
	log(x)    Natural Logarithm
	acos(x)   Arc cosine of x
	asin(x)   Arc sine of x
	atan(x)   Arc tangent of x
	cos(x)    Cosine of x
	sin(x)    Sine of x
	tan(x)    Tangent of x
	acosh(x)  Inverse hyperbolic cosine of x
	asinh(x)  Inverse hyperbolic sine of x
	atanh(x)  Inverse hyperbolic tangent of x
	cosh(x)   Hyperbolic cosine of x
	sinh(x)   Hyperbolic cosine of x
	tanh(x)   Hyperbolic tangent of x	
		
		"""
#example cost_functions are given
#cost_function = '-2*((-x+1/x)/(x*(x-1/x)**2)-1/(x*(x-1/x)))'
#cost_function="(7/2)*x**3 - x**9 +1"
#cost_function="6*x**5+11*x**4 -33*x**3-33*x**2 + 11*x+6"
x = Symbol('x')
cost_function=raw_input("Enter cost function f(x):  ").strip()
c_f=sympify(cost_function)
#will lambdify c_f for fast parrallel multipoint computation 
f = lambdify(x, c_f, "numpy")
#print("Verify f(0.9)")
#print N(f(0.9))

batch_gradient_descent(c_f, f)