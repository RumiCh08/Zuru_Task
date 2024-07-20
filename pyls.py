import json
import sys
import argparse


# Load the JSON data
with open('structure.json') as f:
    data = json.load(f)

# Function to print the directory contents
def print_ls(contents, show_all=False):
    for item in contents:
        if not show_all and item['name'].startswith('.'):
            continue
        print(item['name'], end=' ')
    print()

#Argument parser
parser = argparse.ArgumentParser(description='A simple implementation of ls command in Python')
parser.add_argument('-A', action='store_true', help='do not ignore entries starting with .')
args = parser.parse_args()

# Get the top-level contents
top_level_contents = data['contents']

# Print the top-level contents
print_ls(top_level_contents, show_all=args.A)
