import json

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

# Get the top-level contents
top_level_contents = data['contents']

# Print the top-level contents
print_ls(top_level_contents)
