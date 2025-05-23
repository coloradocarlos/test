
def fizz_buzz(max: int):
    """Implementation of the famous drinking game FizzBuzz"""
    for i in range(1, max + 1):
        emit_fizz_or_buzz = False
        if i % 3 == 0:
            print("Fizz", end='')
            emit_fizz_or_buzz = True

        if i % 5 == 0:
            print("Buzz", end='')
            emit_fizz_or_buzz = True

        if emit_fizz_or_buzz is True:
            print("")
        else:
            print(i)


if __name__ == '__main__':
    fizz_buzz(30)
