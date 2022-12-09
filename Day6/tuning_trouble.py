def find_char_sequence(line, count):
  for i in range(len(line)):
    text = line[i:i+count]
    found = True
    for j in range(len(text)):
      for k in range(len(text)):
        if j != k and text[j] == text[k]: found = False
    if found: return i + count

with open('day6/input.txt') as f:
  for line in f:
    print(find_char_sequence(line.strip(), 4))
    print(find_char_sequence(line.strip(), 14))