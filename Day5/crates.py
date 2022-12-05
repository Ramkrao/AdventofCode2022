import re
import copy

crates1 = [['D','Z','T','H'], ['S','C','G','T','W','R','Q'], ['H','C','R','N','Q','F','B','P'], ['Z','H','F','N','C','L'], ['S','Q','F','L','G'], ['S','C','R','B','Z','W','P','V'], ['J','F','Z'], ['Q','H','R','Z','V','L','D'], ['D','L','Z','F','N','G','H','B']]
crates2 = copy.deepcopy(crates1)

def parse_and_move1(line):
  instr = re.findall(r"\d+", line)
  for i in range(int(instr[0])):
    crates1[int(instr[2])-1].insert(0,crates1[int(instr[1])-1].pop(0))

def parse_and_move2(line):
  instr = re.findall(r"\d+", line)
  for i in range(int(instr[0]),0,-1):
    crates2[int(instr[2])-1].insert(0,crates2[int(instr[1])-1].pop(i-1))

with open('day5/input.txt') as f:
  for line in f:
    parse_and_move1(line.strip())
    parse_and_move2(line.strip())

for crate in crates1:
  print(crate[0])
print('---------------------------')
for crate in crates2:
  print(crate[0])