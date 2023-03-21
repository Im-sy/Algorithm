def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    camera = -30001
    for start, end in routes:
        if start > camera:
            answer += 1
            camera = end
        # print(camera)
    return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))