from time import sleep
import gym

def main():
    env = gym.make('CartPole-v0')
    for episode in range(20):
        state = env.reset()
        for t in range(100):
            sleep(0.01)
            env.render()
            action = env.action_space.sample()
            state, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                sleep(0.5)
                break


if __name__ == '__main__':
    main()
