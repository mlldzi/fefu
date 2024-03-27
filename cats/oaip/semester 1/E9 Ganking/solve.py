def check(now_id, data, size_data, good_time):
    fix_time = data[now_id]['time_line']
    fix_victim = data[now_id]['victim_player']

    set_G = [0] * 11

    for i in range(now_id, -1, -1):
        if (fix_time - data[i]['time_line']) >= good_time:
            break
        if data[i]['victim_player'] == fix_victim:
            set_G[data[i]['attacking_player']] = 1

    for i in range(now_id + 1, size_data):
        if data[i]['time_line'] != fix_time:
            break
        if data[i]['victim_player'] == fix_victim:
            set_G[data[i]['attacking_player']] = 1

    for i in range(now_id + 1, size_data):
        if data[i]['time_line'] != fix_time:
            break
        if set_G[data[i]['attacking_player']] == 1 and data[i]['victim_player'] != fix_victim:
            return
        if set_G[data[i]['victim_player']] == 1 and data[i]['attacking_player'] != fix_victim:
            return
        if data[i]['attacking_player'] == fix_victim and set_G[data[i]['victim_player']] != 1:
            return

    for i in range(now_id - 1, -1, -1):
        if (fix_time - data[i]['time_line']) >= good_time:
            break
        if set_G[data[i]['attacking_player']] == 1 and data[i]['victim_player'] != fix_victim:
            return
        if set_G[data[i]['victim_player']] == 1 and data[i]['attacking_player'] != fix_victim:
            return
        if data[i]['attacking_player'] == fix_victim and set_G[data[i]['victim_player']] != 1:
            return

    for i in range(1, 11):
        result[i] += set_G[i]

    return


with open("input.txt", "r") as inp, open("output.txt", "w") as out:
    n, t = map(int, inp.readline().split())
    data = []
    result = [-1] + [0] * 10

    for _ in range(n):
        a, b, c, d = map(int, inp.readline().split())
        data.append({'time_line': a, 'attacking_player': b, 'victim_player': c, 'result_line': d})

    for id_line in range(n):
        if data[id_line]['result_line'] == 1:
            check(id_line, data, n, t)

    out.write(' '.join(map(str, result[1:])))
