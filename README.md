# 🧠 Q-Learning Agent in a 2D Grid World

This project demonstrates a simple **Q-learning agent** navigating through a 2D grid environment. The agent learns — through trial and error — how to reach a goal position while avoiding obstacles.

---

## 🌟 Features

- 2D grid environment (default: 5x5)
- Customizable start, goal, and wall positions
- Reward structure: +10 for goal, -1 for every move
- Q-learning algorithm implementation
- Console visualization of the learned path
- Modular and beginner-friendly code structure

---

## 🧠 Q-Learning Formula

The agent learns by updating a Q-table using the following formula:
Q(s, a) ← Q(s, a) + α × (r + γ × max Q(s’, a’) − Q(s, a))


Where:
- `s` is the current state (position)
- `a` is the action taken
- `r` is the immediate reward
- `s’` is the new state after action
- `α` is the learning rate
- `γ` is the discount factor

---

## 📂 Project Structure

| File            | Description                              |
|-----------------|------------------------------------------|
| `environment.py`| The 2D grid world and step logic         |
| `agent.py`      | Q-learning agent logic                   |
| `train.py`      | Trains the agent in the environment      |
| `visualize.py`  | Displays the path learned by the agent   |
| `README.md`     | Project documentation                    |

---

## 🛠 How to Run

1. Clone the repository:
git clone https://github.com/yourusername/qlearning-agent-2d.git
cd qlearning-agent-2d

2.Train the agent:
python3 train.py

3.Visualize the learned path:
python3 visualize.py

🖼 Sample Output (Terminal Visualization)

S 🟩 ⬜ ⬜ ⬜
⬜ ⬛ ⬜ ⬜ ⬜
⬜ ⬜ ⬛ ⬜ ⬜
⬜ ⬜ ⬜ ⬛ ⬜
⬜ ⬜ ⬜ ⬜ G

S → Start

G → Goal

⬛ → Wall

🟩 → Agent's path

⬜ → Empty cell





