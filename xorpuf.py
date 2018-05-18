import numpy as np
#from sklearn.iterar_model import LogisticRegression
#from sklearn.model_selection import train_test_split

#Number of Levels
level = 4 

#Number of Stages
stages = 48

#Number of Challenge Responses
ncr    = 2

#Train to testing Ratio
ttt    = 0.2

#Delay Vector with K+1 stages
# stage_delays = np.random.uniform(low=-0.5,high=0.5,size=stages+1)
# print "Stage Delays", stage_delays
# print "\n"
#Size(stage_delays) = stages + 1
#Even Arbiter has a stage

s = (level,stages+1)
sd=np.zeros(s)

for lvl in range(level):
	stage_random = np.random.uniform(low=-0.5,high=0.5,size=stages+1)
	sd[lvl] = stage_random
	print lvl, sd[lvl]

# Thus, we have created unique delay vector for each level of of the XOR PUF
# Thus, we have same challenge applied accross four levels of PUFS, each with a different delay vector

#Challenge vector for all multiplexers
#Feature vector for size = stages + 1
# feature_vector [ last stage ] = 1
# All other stages computed

#Creating Challenge Vector
#Challenge vector common for each iteration / challenge response pair #
# This implies feature is also common

for iter in range(ncr):
	iteration_response = np.zeros(ncr)
	challenge_vector = np.random.randint(low = 0, high =2, size = stages)
	for lvl in range(level):
		stage_delays = sd[lvl]
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
#		print "lvl", lvl, " r ", r
#		print "\n"
		iteration_response[iter] = (iteration_response[iter] + r) %2
	sarr = [str(x) for x in challenge_vector]
	#print "iteration_response", iteration_response[iter]
	#print iter, "\t", (" " . join(sarr)),"\t",iteration_response[iter]
	# print "\n"
	sarr2 = [str(x) for x in feature_vector]
	print (" " . join(sarr2)),"\t",iteration_response[iter]
#	print "\n"
#	print "\n"

#	print challenge_vector, r