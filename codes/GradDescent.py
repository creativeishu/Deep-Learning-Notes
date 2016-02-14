"""
Gradient Descent
"""

class GradientDescent(object):
	'''
	Inherit this class to add the following functions:
	1) Cost Function: J
	2) Derivative of the Cost Function: DerivJ
	3) Criteria to ensure convergence: Criteria
	'''

	def __init__(self,data=None,alpha=1.0,P_init=None):
		import pylab as np

		if data==None:
			data = np.zeros((100,10))

		self.alpha = alpha

		# Total number of features including X0
		self.nFeatures = len(data[0])
		self.X = data[:,:self.nFeatures-1]
		self.Y = data[:,self.nFeatures-1]

		# Adding X0=1 to all samples
		self.Addx0()

		# The initial parameter set to zero, if not specified
		if P_init==None:
			self.P_init = np.zeros((self.nFeatures))
		else:
			self.P_init = P_init

		print "Gradient Descent base class"

	def Addx0(self):
		# Adding X0=1 to the features. 
		x0 = np.ones((len(self.X)))
		self.X = np.transpose(np.vstack((x0,np.transpose(self.X))))
		return 0.0

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

	def UpdateParameters(self,P):
		# Update parameter
		return P + self.alpha * DerivJ(P)

	def Run(self,P):
		P = self.P_init
		while Criteria(P):
			P = UpdateParameters(P)
		return P

#------------------------------------------------

if __name__=="__main__":
	import pylab as np

