grid = []
visible_count = 0

def check_surroundings(i, j, row, col):
  visTop = visBot = visLft = visRgt = True
  top = bottom = left = right = 0
  if i == 0 or j == 0 or i == row-1 or j == col-1:
    return True, (top * bottom * left * right)
  else:
    # check top
    r = i - 1
    while r >= 0 and visTop:
      top += 1
      if grid[i][j] <= grid[r][j]:
        visTop = False
      r -= 1
    # check bottom
    r = i + 1
    while r < row and visBot:
      bottom += 1
      if grid[i][j] <= grid[r][j]:
        visBot = False
      r += 1
    # check left
    r = j - 1
    while r >= 0 and visLft:
      left += 1
      if grid[i][j] <= grid[i][r]:
        visLft = False
      r -= 1
    # check right
    r = j + 1
    while r < col and visRgt:
      right += 1
      if grid[i][j] <= grid[i][r]:
        visRgt = False
      r += 1
    return (visTop or visBot or visLft or visRgt), (top * bottom * left * right)

def idenify_visible_trees():
  global visible_count
  row = len(grid[0])
  col = len(grid)
  for i in range(row):
    for j in range(col):
      isvisible, score = check_surroundings(i, j, row, col)
      print(i, j, isvisible, score)
      if isvisible:
        visible_count += 1

with open('day8/input.txt') as f:
  for line in f:
    row = []
    for c in line.strip():
      row.append(int(c))
    grid.append(row)

idenify_visible_trees()

print(visible_count)