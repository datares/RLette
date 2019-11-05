import gym
import numpy as np
import roulette
#env = gym.make('Roulette-v0')
RLette=roulette.n

import gym

from gym import spaces
from gym.utils import seeding

class new_roulette(gym.Env):
	def  __init__(self, spots=37):
		self.n = spots +  1
		self.action_space = spaces.Discrete(self.n)
		self.observation_space = spaces.Discrete(1)
		self.seed()
		self.budget = 500
	def  seed(self, seed=None):
		self.np_random, seed = seeding.np_random(seed)
		return  [seed]
	def  step(self, action):
		assert  self.action_space.contains(action)
		if action ==  self.n -  1:  
			# observation, reward, done, info
			return  0,  0,  True, {}

		#	Pick a value for the roulette 
		val =  self.np_random.randint(0,  self.n -  1)
		
		if val == action ==  0:
			reward =  self.n -  2.0
		elif val !=  0  and action !=  0  and val %  2  == action %  2:
			reward = 1.0
		else:
			reward = -1.0
		
		#	COULD INTRODUCE REWARD CLIPPING

		self.budget = self.budget + reward
		return  0, reward, self.budget < 100, {}

	def  reset(self):
		self.budget = 500
		return 0
	