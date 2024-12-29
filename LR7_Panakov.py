import sys
import math

g, h, q = [int(i) for i in input().split()]

def baby_step_giant_step(g, h, q):
    m = int(math.ceil(math.sqrt(q)))

    baby_steps = {pow(g, j, q): j for j in range(m)}

    g_m = pow(g, m * (q - 2), q) 

    for k in range(m):
        current = (h * pow(g_m, k, q)) % q
        if current in baby_steps:
            return k * m + baby_steps[current]

    return -1 

x = baby_step_giant_step(g, h, q)

print(x)