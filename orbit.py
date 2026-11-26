# Planet going around the Sun - the simple version
#
# The story:
#   The Sun pulls the planet towards it (gravity).
#   The planet is also moving sideways.
#   Pull + sideways motion = the planet goes round and round.
#
# We make a movie one tiny step at a time:
#   1. Find out how strongly the Sun pulls the planet.
#   2. Change the planet's speed a little because of the pull.
#   3. Move the planet a little bit.
#   4. Repeat many times and remember every place the planet visited.

import math
import matplotlib.pyplot as plt

# ---- starting point ----
x = 1.0        # planet starts 1 step to the right of the Sun
y = 0.0
vx = 0.0       # no speed to the right
vy = 1.0       # speed 1 going upwards (try 0.5, 0.8, 1.2, 1.5 later!)

dt = 0.01      # size of one tiny time step
steps = 1000   # how many steps to take

# lists to remember where the planet has been
xs = []
ys = []

# ---- the movie loop ----
for step in range(steps):
    # distance from the Sun (the Sun sits at 0, 0)
    r = math.sqrt(x * x + y * y)

    # the pull of gravity gets weaker when you are far away
    ax = -x / (r * r * r)
    ay = -y / (r * r * r)

    # 1) the pull changes the speed
    vx = vx + ax * dt
    vy = vy + ay * dt

    # 2) the speed changes the position
    x = x + vx * dt
    y = y + vy * dt

    # remember this place
    xs.append(x)
    ys.append(y)

# ---- draw the picture ----
plt.plot(xs, ys, label="planet path")
plt.plot(0, 0, "o", color="orange", markersize=15, label="Sun")
plt.gca().set_aspect("equal")    # makes circles look like circles
plt.legend()
plt.title("Planet orbit")
plt.savefig("orbit.png")
plt.show()
