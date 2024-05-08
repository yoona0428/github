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

print('\n[검색]')
t = input('장바구니에서 확인하고자 하는 상품은? ')


print(f'{t}은(는) {shopping_bag.get(t)}개 담겨 있습니다.')

