import json
import sys
import argparse
from datetime import datetime


# Load the JSON data
with open('structure.json') as f:
    data = json.load(f)

# Function to print the directory contents
def print_ls(contents, show_all=False, long_format=False, reverse=False,sort_by_time=False):
    items = [item for item in contents if show_all or not item['name'].startswith('.')]
    if sort_by_time:
        items = sorted(items, key=lambda x: x['time_modified'], reverse=reverse)
    elif reverse:
        items = items[::-1]

    for item in items:
        if long_format:
            time_modified = datetime.fromtimestamp(item['time_modified']).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{item['permissions']} {item['size']} {item['name']}")
        else:
            print(item['name'], end=' ')
    if not long_format:
        print()

#Argument parser
parser = argparse.ArgumentParser(description='A simple implementation of ls command in Python')
parser.add_argument('-A', action='store_true', help='do not ignore entries starting with .')
parser.add_argument('-l', action='store_true', help='use a long listing format')
parser.add_argument('-r', action='store_true', help='reverse order while sorting')
parser.add_argument('-t', action='store_true', help='sort by time modified')
args = parser.parse_args()

# Get the top-level contents
top_level_contents = data['contents']

# Print the top-level contents
print_ls(top_level_contents, show_all=args.A, long_format=args.l, reverse=args.r, sort_by_time=args.t)
