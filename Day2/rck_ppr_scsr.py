
def check_and_score_part1(a):
  if a[0] == 'A':
    if a[1] == 'X': return 3+1
    elif a[1] == 'Y': return 6+2
    elif a[1] == 'Z': return 0+3
  elif a[0] == 'B':
    if a[1] == 'X': return 0+1
    elif a[1] == 'Y': return 3+2
    elif a[1] == 'Z': return 6+3
  elif a[0] == 'C':
    if a[1] == 'X': return 6+1
    elif a[1] == 'Y': return 0+2
    elif a[1] == 'Z': return 3+3

def check_and_score_part2(a):
  if a[0] == 'A':
    if a[1] == 'X': return 0+3
    elif a[1] == 'Y': return 3+1
    elif a[1] == 'Z': return 6+2
  elif a[0] == 'B':
    if a[1] == 'X': return 0+1
    elif a[1] == 'Y': return 3+2
    elif a[1] == 'Z': return 6+3
  elif a[0] == 'C':
    if a[1] == 'X': return 0+2
    elif a[1] == 'Y': return 3+3
    elif a[1] == 'Z': return 6+1

scores_part1 = []
scores_part2 = []
with open('day2/input.txt') as f:
  for line in f:
    scores_part1.append(check_and_score_part1(line.strip().split(' ')))
    scores_part2.append(check_and_score_part2(line.strip().split(' ')))

print(sum(scores_part1), sum(scores_part2))