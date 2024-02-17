# from functools import wraps
import functools
import time

class Rectangle:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	@property
	def area(self):
		return self.a * self.b


# def outer(a, b):
# 	def decorator(func):
# 		# @wraps(func)
# 		def wrapper(a, b):
# 			result = func(a, b)
# 			return result
# 		return wrapper
# 	return decorator
#
#
# @outer(4, 5)
# def funcsum(a, b):
# 	print(a + b)
# 	return a + b


def retry(func):
    def _wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            time.sleep(1)
            func(*args, **kwargs)
    return _wrapper

@retry
def might_fail():
    print("might_fail")
    raise Exception


def retry1(max_retries):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    func(*args, **kwargs)
                except:
                    time.sleep(0.1)
        return _wrapper
    return retry_decorator


@retry1(5)
def might_fail1():
    print("might_fail")
    raise Exception


def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper


@timer
def complex_calculation():
    """Some complex calculation."""
    time.sleep(0.5)
    return 42


@timer
class MyClass:
    def complex_calculation(self):
        time.sleep(1)
        return 42


def decorator(func):
	def inner():
		print('start decorator...')
		func()
		print('finish decorator...')
	return inner


def say():
	print('yo')


def main():
	# print(outer(4, 5)(funcsum))

	rect = Rectangle(5, 6)
	print(rect.area)

	# might_fail()
	might_fail1()

	print(complex_calculation())
	print(complex_calculation.__module__)
	print(complex_calculation.__name__)
	print(complex_calculation.__qualname__)
	print(complex_calculation.__doc__)
	print(complex_calculation.__annotations__)

	# При декорировании класса методы этого класса не подвергаются автом
	# атическому декорированию. Проще говоря — использование обычного де
	# коратора для декорирования обычного класса приводит лишь к декорир
	# ованию конструктора (метод __init__) этого класса.
	my_obj = MyClass()
	my_obj.complex_calculation()


if __name__ == '__main__':
	main()
	say = decorator(say)
	say()