from collections import defaultdict
#
#
#
#
#
#
#
#
#
#
#тут тл на 17 тест хз как лучше
#
#
#
#
#
#
#
#

def fill(depth, i):
    left = tree[i << 1]
    tour_num = n - depth
    for pl in players_won[left]:
        if wins_of_player[pl] == tour_num:
            return pl

with open('input.txt', encoding="utf-8") as file:
    s = [i.strip().split("  ") for i in file.readlines()]
    n = int(s[0][0])
    q = [j for i in s[1:] for j in i]

tree = ["."] + [-1] * (2 ** (n + 1) - 1)
matches = [list(map(int, q[i].split())) for i in range(2 ** n - 1)]

players_won = defaultdict(list)
wins_of_player = defaultdict(int)

for winner, loser in matches:
    players_won[winner].append(loser)
    wins_of_player[winner] += 1

sub_ls = sorted(players_won.keys(), key=lambda x: -len(players_won[x]))
abs_winner = sub_ls[0]
tree[1] = abs_winner

max_depth = (2 ** (n + 1)) // 2
k = 1
for i in range(1, max_depth):
    if 2 ** (k+1) == 2*i:
        k += 1
    tree[i << 1] = tree[i]
    tree[(i << 1) + 1] = fill(k, i)

with open('output.txt', 'w') as f:
    res = tree[2**n:]
    f.write(" ".join(map(str, res)))