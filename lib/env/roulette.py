import gym
from gym import spaces
from gym.utils import seeding

class  new_roulette(gym.Env):
	def  __init__(self, spots=37):
		self.n = spots +  1
		self.action_space = spaces.Discrete(self.n)
		self.observation_space = spaces.Discrete(1)
		self.seed()
		self.budget = 100
		self.reward = 0
		self.val = 'placeholder'
		self.bet = 'placeholder'

	def  seed(self, seed=None):
		self.np_random, seed = seeding.np_random(seed)
		return  [seed]
	def  step(self, action):
		assert  self.action_space.contains(action)
		self.bet = action
		if action ==  self.n -  1:
			# observation, reward, done, info
			return  0,  0,  True, {}, self.budget
		# N.B. np.random.randint draws from [A, B) while random.randint 		draws from [A,B]
		self.val =  self.np_random.randint(0,  self.n -  1)
		if self.val == action:
			self.reward = 15
		if self.val == action ==  0:
			self.reward =  self.n -  2.0
		elif self.val !=  0  and action !=  0  and self.val %  2  == action %  2:
			self.reward =  1.0
		else:
			self.reward =  -1.0

		return  0, self.reward,  False, {}, self.budget, self.val, action
    
	def render(self):
        # Render the environment to the scsreen
		self.budget = self.budget + self.reward
		print('You bet on ' + str(self.bet) + '. The roulette ball has landed on ' + str(self.val) + '.')
		print('You earned ' + str(self.reward) + ' in the previous round.')
		print('Your current budget is ' + str(self.budget))

	def  reset(self):
		return  0

# if  __name__  ==  "__main__":
# 	n =  NewRoulette()
# 	print(n.action_space, n.observation_space)


# #import rouletteclass
# #env = gym.make('Roulette-v0')
# env = NewRoulette()
# env.reset()

# for _ in  range(1000):
#     env.step(env.action_space.sample()) # take a random action
#     env.render()