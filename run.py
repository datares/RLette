
from lib.env.roulette import datares_roulette

from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN, PPO2
from stable_baselines.common.policies import MlpPolicy
from lib.env.roulette import combos
from itertools import combinations 
import pandas as pd
import gym
import numpy as np
import argparse

def play(model):
	arr = combos()
	while(1):
		val = input("Enter number")
		val = int(val)
		obs = [val, 
				500, 
				val % 2 == 0, 
				val % 2 != 0, 
				val >= 1 and val <= 12, 
				val >= 13 and val <= 24, 
				val >= 25 and val <= 36,
				val >= 1 and val <= 18, 
				val >= 19 and val <= 36]
		pred = model.predict(obs)
		print(arr[pred])
def train_PPO2_agent(name, timesteps=1000):
	env = datares_roulette()
	env = DummyVecEnv([lambda: env])
	model = PPO2(MlpPolicy, env, verbose=1)
	model.learn(total_timesteps=timesteps)
	model.save(name)
	return model
def test_model(model, episodes, steps, env):
	average_gain = []
	for _ in  range(episodes):
		state = env.reset()
		for _ in range(steps):
			action, _states = model.predict(state)
			nextstate, _ , done, _ = env.step(action)	
			state = nextstate

			if done:
				gain = env.budget - 500
				average_gain.append(gain)
		gain = env.budget - 500
		average_gain.append(gain)
		
		print("BUDGET: {}".format(env.budget))
		print("AVERAGE_GAIN: {}".format(mean(average_gain)))
		print("-------------------------------------------")
def mean(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i]
	sum = sum / len(arr)
	return sum

if __name__ == "__main__":
	EPISODES = 1000
	STEPS = 500
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', '--mode', type=str, required=True,
						help='choose between train and test.')
	parser.add_argument('-n', '--name', type=str, required=True,
						help='Your model name.')

	# Parses arguments
	args = parser.parse_args()
	env = datares_roulette()

	if args.mode == "train":
		model = train_PPO2_agent(args.name, 7000000)
	if args.mode == "test":
		model = PPO2.load(args.name)
	test_model(model, EPISODES, STEPS, env)