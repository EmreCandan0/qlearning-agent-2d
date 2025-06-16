from environment import GridEnvironment
from agent import QLearningAgent
import pickle

def visualize(agent, env):
    state = env.reset()
    path = [state]
    done = False
    step_limit = 100  # sonsuz döngüye girmesin diye

    for _ in range(step_limit):
        q_values = agent.get_q_values(state)
        action = max(q_values, key=q_values.get)  # en iyi aksiyon
        next_state, _, done = env.step(action)
        path.append(next_state)
        state = next_state
        if done:
            break

    draw_grid(env, path)

def draw_grid(env, path):
    print("\n🗺️ Öğrenilen Yol Haritası:\n")
    for r in range(env.rows):
        row_str = ""
        for c in range(env.cols):
            pos = (r, c)
            if pos == env.start:
                row_str += "S "  # Start
            elif pos == env.goal:
                row_str += "G "  # Goal
            elif pos in env.walls:
                row_str += "⬛ "
            elif pos in path:
                row_str += "🟩 "
            else:
                row_str += "⬜ "
        print(row_str)

# Eğitim yeniden yapılmasın diye buraya da eğitim koyabiliriz:
if __name__ == "__main__":
    env = GridEnvironment(rows=5, cols=5, start=(0, 0), goal=(4, 4),
                          walls=[(1, 1), (2, 2), (3, 3)])
    agent = QLearningAgent(actions=["up", "down", "left", "right"])

    # Ajanı eğit (1000 adım)
    for _ in range(1000):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update_q(state, action, reward, next_state)
            state = next_state

    # Öğrenilen yolu çiz
    visualize(agent, env)
