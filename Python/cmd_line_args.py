"""
Purpose: Processing comand line arguments using python
Date: 03/01/2024
Author: Lyra "Archivist" Hawkins
"""

# Processing command line arguments in python has a few options available:
# You can use:
# sys.argv - raw list of arguments passed to the py interpreter
# argparse - standard package for arg parsing
# fileinput.input() 
# docopt
# click

import sys
print(type(sys.argv))
print(sys.argv)

# when runing from the cmd line now, the above will return a list of whatever
# is parsed after the file call
# python cmd_line_args.py --a -b c d
# Returns:
# <class list>
# ['cmd_line_args.py','--a','-b','c','d']

# Check if your first argument is --help

if len(sys.argv) == 2 and sys.argv[1] == '--help':
    print('Help initialised')

# To check, run this code with the cmd function:
# >> python cmd_line_args.py --help

"""
If you want a higher level interface to the arguments aside from directly accessing the sys.argv list,
you can use Python's standard library package argparse.

Argparse allows for many things:

    Required or optional arguments
    Automatic -h/--help option with usage instructions
    Multiple versions of flags, e.g. short and long flags (-h/--help)
    Type checking
    Required argument checking

Check out: 'https://peps.python.org/pep-0389/' for more info

class argparse.ArgumentParser(
    prog=None, usage=None, description=None, epilog=None,
    parents=[], formatter_class=argparse.HelpFormatter,
    prefix_chars='-', fromfile_prefix_chars=None,
    argument_default=None, conflict_handler='error',
    add_help=True, allow_abbrev=True)

"""

import argparse

# Initialize a default arg parser
arg_parser = argparse.ArgumentParser()

# Simple optional argument. Example usage `--filename test.txt`
arg_parser.add_argument('--filename')
# Boolean, true or false (exists or not)
arg_parser.add_argument('--turbo', action='store_true')
# Multiple variations
arg_parser.add_argument('--verbose', '-v', action='store_true')
# With help text
arg_parser.add_argument('--debug', help='Raise log levels to debug', action='store_true')
# Required arguments
arg_parser.add_argument('--run', required=True, action='store_true')
# Arg with default provided
arg_parser.add_argument('--user', default='anonymous')
# Multiple arguments. Example usage `--numbers 2 4 6 8 10`
arg_parser.add_argument('--numbers', metavar='num', type=int, nargs='+', help='Provide a list of numbers')

# Now that the arg parser knows what arguments to look for,
# parse all the command line arguments in to a convenient object
arguments = arg_parser.parse_args()

print(type(arguments))  # <class 'argparse.Namespace'>
print(arguments)
print(arguments.filename)
print(arguments.turbo)
print(arguments.verbose)
print(arguments.debug)
print(arguments.run)
print(arguments.user)
print(arguments.numbers)