def calculate_result(number):
    result = number -25
    result = result ** 2
    result = result * -.42
    result = result + 1000
    result = result * .02
    return result

#make sure you are aware of these
ages = [random.randint(15,75) for _ in range(500)]
rates = list(map(calculate_result, ages))

agesNrates=list(zip(ages,rates))


