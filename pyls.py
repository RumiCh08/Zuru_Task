import json
import sys
import argparse


# Load the JSON data
with open('structure.json') as f:
    data = json.load(f)

# Function to print the directory contents
def print_ls(contents, show_all=False, long_format=False):
    for item in contents:
        if not show_all and item['name'].startswith('.'):
            continue
        if long_format:
            print(f"{item['permissions']} {item['size']} {item['name']}")
        else:
            print(item['name'], end=' ')
    if not long_format:
        print()

#Argument parser
parser = argparse.ArgumentParser(description='A simple implementation of ls command in Python')
parser.add_argument('-A', action='store_true', help='do not ignore entries starting with .')
parser.add_argument('-l', action='store_true', help='use a long listing format')
args = parser.parse_args()

# Get the top-level contents
top_level_contents = data['contents']

# Print the top-level contents
print_ls(top_level_contents, show_all=args.A, long_format=args.l)
