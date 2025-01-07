with open("pipes.txt", "r") as f:
    data = f.read().split("\n")
all_pipe_times = []
for el in data:
    if el != '':
        all_pipe_times.append(float(el))
    else:
        break
work_pipe = list(map(int, data[-1].split()))
all_pipe_times_together = sum(1 / all_pipe_times[i - 1] for i in work_pipe)


res = 60 / all_pipe_times_together
with open("time.txt", "w") as f:
    f.write(str(res))