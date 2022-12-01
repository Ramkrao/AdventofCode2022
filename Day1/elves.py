highsums = []

def check_and_add_toList(val):
  if len(highsums) < 3:
    highsums.append(val)
  else:
    highsums.sort()
    el = highsums.pop(0)
    if val > el:
      highsums.append(val)
    else:
      highsums.append(el)

with open('day1/input.txt', encoding='utf8') as f:
  curr_sum = 0
  for line in f:
    cal = line.strip()
    if len(cal) == 0:
      check_and_add_toList(curr_sum)
      curr_sum = 0
    else:
      curr_sum += int(cal)

print(highsums, sum(highsums))