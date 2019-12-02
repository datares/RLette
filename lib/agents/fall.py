from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN, PPO2
from stable_baselines.common.policies import MlpPolicy

from lib.env.roulette import datares_roulette

import os

def train_andrei(timesteps, name):
    raise NotImplementedError

def train_qj(timesteps, name):
    raise NotImplementedError

def train_chloe(timesteps, name):
    raise NotImplementedError

def train_angela(timesteps, name):
    raise NotImplementedError

def train_francesco(timesteps, name):
    env = datares_roulette
    env = DummyVecEnv([env])
    model = PPO2(MlpPolicy, env, verbose=1,)
    model.learn(total_timesteps=timesteps)
    model.save(name)
    return model

def test_nn(name):
    model_path = os.path.join('models', name)
    model = PPO2.load(model_path)
    return model