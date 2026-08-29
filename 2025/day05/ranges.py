import time

def part1():
  start_time = time.time()

  with open("./2025/day05/data.txt", "r") as file:
    lines = file.readlines()

  ranges = []
  for i in range(0, len(lines)):
    line = lines[i]
    if line == "\n":
      ingredients = [int(v.strip()) for v in lines[i+1:]]
      break

    start, end = line.strip().split("-")
    ranges.append((int(start), int(end)))

  fresh_ingredients = 0
  ranges.sort(key=lambda n: n[0])

  for ingredient in ingredients:
    for s, e in ranges:
      if ingredient >= s and ingredient <= e:
        fresh_ingredients += 1
        break
      elif ingredient < s:
        break

  end_time = time.time()

  print(f"Day 5 part 1:\n\tNumber of fresh ingredients: {fresh_ingredients}\n\tDuration: {end_time - start_time:.3f}s")

def part2():
  start_time = time.time()
  
  with open("./2025/day05/data.txt", "r") as file:
    lines = file.readlines()

  ranges = []
  for i in range(0, len(lines)):
    line = lines[i]
    if line == "\n":
      break

    start, end = line.strip().split("-")
    ranges.append((int(start), int(end)))

  ranges.sort(key=lambda n: n[0])
  full_ranges = []

  for s, e in ranges:
    processed = False
    for i, (other_s, other_e) in enumerate(full_ranges):
      # other s is always more than s
      if s <= other_e and e <= other_e:
        processed = True
        break
      elif s <= other_e:
        full_ranges[i] = (other_s, e)
        processed = True
        break

    if not processed:
      full_ranges.append((s, e))

  fresh_range_count = 0
  for s, e in full_ranges:
    fresh_range_count += (e - s) +1

  end_time = time.time()

  print(f"Day 5 part 2:\n\tNumber of fresh ingredients IDs: {fresh_range_count}\n\tDuration: {end_time - start_time:.3f}s")

if __name__ == "__main__":
  part1()
  part2()