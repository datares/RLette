from lib.env.roulette import new_roulette
if __name__ == "__main__":
    env = new_roulette()
    
env.reset()

for _ in  range(1000):
    env.step(env.action_space.sample())  # take a random action
    env.render()
env.close()