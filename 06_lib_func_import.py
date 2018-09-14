import simple

print(simple.x)

import sys
print(sys.modules['simple']) # module stored in python's cache

print(sys.path)

# sys.path.append('..)
# env PYTHONPATH=.. python3