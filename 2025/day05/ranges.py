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

if __name__ == "__main__":
  part1()