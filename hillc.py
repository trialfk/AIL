import random
# Function to maximize
def f(x):
    return -x**2 + 9  
def hill_climb(start, steps=100, step_size=0.1):
    current = start
    print(f"Starting at x = {current:.2f}, f(x) = {f(current):.2f}\n")
    for i in range(steps):
        neighbors = [current + step_size, current - step_size]
        next_move = max(neighbors, key=f)
        print(f"Step {i+1}: x = {current:.2f}, Best neighbor = {next_move:.2f}, f(x) = {f(next_move):.2f}")
        if f(next_move) <= f(current):
            print("\nNo better neighbor found — stopping climb.")
            break
        current = next_move
    return current, f(current)
# Example usage
start = random.uniform(0, 6)
x, fx = hill_climb(start)
print(f"\nEstimated Maximum: x = {x:.2f}, f(x) = {fx:.2f}")
 #keep executing until setps less/ equal 20