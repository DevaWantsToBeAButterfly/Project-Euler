from scripts import timer

start = timer.start()

multiples_sum = 0

for n in range(0,1000,3):
    multiples_sum += n
for n in range(0,1000,5):
    multiples_sum += n
for n in range(0,1000,15):
    multiples_sum -= n

print(multiples_sum)

timer.end(start)