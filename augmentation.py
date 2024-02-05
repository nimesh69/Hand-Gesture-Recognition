# from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
# import numpy as np
# import os

# # Create a new directory for saving the transformed images
# preview_directory = 'preview'
# if not os.path.exists(preview_directory):
#     os.makedirs(preview_directory)
#     print(f"Directory '{preview_directory}' created successfully.")
# else:
#     print(f"Directory '{preview_directory}' already exists.")

# # # Define the transformations for data augmentation
# datagen = ImageDataGenerator(
#     rotation_range=20,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True,
#     fill_mode='nearest'
# )
# # # DATA_PATH = os.path.join('Frame_Data')
# IMAGES_PATH= os.path.join('D:\Data collection\Frame_Collection')
# # #action that we are creating and detect
# actions = np.array(['Ambulance'])

# # #thirty videos worth of data
# no_sequences = 50

# # #videos are going to be 60 frames in length
# sequence_length = 60

# # # Load an image from file and perform data augmentation
# # for action in actions:
# #     for sequence in range(no_sequences):
# #         for frame_num in range(sequence_length):
# #             img_path = os.path.join(IMAGES_PATH, action, str(sequence), "{}.jpg".format(frame_num))
# #             img = load_img(img_path)

# #             # Convert the image to a Numpy array
# #             x = img_to_array(img)

# #             # Reshape the array to have a batch dimension
# #             x = x.reshape((1,) + x.shape)

# #             # Apply data augmentation and save the transformed images to the 'preview' directory
# #             i = 0
# #             for batch in datagen.flow(x, batch_size=1, save_to_dir=preview_directory, save_prefix='i', save_format='jpg'):
# #                 i += 1
# #                 if i > 10:
# #                     break

# # Generate augmented data
# # DATA_PATH = os.path.join('Frame_Data')
# # IMAGES_PATH= os.path.join('Frame_collection')
# # #action that we are creating and detect
# # actions = np.array(['Aausadi','Eklopan','Firstaid','Need','Sign','Sorry'])

# # #thirty videos worth of data
# # no_sequences = 50

# # #videos are going to be 60 frames in length
# # sequence_length = 60
# # augmented_data = []
# # for action in actions:
# #     for sequence in range(no_sequences):
# #         for frame_num in range(sequence_length):
# #             img_path = os.path.join(IMAGES_PATH, action, str(sequence), "{}.npy".format(frame_num))
# #             img = np.load(img_path)
# #             img = np.expand_dims(img, axis=0)  # Expand dimensions to make it compatible with flow method
# #             # Generate augmented images
# #             augmented_images = datagen.flow(img, batch_size=1)
# #             for augmented_image in augmented_images:
# #                 augmented_data.append(augmented_image[0])




# # Load an image from file and perform data augmentation
# # Load an image from file and perform data augmentation
# # Load an image from file and perform data augmentation
# for action in actions:
#     for sequence in range(no_sequences):
#         # Create a directory for each sequence
#         sequence_directory = os.path.join(preview_directory, action, str(sequence))
#         if not os.path.exists(sequence_directory):
#             os.makedirs(sequence_directory)

#         # Generate 10 variations for each frame in the sequence
#         for folder_index in range(10):
#             # Create a directory for each variation
#             variation_directory = os.path.join(sequence_directory, f'variation_{folder_index}')
#             if not os.path.exists(variation_directory):
#                 os.makedirs(variation_directory)

#             for frame_num in range(sequence_length):
#                 img_path = os.path.join(IMAGES_PATH, action, str(sequence), "{}.jpg".format(frame_num))
#                 img = load_img(img_path)

#                 # Convert the image to a Numpy array
#                 x = img_to_array(img)

#                 # Reshape the array to have a batch dimension
#                 x = x.reshape((1,) + x.shape)

#                 # Apply data augmentation and save the transformed images to the variation directory
#                 i = 0
#                 for batch in datagen.flow(x, batch_size=1, save_to_dir=variation_directory, save_prefix=f'frame_{frame_num}_', save_format='jpg'):
#                     i += 1
#                     if i >= 10:  # Generate 10 variations per frame
#                         break


from PIL import Image
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

def rotateimages_in_folder(input_folder, datagen, batch_size=1):
    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg'))]
    input_folder_name = os.path.basename(input_folder)

    # Create a separate folder for the augmented images
    output_folder = os.path.join(input_folder, f'{input_folder_name}_rotated_30')
    os.makedirs(output_folder, exist_ok=True)

    # Rotate each image in the input folder
    for image_file in image_files:
        # Open the image file
        input_path = os.path.join(input_folder, image_file)
        image = Image.open(input_path)
        
        # Convert the PIL image to a numpy array
        img_array = np.array(image)
        img_array = img_array.reshape((1,) + img_array.shape)

        # Generate augmented images with rotation by 30 degrees
        for batch in datagen.flow(img_array, batch_size=batch_size, save_to_dir=output_folder, save_prefix='aug', save_format='jpg'):
            break  # Break the loop to prevent generating more images

# Example usage
input_folder_path = r'D:\Ambulance\0'

# Create an instance of ImageDataGenerator with rotation by 30 degrees
datagen = ImageDataGenerator(
    # rotation_range=30,
    horizontal_flip=True,
    fill_mode='nearest'
)

rotateimages_in_folder(input_folder_path, datagen, batch_size=5)
