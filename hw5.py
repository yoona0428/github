def read_number(n_input) :
    if len(n_input) == 3 :
        n1 = read_single_digit(n_input[0])
        n2 = read_single_digit(n_input[1])
        n3 = read_single_digit(n_input[2])
        print(n1, n2, n3)
    elif len(n_input) == 2 :
        n1 = read_single_digit(n_input[0])
        n2 = read_single_digit(n_input[1])
        print(n1, n2)
    elif len(n_input) == 1 :
        n1 = read_single_digit(n_input[0])
        print(n1)
    


def read_single_digit(n) :
    k = int(n)
    if k == 0 :
        return '영'
    elif k == 1 :
        return '일'
    elif k == 2 :
        return '이'
    elif k == 3 :
        return '삼'
    elif k == 4 :
        return '사'
    elif k == 5 :
        return '오'
    elif k == 6 :
        return '육'
    elif k == 7 :
        return '칠'
    elif k == 8 :
        return '팔'
    else :
        return '구'
    
n_input = input('세 자리 정수 입력: ')
read_number(n_input)
