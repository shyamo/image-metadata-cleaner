import os
import sys
import imghdr

from exif import Image
from PIL import Image
from PIL.ExifTags import TAGS

ERR_NO_FOLDER_PROVIDED = "WARNING: please provide folder with image(s) as a parameter. e.g. python index.py <ABSOLUTE_PATH_TO_FOLDER>"
ERR_INVALID_FILE = "WARNING: Not an image: "
SUCCESS_MSG = "\nProcess completed without errors."

def check_folder_provided():
    if len(sys.argv) > 1:
        return True

def remove_image_metadata():
    print('Processing...\n')
    image_folder = sys.argv[1]
    counter = 0
    try:
        image_absolute_path_arr = [item for item in (os.path.join(image_folder, folder) for folder in os.listdir(image_folder)) 
            if os.path.isfile(item)]

        for file in image_absolute_path_arr:
            filename = os.path.basename(file)

            if imghdr.what(filename, None):
                image = Image.open(filename)
                image.convert('RGB')
                exif_data = image.getexif()

                for tagid in exif_data:
                    tagname = TAGS.get(tagid, tagid)
                    value = exif_data.get(tagid)
                    print(f"{filename:50} {tagname:25} {value}")

                formatted_filename = "f_" + str(filename)
                data = list(image.getdata())

                split_filename = os.path.splitext(filename)
                file_extension = split_filename[1]

                if image.mode in ("RGBA", "P") and file_extension != '.png':
                    image = image.convert("RGB")
                cleaned_image = Image.new(image.mode, image.size)
                cleaned_image.putdata(data)
                cleaned_image.save(formatted_filename)
                counter += 1
            else:
                print(ERR_INVALID_FILE + filename)
    except NameError:
        print('error: ' + NameError)
    else:
        PROCESS_COUNT = " Processed " +  str(counter) + " file(s)."
        print(SUCCESS_MSG + PROCESS_COUNT)

def process_images():
    if check_folder_provided():
        remove_image_metadata()
    else:
        print('\n' + ERR_NO_FOLDER_PROVIDED + '\n')

process_images()
