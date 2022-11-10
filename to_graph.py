from PIL import Image
from sys import argv
import functools

width = 106
height = 17
script, scale, yOffset = argv
scale = int(scale)
yOffset = int(yOffset)


# ((y+yOffset)//17 * 2 ^ (-17*x - ((y+yOffset) % 17))) % 2
def is_formula_true(x, y):
    d = ((-17 * x) - (y % 17))
    e = functools.reduce(lambda x, y: x * y, [2 for x in range(-d)]) if d else 1
    f = ((y // 17) // e)
    g = f % 2
    return 1 / 2 < g


graph = Image.new('RGBA', (width, height))
# loop through data
for w in range(0, width):
    for h in range(0, height):
        # for s in range(0, scale):
        if is_formula_true(w, h+yOffset):
            # Set black
            graph.putpixel((w, h), (0, 0, 0, 255))
        else:
            # Set white
            graph.putpixel((w, h), (217, 199, 178, 0))

graph_corrected = graph.transpose(method=Image.FLIP_LEFT_RIGHT)
graph_corrected.save('graph.png')
