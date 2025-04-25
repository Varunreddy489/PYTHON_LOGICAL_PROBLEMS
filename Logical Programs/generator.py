def even_numbers(limit):
    for i in range(0, limit, 2):
        yield i


evens = even_numbers(10)
print(list(evens))
