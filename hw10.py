import pickle

def input_scores():
    s = []
    i = 1
    while (True):
        n = int(input(f'#{i}? '))
        if n < 0 :
            break
        s.append(n)
        i += 1
    return s

def get_average(s) :
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s :
        print(n, end='')
    print()

print('[점수 입력]')
scores = input_scores()
print('\n[점수 출력]\n개인점수: ', end ='')
show_scores(scores)
avg = get_average(scores)
print(f'평균: {avg: .1f}')


with open('score.bin', 'vb') as f:
    pickle.dump('10.3 pickle.py', f)

with open('score.bin', 'rb') as f:
    readst = pickle.load(f)

print(readst)
