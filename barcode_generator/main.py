import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

user_data = input("Enter the data to encode in the barcode: ")
# This code generates a barcode based on user input and saves it as an image file.
# It uses the 'python-barcode' library to create a barcode of type 'code128'.
# The user is prompted to enter the data they want to encode in the barcode.
# The generated barcode is saved as 'barcode.png' in the current directory.
# The barcode is displayed using IPython's display function.
# Ensure you have the 'python-barcode' and 'IPython' libraries installed to run this code.

code = barcode.get('code128', user_data, writer=ImageWriter())
filename = code.save('code_barcode')

print(f"Barcode saved as {filename}.png")
# Display the generated barcode image
# display(Image(filename=f"{filename}.png"))
display(Image(filename=filename))
# Note: The above code requires the 'python-barcode' and 'IPython' libraries to be installed.