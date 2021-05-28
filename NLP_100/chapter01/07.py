def generate_text(x, y, z):
    return f'{x}時の{y}は{z}'
x, y, z  = 12, '気温', 22.4
print(generate_text(x, y, z))