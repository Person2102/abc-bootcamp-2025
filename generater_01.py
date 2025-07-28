def generate_numbers_1(max_number: int):
    print("Called generater_numbers_1 function")
    numbers = []
    for i in range(1, max_number+1):
        numbers.append(i)
    return numbers

# Generater 객체를 생성하는 함수
def generate_numbers_2(max_number: int):
    print("Called generater_numbers_2 function")
    for i in range(1, max_number+1):
        yield i

numbers_1 = generate_numbers_1(10)
numbers_2 = generate_numbers_2(10)
print(numbers_1)
print(numbers_2)

# gen1 = (i**2 for i in [1, 2, 3, 4, 5])

# def make_number():
#     for i in [1, 2, 3, 4, 5]:
#         yield i

# gen2 = make_number()