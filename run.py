import gym
import numpy as np
#import roulette
from lib.env.roulette import new_roulette
#if __name__ == "__main__":
#   env = new_roulette()

RLette = new_roulette()

# Q-TABLE
qtable = np.zeros([RLette.observation_space.n,RLette.action_space.n])
# HYPERPARAMETERS
lr = .1
gamma = .9
epsilon = .1
episodes = 100000
steps = 100

print(qtable)

#	UTIL variables to store all the budgets so far 
gainz = []
verbose = False

for _ in  range(episodes):
	state = RLette.reset()
	for _ in range(steps):
		#	Either take a random action or use qlearning
		if np.random.uniform(0,1) < epsilon:
			action = RLette.action_space.sample()
		else:
			action = np.argmax(qtable[state])
		
		nextstate, reward, done, info = RLette.step(action)	
		
		current_Q = qtable[state, action]
		bestnextmove = np.argmax(qtable[nextstate])
		next_Q = qtable[nextstate][bestnextmove]
		
		qtable[state,action] = (1 - lr) * current_Q + lr*(reward + gamma*next_Q)
		
		state = nextstate
		
		if done:
			gain = RLette.budget - 500
			if verbose: 
				print("Episode is over.")
				print("Number of steps: %s" % steps)
				print("Net gain: {}".format())
			else:
				gainz.append(gain)
	 	  #env.render()
			break
print("Session ended. Result:", gainz)
