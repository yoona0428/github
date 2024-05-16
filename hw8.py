print('[구입]')

shopping_bag = {}
while True:
    T = input('상품명? ')
    if T == '':
        break
    N = input('수량은? ')
    shopping_bag[T] = N
    print(f'장바구니에 {T} {N}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기:{shopping_bag}')

def search(dic, key) :
    if key  in dic :
        return key
    else :
        return None
    


print('\n[검색]')
t = input('장바구니에서 확인하고자 하는 상품은? ')


res = search(shopping_bag, t)

if res != None :
    print(f'{t}은(는) {shopping_bag[t]}개 담겨 있습니다.')
else :
    print(f'장바구니에 {t}은(는) 없습니다.')
