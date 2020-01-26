with open('image.jpg', 'rb') as my_file:
    b = my_file.read()
    print(b)

with open('new_image.jpg', 'wb') as new_file:
    new_file.write(b)
