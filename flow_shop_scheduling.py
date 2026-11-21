n = int(input("Enter number of jobs: "))
jobs = []
for i in range(n):
    first, second = map(int, input(f"Enter M1 and M2 processing times for job {i + 1}: ").split())
    jobs.append((i + 1, first, second))

left, right = [], []
remaining = jobs[:]
while remaining:
    job = min(remaining, key=lambda item: min(item[1], item[2]))
    remaining.remove(job)
    if job[1] <= job[2]:
        left.append(job)
    else:
        right.append(job)

order = left + right[::-1]
time_m1 = time_m2 = 0
for job_id, first, second in order:
    time_m1 += first
    time_m2 = max(time_m1, time_m2) + second

print("Optimal job sequence:", " ".join(f"J{job[0]}" for job in order))
print("Total elapsed time (makespan):", time_m2)
print("Time Complexity: O(n^2)")