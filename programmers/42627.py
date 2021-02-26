import heapq as hq


def solution(jobs):
    answer, time, num_jobs = 0, 0, len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])

    while jobs:
        for req_time, run_time in jobs:
            if req_time <= time:    # if arrived
                time += run_time    # add processing time
                answer += time - req_time   # add waiting time
                jobs.pop(jobs.index([req_time, run_time]))
                break
            if [req_time, run_time] == jobs[len(jobs) - 1]:
                time += 1

    return answer // num_jobs


print(solution([[0, 3], [1, 9], [2, 6]]))
