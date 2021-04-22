from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'Hello from thread {id}')
    sleep(1)


start_time = perf_counter()


n = 50
for i in range(n, 0, -1):
    t = Thread(target=task, args=(i,))
    t.start()

end_time = perf_counter()

print()
print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
