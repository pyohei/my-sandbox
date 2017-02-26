import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
vision_client = vision.Client()

# The name of the image file to annotate
file_name = os.path.join('r.png')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content)

# Performs label detection on the image file
labels = image.detect_labels()

#print('Labels:')
#for label in labels:
#    print(label.description)

texts = image.detect_text()
print('Texts:')
for text in texts:
    print(text.description)

