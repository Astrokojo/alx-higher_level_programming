#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if isinstance(i, int):
                print("{:d}".format(i), end='')
                count += 1
            if count >= x:
                break
    except (TypeError, ValueError):
            pass
    finally:
        print()
    if count < x:
            raise IndexError
    return count

