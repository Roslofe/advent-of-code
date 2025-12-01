import time

class Dial():

  # assume minimum value is 0, and max_value is exclusive
  def __init__(self, start_pos=50, max_value=100):
    self.__position = start_pos
    self.__max_value = max_value

  def turn_left(self, amount):
    # remove any full turns, as they don't contribute to the end value
    turn_amount = amount % self.__max_value
    new_pos = self.__position - turn_amount

    # in case we go past 0
    if new_pos < 0:
      new_pos = self.__max_value + new_pos

    self.__position = new_pos
    return new_pos
  
  def turn_right(self, amount):
    # remove full turns
    turn_amount = amount % self.__max_value
    new_pos = self.__position + turn_amount

    if new_pos >= self.__max_value:
      new_pos = new_pos - self.__max_value

    self.__position = new_pos
    return new_pos
  

def part_1():
  start_time = time.time()

  with open("./2025/day01/data.txt","r") as file:
    turns = file.readlines()
  
  turns = [ (turn_info[0], int(turn_info.strip()[1:])) for turn_info in turns ]

  dial = Dial()
  positions = [dial.turn_left(amount) if direction == "L" else dial.turn_right(amount) for (direction, amount) in turns]
  zero_count = len(list(filter(lambda n: n==0, positions)))
  
  end_time = time.time()

  print(f"Day 1 part 1:\n\tPassword: {zero_count}\n\tDuration: {end_time - start_time:.3f}s")

part_1()