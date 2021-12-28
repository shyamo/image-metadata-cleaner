# Image Metadata Cleaner 
 Images contain a lot of metadata which you may not be aware of. This tool strips out all that metadata linked to the image and create a new one in the same folder.
 Please see https://www.exiftool.org/TagNames/EXIF.html for list of potential metadata that could be in your image.
 
 **Dependancies**:
 ```
  from exif import Image
  from PIL import Image
  from PIL.ExifTags import TAGS
 ```
 
 Notes:
 If you're having an issue where `PIL` package is not recognized or have multiple version of python on your machine, add an alias to your bash or `.zshrc` file referencing the python3 like below:
 ```
 alias python='/usr/local/bin/python3'
 ```
 and set your default to python 3.10.
 
 **How to run the script**
 ```
 python index.py <FOLDER_LOCATION>
 ```
 1. It will find the image files in the folder and attempt to remove EXIF data.
 2. It will list any EXIF metadata onto the console which includes, `filename`, `attribute` and `value`.
 3. A new image file is created with a prefix `f_` in the same folder.

**Disclaimer**
The purpose of this tool is to remove all EXIR metadata from your images. I am not responsible if your original images change in anyway or become corrupt or even if  metadata is not removed from the image. 
