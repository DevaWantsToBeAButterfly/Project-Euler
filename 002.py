from scripts import timer

start = timer.start()

fibonacci_sequence = [1, 2]
next_number = fibonacci_sequence[-2] + fibonacci_sequence [-1]

while next_number <= 4000000:
    fibonacci_sequence.append(next_number)
    next_number = fibonacci_sequence[-2] + fibonacci_sequence [-1]

print(sum([n for n in fibonacci_sequence if not n % 2]))

timer.end(start)