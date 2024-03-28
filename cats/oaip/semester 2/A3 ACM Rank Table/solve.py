class Team:
    def __init__(self, number):
        self.number = number
        self.problems_solved = 0
        self.total_time = 0
        self.submission_times = [[] for _ in range(21)]


with open('input.txt', 'r') as file:
    C, N = map(int, file.readline().split())
    teams = [Team(i + 1) for i in range(C)]
    for _ in range(N):
        ci, pi, ti, ri = map(int, file.readline().split())
        ci -= 1
        pi -= 1
        teams[ci].submission_times[pi].append((ti, ri))

for team in teams:
    for i in range(21):
        team.submission_times[i].sort()
        penalty = 0
        for run in team.submission_times[i]:
            if run[1] == 1:
                team.problems_solved += 1
                team.total_time += run[0] + penalty
                break
            else:
                penalty += 20 * 60

with open('output.txt', 'w') as file:
    teams.sort(key=lambda x: (-x.problems_solved, x.total_time, x.number))
    for team in teams:
        file.write(str(team.number) + ' ')
