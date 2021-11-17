def solution(s):
    s_solution = []
    if len(s) % 2 != 0:
        s += '_'
    for i in range(0,len(s),2):
        x = s[i:i+2]
        s_solution.append(x)
    print(s_solution)
solution('helloworl')