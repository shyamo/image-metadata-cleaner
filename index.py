import os
import sys
import imghdr

from exif import Image
from PIL import Image
from PIL.ExifTags import TAGS

ERR_NO_FOLDER_PROVIDED = "please provide folder with image(s) as a parameter"

def check_folder_provided():
    if len(sys.argv) > 1:
        return True

def remove_image_metadata():
    print('Processing...\n')
    image_folder = sys.argv[1]

    try:
        for file in os.listdir(image_folder):

            if imghdr.what(file, None):
                image = Image.open(file)
                image.convert('RGB')
                exif_data = image.getexif()

                for tagid in exif_data:
                    tagname = TAGS.get(tagid, tagid)
                    value = exif_data.get(tagid)
                    print(f"{file:50} {tagname:25} {value}")

                formatted_filename = "f_" + str(file)
                data = list(image.getdata())

                if image.mode in ("RGBA", "P"): image = image.convert("RGB")
                cleaned_image = Image.new(image.mode, image.size)
                cleaned_image.putdata(data)
                cleaned_image.save(formatted_filename)
    except NameError:
        print('error: ' + NameError)
    else:
        print('Process completed without errors')

def process_images():
    if check_folder_provided():
        remove_image_metadata()
    else:
        print('\n' + ERR_NO_FOLDER_PROVIDED + '\n')

process_images()
