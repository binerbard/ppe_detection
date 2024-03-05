import argparse
import cv2
from source.model_detection import object_detection
from source.video import video_source
from source.image import image_source

# Inisialisasi argumen baris perintah
parser = argparse.ArgumentParser(description='Process some files.')

# Tambahkan argumen media
parser.add_argument('--media', type=str, help='Type of media video/image', required=True)

# Tambahkan argumen src
parser.add_argument('--src', type=str, help='Source file', required=True)

# Parsing argumen dari baris perintah
args = parser.parse_args()

# Akses nilai argumen yang diberikan
media_type = args.media
source_file = args.src

if(media_type == "video"):
    video_source(source_file)

if(media_type == "image"):
    image_source(source_file)


# Lakukan sesuatu dengan argumen yang diberikan
print("Media type:", media_type)
print("Source file:", source_file)
