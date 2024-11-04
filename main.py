import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

path = [(0, 0)]

for _ in range(1000):
    direction = random.choice([1, -1])
    x_or_y = random.choice(['x', 'y'])
    match x_or_y, direction:
        case 'x', 1:
            path.append((path[-1][0] + 1, path[-1][-1]))
        case 'x', -1:
            path.append((path[-1][0] - 1, path[-1][-1]))
        case 'y', 1:
            path.append((path[-1][0], path[-1][-1] + 1))
        case 'y', -1:
            path.append((path[-1][0], path[-1][-1] - 1))

path_x = list(path[n][0] for n in range(len(path)))
path_y = list(path[n][-1] for n in range(len(path)))

fig, ax = plt.subplots()
scat = ax.scatter([], [], color="blue")

ax.set_xlim(min(path_x) - 1, max(path_x) + 1)
ax.set_ylim(min(path_y) - 1, max(path_y) + 1)

def update(frame):
    current_x = path_x[:frame + 1]
    current_y = path_y[:frame + 1]
    colors = ["green"] + ["blue"] * (frame - 1) + ["red"] if frame > 0 else ["green"]
    scat.set_offsets(list(zip(current_x, current_y)))
    scat.set_color(colors)
    return scat,

animation = FuncAnimation(fig, update, frames=range(len(path)), interval=50, blit=True)

plt.show()
