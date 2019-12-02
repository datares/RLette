
from lib.env.roulette import datares_roulette
from lib.env.roulette import combos

from lib.agents.fall import test_nn

from itertools import combinations 
import pandas as pd
import gym
import numpy as np
import argparse
import os
import random

def step(obs, model):
	arr = combos()
	action = arr[model.predict(obs)]	
	if action.shape == (1, 7):
		action = action[0]

	reward = compute_reward(obs, action)
	return action, reward
def compute_reward(obs, action):
	reward = 0
	for i in range(len(obs) - 2):
		if obs[i + 2] and action[i]:
			reward += 1
		if not obs[i + 2] and action[i]:
			reward -= 1
	return reward
def multiplayer_roulette(cycles):
	budgets = []
	agents =  [test_nn("500k.zip"), test_nn("1m.zip"), test_nn("2m.zip")]
	for i in range(len(agents)):
		budgets.append(500)

	for _ in range(cycles):
		val = random.randint(0, 38) 
		obs = [val, 
				500, 
				val % 2 == 0, 
				val % 2 != 0, 
				val >= 1 and val <= 12, 
				val >= 13 and val <= 24, 
				val >= 25 and val <= 36,
				val >= 1 and val <= 18, 
				val >= 19 and val <= 36]
		pred = []
		for i in range(len(agents)):
			action, reward = step(obs, agents[i])
			budgets[i] += reward
			pred.append((val, action))

		print(pred, budgets)

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
	multiplayer_roulette(10000)