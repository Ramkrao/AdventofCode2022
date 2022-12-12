import math
from functools import reduce

monkeys = []
tests = []
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y}

class Monkey:
  def __init__(self):
    self.index = 0
    self.items = []
    self.operation = None
    self.test = 0
    self.ifTrue = 0
    self.ifFalse = 0
    self.totInspected = 0

m = None
def parse_and_construct_input(line):
  global m
  if line.find('Monkey') != -1:
    m = Monkey()
  elif line.find('Starting') != -1:
    instr = line.split(':')
    for item in instr[1].split(','):
      m.items.append(int(item.strip()))
  elif line.find('Operation') != -1:
    instr = line.split('=')
    op = instr[1].strip().split(' ')
    m.operation = {'operand1': op[0].strip(), 'operand2': op[2].strip(), 'type': op[1].strip()}
  elif line.find('Test:') != -1:
    m.test = int(line.split(' ')[3])
    tests.append(m.test)
  elif line.find('If true:') != -1:
    m.ifTrue = int(line.split(' ')[5])
  elif line.find('If false:') != -1:
    m.ifFalse = int(line.split(' ')[5])
    monkeys.append(m)

def compute():
  # Thanks gamma032steam for the tip - https://github.com/gamma032steam/advent-of-code/blob/bb4b1092d43e1a3a9bcc0edcb634e8183c775acd/2022/11.py#L25
  lcm = reduce(lambda x,y: math.lcm(x,y), tests)

  round = 0
  while True:
    round += 1
    # print(f'Starting round {round}', round)
    for m in monkeys:
      for item in m.items:
        m.totInspected += 1
        if m.operation['operand1'] == 'old':
          op1 = item
        if m.operation['operand2'] == 'old':
          op2 = item
        else:
          op2 = int(m.operation['operand2'])
        worry_level = op[m.operation['type']](op1, op2)
        worry_level %= lcm
        # worry_level = math.floor(worry_level / 3)
        if worry_level % m.test == 0:
          monkeys[m.ifTrue].items.append(worry_level)
        else:
          monkeys[m.ifFalse].items.append(worry_level)
      m.items = []
    if round == 10000:
      break

with open('day11/input.txt') as f:
  for line in f:
    parse_and_construct_input(line.strip())

compute()
top_2 = (sorted(m.totInspected for m in monkeys)[-2:])
print(top_2[0] * top_2[1])