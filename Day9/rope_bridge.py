headRow = headCol = 0
tails_mov_list = []
tailRow = []
tailCol = []
for i in range(9):
  tailRow.append(0)
  tailCol.append(0)
  tails_mov_list.append([])
  tails_mov_list[i].append({'row': tailRow[i], 'col': tailCol[i]})

def simulate_motion(line):
  global headRow, headCol
  instr = line.split(' ')
  if instr[0] == 'R':
    for i in range(int(instr[1])):
      headCol += 1
      iterate_tails()
  elif instr[0] == 'L':
    for i in range(int(instr[1])):
      headCol -= 1
      iterate_tails()
  elif instr[0] == 'U':
    for i in range(int(instr[1])):
      headRow -= 1
      iterate_tails()
  elif instr[0] == 'D':
    for i in range(int(instr[1])):
      headRow += 1
      iterate_tails()

def iterate_tails():
  for index in range(9):
    if index == 0:
      hr = headRow
      hc = headCol
      tr = tailRow[index]
      tc = tailCol[index]
    else:
      hr = tailRow[index-1]
      hc = tailCol[index-1]
      tr = tailRow[index]
      tc = tailCol[index]
    compute_tail_pos(hr, hc, tr, tc, index)

def compute_tail_pos(hr, hc, tr, tc, index):
  pos = []
  for i in range(hr-1,hr+2):
    for j in range(hc-1,hc+2):
      pos.append({'row': i, 'col': j})
      if tr == i and tc == j:
        return
  # head in same row but right
  if hr == tr and hc - tc == 2:
    tc += 1
  # head in same row but left
  elif hr == tr and tc - hc == 2:
    tc -= 1
  # head in same col but up
  elif hc == tc and tr - hr == 2:
    tr -= 1
  # head in same col but down
  elif hc == tc and hr - tr == 2:
    tr += 1
  # head is in diagonal 2 up - 1 right
  elif tr - hr == 2 and hc - tc == 1:
    tc += 1
    tr -= 1
  # head is in diagonal 2 up - 1 left
  elif tr - hr == 2 and tc - hc == 1:
    tc -= 1
    tr -= 1
  # head is in diagonal 2 bottom - 1 right
  elif hr - tr == 2 and hc - tc == 1:
    tr += 1
    tc += 1
  # head is in diagonal 2 bottom - 1 left
  elif hr - tr == 2 and tc - hc == 1:
    tr += 1
    tc -= 1
  # head is in diagonal 1 up - 2 right
  elif tr - hr == 1 and hc - tc == 2:
    tc += 1
    tr -= 1
  # head is in diagonal 1 up - 2 left
  elif tr - hr == 1 and tc - hc == 2:
    tc -= 1
    tr -= 1
  # head is in diagonal 1 bottom - 2 right
  elif hr - tr == 1 and hc - tc == 2:
    tr += 1
    tc += 1
  # head is in diagonal 1 bottom - 2 left
  elif hr - tr == 1 and tc - hc == 2:
    tr += 1
    tc -= 1
  # head is in diagonal 2 up - 2 right
  elif tr - hr == 2 and hc - tc == 2:
    tc += 1
    tr -= 1
  # head is in diagonal 2 up - 2 left
  elif tr - hr == 2 and tc - hc == 2:
    tc -= 1
    tr -= 1
  # head is in diagonal 2 bottom - 2 right
  elif hr - tr == 2 and hc - tc == 2:
    tr += 1
    tc += 1
  # head is in diagonal 2 bottom - 2 left
  elif hr - tr == 2 and tc - hc == 2:
    tr += 1
    tc -= 1

  tailRow[index] = tr
  tailCol[index] = tc
  found = False
  for m in tails_mov_list[index]:
    if m['row'] == tr and m['col'] == tc:
      found = True
  if not found:
    tails_mov_list[index].append({'row': tr, 'col': tc})

with open('day9/input.txt') as f:
  for line in f:
    simulate_motion(line.strip())

print(len(tails_mov_list[0]), len(tails_mov_list[8]))