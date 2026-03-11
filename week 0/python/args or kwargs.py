def add(*args):
    return sum(args)


def avg(*nums):
    return sum(nums)/len(nums)

#print(avg(1,2, 3))


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")