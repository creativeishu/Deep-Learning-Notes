"""
Gradient Descent
"""

from GradDescent import GradientDescent
class DerivedGradientDescent(GradientDescent):
	'''
	This is the derived class
	'''

	def __init__(self,data=None,alpha=1.0,P_init=None):
		import pylab as np

	def J(self,P):
		print "Make your own Cost Function"
		return 0.0

	def DerivJ(self,P):
		print "Make your own Derivative Cost Function"
		return 0.0

	def Criteria(self,P):
		cost = J(P)
		print "Make your own Criteria for convergence"
		return False

#------------------------------------------------

if __name__=="__main__":
	import pylab as np

	grobj = DerivedGradientDescent()
