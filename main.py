
import easygui
from rembg import remove
from PIL import Image

#Select Image to remove background
input_path = easygui.fileopenbox(title="Select image.")

#Save the new picture as picture.png
output_path = easygui.filesavebox(title="Save file as .png")

inpt = Image.open(input_path)
output = remove(inpt)
output.save(output_path)