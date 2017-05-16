from time import sleep
import gym

def main():
    env = gym.make('CartPole-v0')
    env.render()

    RIGHT = 1
    LEFT = 0

    SLOW = 0.01 # 1/SPEED

    def choose_action(state, end):
        x, dx, w, dw = state
        return RIGHT
    
    def update(state, end, next_state):
        x, dx, w, dw = state
        nx, ndx, nw, ndw = next_state
        pass
    
    for episode in range(20):
        state = env.reset()
        done = False
        t = 0
        while not done:
            sleep(SLOW)
            env.render()
            action = choose_action(state, done)         # action = env.action_space.sample()
            next_state, _, done, _ = env.step(action)   # state, reward, done, info = env.step(action)
            update(state, done, next_state)
            state = next_state
            t += 1
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                sleep(0.5)
                break


if __name__ == '__main__':
    main()
