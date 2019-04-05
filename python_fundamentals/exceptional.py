'''A module for demonstrating exceptions'''

import sys

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('Conversion error: {}'.format(str(e)), file=sys.stderr)
        raise

#
# def convert(s):
#     '''Convert to an integer.'''
#     x = -1
#     try:
#         x = int(s)
#         print('Conversion suceeded! x= ', x)
#     except (ValueError, TypeError):
#         print('Conversion failed!')
#     return x
