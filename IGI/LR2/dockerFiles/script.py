import os

import square 
import circle
  

side = float(os.environ.get('SIDE'))
radius = float(os.environ.get('RADIUS'))

print(f'Circle area :{circle.area(radius)}\n')
print(f'Square area :{square.area(side)}\n')
print(f'Circle perimeter :{circle.perimeter(radius)}\n')
print(f'Square perimeter :{square.perimeter(side)}\n')