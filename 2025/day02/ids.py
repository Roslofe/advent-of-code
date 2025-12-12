import time
import re

def part_1():

  start_time = time.time()

  with open("./2025/day02/data.txt","r") as file:
      id_ranges = file.readline().split(",")

  invalid_ids = []

  for range_data in id_ranges:
      start, end = range_data.split("-")
      num_range = list(range(int(start), int(end) + 1))
      for num in num_range:
          if re.match("^([0-9]+)\\1$", f"{num}") is not None:
              invalid_ids.append(num)

  id_sum = sum(invalid_ids)

  end_time = time.time()

  print(f"Day 2 part 1:\n\tSum of invalid IDs: {id_sum}\n\tDuration: {end_time - start_time:.3f}s")
    
part_1()