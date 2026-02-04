# def calculate_square_root(number):
#     assert number >= 0, 'Cannot calculate square root of negative number'
#     return number ** 0.5

# try:
#     result = calculate_square_root(-4)
# except AssertionError as e:
#     print(f'Assertion failed: {e}')

# def parse_config(filename):
#     try:
#         with open(filename, 'r') as file:
#             data = file.read()
#             return int(data)
#     except FileNotFoundError:
#         raise ValueError('Configuration file is missing') from None
#     except ValueError as e:
#         raise ValueError('Invalid configuration format') from e

# config = parse_config('config.txt')