def paint_fill(x, y, old_color, new_color, image):
    if image[y][x] == old_color:
        image[y][x] = new_color
    if x + 1 < len(image[0]) and image[y][x + 1] == old_color:
    	paint_fill(x + 1, y, old_color, new_color, image)
    if x - 1 >= 0 and image[y][x - 1] == old_color:
        paint_fill(x - 1, y, old_color, new_color, image)
    if y + 1 < len(image) and image[y + 1][x] == old_color:
        paint_fill(x, y + 1, old_color, new_color, image)
    if y - 1 >= 0 and image[y - 1][x] == old_color:
        paint_fill(x, y - 1, old_color, new_color, image)
    return image


def get_color(x, y, image):
    return image[y][x]

def main():
    image = [ [1, 0, 1],
              [1, 0, 0],
              [1, 0, 0] ]
    old_color = get_color(1, 1, image)
    image = paint_fill(1, 1, old_color, 2, image) 
    for row in image:
        line = ""
        for item in row:
            line += str(item)
        print line  

main()
