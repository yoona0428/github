class Rectangle :
    def getPerimeter(self1, self2, self3, self4):
        result = self1.r1 + self2.r1 + self3.r1 + self4.r1
        return result
    def getArea(self1, self2, self3, self4) :
        result = (self3.r1 - self1.r1) * (self4.r1 - self2.r1)
        return result
        

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print('좌측 상단 꼭지점이 (5,5)이고, 우측 하단 꼭지점이 (20,10)인 사각형입니다.')
print(f'\n넓이는 {a}, 둘레는 {p}')
