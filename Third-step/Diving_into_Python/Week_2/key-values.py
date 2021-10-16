import argparse, json, os, tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
parser = argparse.ArgumentParser(description='key-values')
parser.add_argument('--key', type=str, default='', help='provide a key')
parser.add_argument('--val', type=str, default='', help='provide a value')
my_arguments = parser.parse_args()
with open(storage_path, 'r') as f:
    if f.readlines():
        f.seek(0)
        dictionary = json.load(f)
    else:
        dictionary = {}
if my_arguments.val:
    with open(storage_path, 'w') as f:
        dictionary[my_arguments.key] = dictionary.get(my_arguments.key, []) + [my_arguments.val]
        json.dump(dictionary, f)
elif my_arguments.key in dictionary:
    print(', '.join(dictionary[my_arguments.key]))
else:
    print()

