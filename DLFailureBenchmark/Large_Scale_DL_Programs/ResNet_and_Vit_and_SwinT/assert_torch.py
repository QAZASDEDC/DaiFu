import sys

# 查看sys.path中的路径
print('# 查看sys.path中的路径')
for path in sys.path:
    print(path)

import torch
import inspect

# 查看torch的源代码路径
print('# 查看torch的源代码路径')
print(inspect.getsourcefile(torch))