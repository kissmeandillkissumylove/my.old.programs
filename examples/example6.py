from typing import Optional, Union, NoReturn, Iterable

amount: int
amount = None  # Incompatible types in assignment (expression has type "None", variable has type "int")

price: Optional[int]
price = None

unknown_item: any = '1'
print(unknown_item.startswith('hello'))
print(unknown_item)
# print(int(unknown_item) // 0)
print(type(unknown_item))


#_______________________________________________________________________


def hundreds(x: Union[int, float]) -> int:
	return (int(x) // 100) % 10

print(hundreds(100.0))
print(hundreds(100))
print(hundreds("100")) # Argument 1 to "hundreds" has incompatible type "str"; expected "Union[int, float]"


#_______________________________________________________________________


items: list = ["hello", 1]
print(items)
items = 1
price_container: tuple[int] = ('1',)
print(price_container)
book_authors: dict[str, int] = {'hhhn' : 'hhhnn'}
print(book_authors)


#_______________________________________________________________________


def forever() -> NoReturn:
    while True:
        pass


#_______________________________________________________________________


def generate_two() -> Iterable[int]:

	yield 1
	yield '2' # Incompatible types in "yield" (actual type "str", expected type "int")


