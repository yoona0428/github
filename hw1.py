def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(R):
    circle=3.14*R*R
    return circle


input_r=('넓이를 구하고자 하는 원의 반지름은? ')
result=get_radius(input_r)
print("반지름", result, "인 원의 넓이= 3.14x", result, "x",result,'=', get_circle_area(result))

