def solution(genres, plays):
    answer = []
    music = dict()
    sum_play = dict()
    for genre in set(genres):
        music[genre] = []
        sum_play[genre] = 0
    for i, play in enumerate(plays):
        music[genres[i]].append((i, play))
        sum_play[genres[i]] += play
    for genre in music.keys():
        music[genre].sort(key=lambda x:x[1], reverse=True)
    sum_play = dict(sorted(sum_play.items(), key=lambda x: x[1], reverse=True))
    for genre in sum_play.keys():
        for i in range(2):
            try:
                answer.append(music[genre][i][0])
            except:
                break
    # print(music, sum_play)
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))