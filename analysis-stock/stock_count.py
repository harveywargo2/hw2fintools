import os

script_path = os.path.dirname(os.path.abspath(__file__))

base_depth = script_path.count(os.sep)

count = 0

for root, dirs, files in os.walk(script_path):
    current_depth = root.count(os.sep) - base_depth

    if current_depth == 0:
        count = len(dirs)
        dirs_fin = dirs

print(dirs_fin)
print(count)