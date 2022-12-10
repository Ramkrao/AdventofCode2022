x = 1
cycle = 0
compute_cycles = [20, 60, 100, 140, 180, 220]
signal = 0
pixels = []
for i in range(240):
  pixels.append('.')

def execute(line):
  global cycle, x, signal
  instr = line.split(' ')
  if instr[0] == 'addx':
    for i in range(2):
      compute_signal_strength()
      cycle += 1
    x += int(instr[1])
  elif instr[0] == 'noop':
    compute_signal_strength()
    cycle += 1

def compute_signal_strength():
  global signal
  mod_cycle = cycle
  if cycle in compute_cycles:
    signal += (x * cycle)
  if cycle >= 40:
    mod_cycle = cycle - (int(cycle/40) * 40)
  if mod_cycle-1 <= x <= mod_cycle+1:
    pixels[cycle] = '#'

with open('day10/input.txt') as f:
  for line in f:
    execute(line.strip())

print(signal)

for i, p in enumerate(pixels):
  if i % 40 == 0:
    print() 
  print(p, end="")

