import get_price

S = int(input('할인율은? '))
aresult = get_price.get_fixed_price(S, int(input('A 상품의 할인된 가격은? ')))
bresult = get_price.get_fixed_price(S, int(input('B 상품의 할인된 가격은? ')))
print('A 상품의 정가는',aresult,'원')
print('B 상품의 정가는',bresult,'원')
