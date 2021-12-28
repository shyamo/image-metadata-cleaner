# image-metadata-cleaner
 Cleans EXIR metadata from an image
 
 **Dependancies**:
 ```
  from exif import Image
  from PIL import Image
  from PIL.ExifTags import TAGS
 ```
 
 **How to run the script**
 ```
 python index.py <FOLDER_LOCATION>
 ```
 1. It will find the image files in the folder and attempt to remove EXIR data.
 2. It will list any EXIR metadata onto the console which includes, `filename`, `attribute` and `value`
 3. A new image file is created with a prefix `f_` in the same folder.
