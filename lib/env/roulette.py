import gym
import numpy as np
from gym import spaces
from gym.utils import seeding

class new_roulette(gym.Env):
	def  __init__(self, spots=37):
		self.n = spots +  1
		self.action_space = spaces.Box(low=0, high=1, shape=
		(7,), dtype=np.int32)
		self.observation_space = spaces.Box(low=0, high=10000,shape = (9,), dtype=np.int32)
		self.seed()
		self.budget = 500
	def  seed(self, seed=None):
		self.np_random, seed = seeding.np_random(seed)
		return  [seed]
	def  step(self, action):
		#assert  self.action_space.contains(action)
		print(action)
		#	Pick a value for the roulette 
		val =  self.np_random.randint(0,  self.n -  1)
		obs = [val, 
			self.budget, 
			val % 2 == 0, 
			val % 2 != 0, 
			val >= 1 and val <= 12, 
			val >= 13 and val <= 24, 
			val >= 25 and val <= 36,
			val >= 1 and val <= 18, 
			val >= 19 and val <= 36]

		reward = 0
		for i in range(len(obs) - 2):
			if obs[i + 2] and action[i]:
				reward += 1
			if not obs[i + 2] and action[i]:
				reward -= 1

		self.budget = self.budget + reward
		obs = [val, 
		self.budget, 
		val % 2 == 0, 
		val % 2 != 0, 
		val >= 1 and val <= 12, 
		val >= 13 and val <= 24, 
		val >= 25 and val <= 36,
		val >= 1 and val <= 18, 
		val >= 19 and val <= 36]

        #print("NUMBER, BUDGET, EVEN, ODD, Ist THIRD, IInd THIRD, IIIrd THIRD, 1ST Half, 2nd Half")
     
		return  obs, reward, self.budget < 100, {}

	def  reset(self):
		self.budget = 500
		return [0,self.budget,0,0,0,0,0,0,0]
	