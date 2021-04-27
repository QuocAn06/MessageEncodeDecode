def print_full_name(first, last):
    # Write your code here
    result = f"Hello {first} {last}! You just delved into python."
    return result
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)