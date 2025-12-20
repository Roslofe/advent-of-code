from itertools import combinations
import time

def part_1():
  start_time = time.time()
  with open("./2025/day03/data.txt", "r") as file:
    banks = file.readlines()

  banks = [list(combinations(list(b), 2)) for b in banks]
  
  joltage = 0

  for battery_options in banks:
    battery_values = [int("".join(b)) for b in battery_options]
    max_value = max(battery_values)
    joltage += max_value

  end_time = time.time()

  print(f"Day 3 part 1:\n\tTotal joltage: {joltage}\n\tDuration: {end_time - start_time:.3f}s")

  

part_1()