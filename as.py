import os
from PIL import Image

# Define input and output directories
input_dir = r'E:\Frame Collection'
output_dir = r'E:\Resized Collection'

# Define target dimensions for resizing
target_width = 320
target_height = 250

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over each word folder
for word_folder in os.listdir(input_dir):
    word_folder_path = os.path.join(input_dir, word_folder)
    if os.path.isdir(word_folder_path):
        # Create a directory in the output folder for the current word
        word_output_dir = os.path.join(output_dir, word_folder)
        if not os.path.exists(word_output_dir):
            os.makedirs(word_output_dir)

        # Iterate over each video folder inside the current word folder
        for video_folder in os.listdir(word_folder_path):
            video_folder_path = os.path.join(word_folder_path, video_folder)
            if os.path.isdir(video_folder_path):
                # Create a directory in the output folder for the current video
                video_output_dir = os.path.join(word_output_dir, video_folder)
                if not os.path.exists(video_output_dir):
                    os.makedirs(video_output_dir)

                # Iterate over each image file inside the current video folder
                for file in os.listdir(video_folder_path):
                    if file.endswith('.jpg'):  # Adjust file extension as needed
                        # Load the image
                        img_path = os.path.join(video_folder_path, file)
                        img = Image.open(img_path)

                        # Resize the image
                        img_resized = img.resize((target_width, target_height), Image.ANTIALIAS)

                        # Define the output file path
                        output_file = os.path.join(video_output_dir, file)

                        # Save the resized image
                        img_resized.save(output_file)

print("Resizing complete.")
