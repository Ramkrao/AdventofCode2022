def find_fully_contained_part1(arr):
  if (int(arr[0].split('-')[0]) <= int(arr[1].split('-')[0]) and int(arr[0].split('-')[1]) >= int(arr[1].split('-')[1])) or \
    (int(arr[1].split('-')[0]) <= int(arr[0].split('-')[0]) and int(arr[1].split('-')[1]) >= int(arr[0].split('-')[1])):
    return True

def find_fully_contained_part2(arr):
  a = arr[0].split('-')
  b = arr[1].split('-')
  for i in range(int(a[0]), int(a[1])+1):
    for j in range(int(b[0]), int(b[1])+1):
      if i == j: return True

pairs1 = []
pairs2 = []
with open('day4/input.txt') as f:
  for line in f:
    if find_fully_contained_part1(line.strip().split(',')):
      pairs1.append(line.strip())
    if find_fully_contained_part2(line.strip().split(',')):
      pairs2.append(line.strip())

print(pairs1, len(pairs1))
print(pairs2, len(pairs2))
