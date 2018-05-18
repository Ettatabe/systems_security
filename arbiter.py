import numpy as np
#from sklearn.linear_model import LogisticRegression
#from sklearn.model_selection import train_test_split

#Number of Stages
stages = 64

#Number of Challenge Responses
ncr    = 2

#Train to testing Ratio
ttt    = 0.2

#Delay Vector with K+1 stages
stage_delays = np.random.uniform(low=-0.5,high=0.5,size=stages+1)
#print "Stage Delays", stage_delays
#print "\n"
#Size(stage_delays) = stages + 1
#Even Arbiter has a stage

x = []
y = []

#Challenge vector for all multiplexers
#Feature vector for size = stages + 1
# feature_vector [ last stage ] = 1
# All other stages computed

#Creating Challenge Vector
for line in range(ncr):
	challenge_vector = np.random.randint(low = 0, high =2, size = stages)
	feature_vector = np.ones(stages+1)
	feature_vector [stages] = 1
	for i in range(stages):
		for l in range(i,stages):
			feature_vector[i] = feature_vector[i] * (-1)**challenge_vector[l]
	delay = np.dot(stage_delays,feature_vector)
	if delay > 0:
		r= 1
	else:
		r= 0
	#print "Delay", delay, "Line",line,"Challenge",challenge_vector,"  Response",r
	#print "\n"
#	sarr = [str(x) for x in challenge_vector]
	sarr2 = [str(x) for x in feature_vector]

	print(" " . join(sarr2)),"\t",r
	print "\n"
		# print "\n"

#	print challenge_vector, r