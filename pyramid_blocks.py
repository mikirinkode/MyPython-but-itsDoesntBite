blocks = int(input("How many blocks do you have? : "))
space = blocks // 2
height = 0

while blocks > height:
  height += 1         # each layer consist of (n + 1) blocks
  blocks -= height    
  space -= 1
  print(" "*space + "[]"*height)
