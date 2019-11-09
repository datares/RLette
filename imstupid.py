from lib.env.roulette import new_roulette
if __name__ == "__main__":
    env = new_roulette()
    print("0 means we are not betting on that type, 1 means we are.")
    env.reset()
    for i in range(100):
        action = env.action_space.sample()
        print("LEGEND (STATE): [NUMBER, BUDGET, EVEN, ODD, 1st Third, 2nd Third, 3rd Third, 1st Half, Second_Half] )")
        print("LEGEND (ACTION): [EVEN, ODD, 1st Third, 2nd Third, 3rd Third, 1st Half, Second_Half] )")
        print("AGENT_ACTIONS: {}".format(action))
        print("RESULT: {}\n\n\n\n\n".format(env.step(action)))