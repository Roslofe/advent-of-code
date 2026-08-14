import time
from itertools import product

def get_neighbour_coordinates(x, y, x_max, y_max):
  x_options = [i for i in range(max(0, x - 1), min(x_max, x + 2))]
  y_options = [i for i in range(max(0, y - 1), min(y_max, y + 2))]
  neighbours = list(product(x_options, y_options))
  neighbours.remove((x, y))
  return neighbours

def part1():
  start_time = time.time()
  
  with open("./2025/day04/data.txt","r") as file:
    grids = [line.strip() for line in file.readlines()]

  columns_total = len(grids[0])
  rows_total = len(grids)

  neighbour_counts = {}

  roll_locations = []

  for r, row in enumerate(grids):
    for c, element in enumerate(row):
      if element == "@":
        roll_locations.append((c, r))
        for location in get_neighbour_coordinates(c, r, columns_total, rows_total):
          neighbour_counts[location] = neighbour_counts.get(location, 0) + 1

  accessible = 0
  for roll in roll_locations:
    if neighbour_counts.get(roll, 0) < 4:
      accessible += 1

  end_time = time.time()
  
  print(f"Day 4 part 1:\n\tAccessible rolls of paper: {accessible}\n\tDuration: {end_time - start_time:.3f}s")

    
part1()