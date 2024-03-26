def exchange(M):
    n500= M // 500
    n100= (M % 500)//100
    n50= ((M % 500)% 100)//50
    n10= (((M % 500)% 100)% 50)//10
    print('500원 동전의 개수: ', n500)
    print('100원 동전의 개수: ', n100)
    print('50원 동전의 개수: ', n50)
    print('10원 동전의 개수: ', n10)
    


def get_integer(prompt) :
    return int(input(prompt))

M=get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(M)
