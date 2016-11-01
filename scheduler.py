def scheduler(schedule, cooldown):
	timesteps = 0

	task_set = set(schedule)
	cooldown_time = {task : 0 for task in task_set}

	for task in schedule:
		timesteps += 1
		if cooldown_time[task] > 0:
			extra_steps = cooldown_time[task]
			timesteps += extra_steps

			for elem in schedule:
				cooldown_time[elem] -= extra_steps
		else:
			for elem in schedule:
				cooldown_time[elem] -= 1
		cooldown_time[task] = cooldown


	return timesteps

print(scheduler(['A', 'B', 'C', 'A', 'B', 'C'], 3))
print(scheduler(['A', 'A'], 3))
print(scheduler(['A'], 3))
print(scheduler([], 3))

