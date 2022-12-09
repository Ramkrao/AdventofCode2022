isList = False
currentNode = None
root = None
dirs = []
totDiskSpace = 70000000
minDiskSpace = 30000000

class Tree:
  def __init__(self):
    self.data = None
    self.parent = None
    self.children = []

def calculate_size(node):
  size = 0
  if type(node) is Tree:
    for child in node.children:
      if type(child) is Tree:
        size += calculate_size(child)
      else:
        size += int(child['size'])
  # print("Final ::", node.data, size)
  dirs.append({'name': node.data, "size": size})
  return size

def calculate_disk_space():
  r = next(filter(lambda x: x['name'] == 'root', dirs))
  free_space = totDiskSpace - r['size']
  required_space = minDiskSpace - free_space
  smallest = r['size']
  smalldir = None
  for dir in dirs:
    if (dir['size'] - required_space) > 0 and smallest > (dir['size'] - required_space):
      smallest = dir['size'] - required_space
      smalldir = dir['name']
  print(smallest, smalldir)

with open('day7/input.txt') as f:
  for line in f:
    cmd = line.strip()
    if cmd.find('$ cd') != -1:
      key = cmd.split(' ')[2]
      if key == '/':
        root = Tree()
        root.data = 'root'
        currentNode = root
      elif key == '..':
        currentNode = currentNode.parent
      else:
        for child in currentNode.children:
          if type(child) is Tree and child.data == key:
            currentNode =child
    elif cmd.find('$ ls') != -1:
      isList = True
    elif isList == True:
      vals = cmd.split(' ')
      v = None
      if vals[0] == 'dir':
        d = Tree()
        d.data = vals[1]
        d.parent = currentNode
        v = d
      else:
        v = {}
        v['key'] = vals[1]
        v['type'] = 'file'
        v['size'] = vals[0]
      currentNode.children.append(v)

calculate_size(root)
tot = 0
for dir in dirs:
  if dir['size'] < 100000:
    tot += dir['size']

print(tot)
calculate_disk_space()
