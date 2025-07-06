tracker = {
    "Sabrina": 7200,
    "Rumi":7200
}

for _ in range(3):
    runner_name = input("Enter name:  ")
    runner_time = int(input("Enter time: "))

    if runner_name not in tracker:
        tracker[runner_name] = runner_time
    else:
        if tracker[runner_name] < runner_time:
            tracker[runner_name] = runner_time

print(tracker)