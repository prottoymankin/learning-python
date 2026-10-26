# while loop
counter = 1
while counter <= 5:
  print("Hello World!")
  counter += 1

counter_1 = 1
while counter_1 <= 4:
  print(counter_1 * '*')
  counter_1 += 1

counter_2 = 5
while counter_2 > 0:
  print(counter_2)
  counter_2 -= 1

# for loops
for counter_3 in range(1, 6):
  print(counter_3)

for i in range(2, 11, 2):
  print(i)

for i in range(1, 51):
  if i == 21: break
  if i % 3 == 0:
    print(i);

for i in range(1, 51):
  if i == 21: continue
  if i % 3 == 0:
    print(i)