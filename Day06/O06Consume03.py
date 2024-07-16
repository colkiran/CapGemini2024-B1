
import sys

sys.path.append("C:\\Delhi")

for pth in sys.path:
    print(pth)

print("-" * 60)
import gurgaon.mymodule as m
from gurgaon.mymodule import greet
m.greet("Mbappe")
greet("Zaltan")