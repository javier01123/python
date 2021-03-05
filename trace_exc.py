import traceback
import sys


def sample_function(text):
    price = float(text)


try:
    sample_function('abc')
except:
    print("TRACE:")
    traceback.print_exc(file=sys.stderr)
    print('STACK:')
    traceback.print_stack(file=sys.stderr)