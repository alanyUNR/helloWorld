# Create a function called sayHello() that will display hello along with a
# string parameter name.
def sayHello(name: str) -> None:
    print('Hello', name)


def sayGoodbye(name: str) -> None:
    print('Goodbye', name)


def greetUser(name: str) -> str:
    message = f'Hello {name}!'
    print(message)
    return message


if __name__ == '__main__':
    sayHello('Samantha')
    sayGoodbye('Alan')
    greetUser('Class')