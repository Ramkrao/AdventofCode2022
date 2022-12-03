def get_priority(c):
  if c.isupper():
    return ord(c) - 38
  else:
    return ord(c) - 96

def split_find_and_priority(line):
  print(line[:len(line)//2], line[len(line)//2:])
  for c in line[:len(line)//2]:
    if line[len(line)//2:].find(c) != -1:
      return get_priority(c)

def find_badge(group):
  for c in group[0]:
    if group[1].find(c) != -1 and group[2].find(c) != -1:
      return get_priority(c)

items = []
group = []
badges = []
with open('day3/input.txt') as f:
  for line in f:
    items.append(split_find_and_priority(line.strip()))
    group.append(line.strip())
    if len(group) == 3:
      badges.append(find_badge(group))
      group = []

print(sum(items), sum(badges))