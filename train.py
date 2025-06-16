from environment import GridEnvironment
from agent import QLearningAgent

# Ortamı oluştur (5x5 grid, hedef: (4,4), duvar: (1,1), (2,2), (3,3))
env = GridEnvironment(rows=5, cols=5, start=(0, 0), goal=(4, 4),
                      walls=[(1, 1), (2, 2), (3, 3)])

# Ajanı oluştur
agent = QLearningAgent(actions=["up", "down", "left", "right"])

# Eğitim ayarları
episodes = 1000

for ep in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0
    step_count = 0

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        agent.update_q(state, action, reward, next_state)

        state = next_state
        total_reward += reward
        step_count += 1

    if (ep + 1) % 100 == 0:
        print(f"Episode {ep+1}: Toplam Ödül: {total_reward}, Adım Sayısı: {step_count}")

# Eğitim tamamlandıktan sonra Q-table'ı yazdır
print("\n📊 Öğrenilen Q Değerleri:")
for state in sorted(agent.q_table):
    print(f"Konum {state}: {agent.q_table[state]}")
