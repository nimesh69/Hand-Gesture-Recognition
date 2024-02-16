# import os
# import numpy as np
# import matplotlib.pyplot as plt

# def mirror_arrays_in_folder(input_folder, direction='horizontal'):
#     # Get the name of the input folder
#     input_folder_name = os.path.basename(input_folder)

#     c = int(input_folder_name) + 50
#     # Create the output folder in the same location as the input folder
#     output_folder = os.path.join(os.path.dirname(input_folder), str(c))
    
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Get a list of all .npy files in the input folder
#     npy_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.npy')]

#     # Mirror each .npy file in the input folder
#     for npy_file in npy_files:
#         # Build the input and output paths
#         input_path = os.path.join(input_folder, npy_file)
#         output_path = os.path.join(output_folder, npy_file)

#         # Load the numpy array
#         array = np.load(input_path)

#         # Mirror the array horizontally or vertically
#         if direction == 'horizontal':
#             if len(array.shape) == 1:
#                 mirrored_array = np.flip(array)
#             elif len(array.shape) == 2:
#                 mirrored_array = np.fliplr(array)
#             else:
#                 print("Invalid array shape. Please use 1D or 2D arrays.")
#                 return
#         elif direction == 'vertical':
#             if len(array.shape) == 1:
#                 mirrored_array = np.flip(array)
#             elif len(array.shape) == 2:
#                 mirrored_array = np.flipud(array)
#             else:
#                 print("Invalid array shape. Please use 1D or 2D arrays.")
#                 return
#         else:
#             print("Invalid direction. Please use 'horizontal' or 'vertical'.")
#             return

#         # Save the mirrored array
#         np.save(output_path, mirrored_array)
#         print(f"Mirrored array saved to {output_path}")

#         # Plot the original and mirrored arrays
#         fig, axs = plt.subplots(1, 2, figsize=(10, 5))
#         axs[0].imshow(array, cmap='gray')
#         axs[0].set_title('Original Array')
#         axs[1].imshow(mirrored_array, cmap='gray')
#         axs[1].set_title('Mirrored Array')
#         plt.show()

# def extract_folder_paths(base_folder):
#     folder_paths = []
    
#     # Walk through the directory and get all folder paths
#     for folder_name, _, _ in os.walk(base_folder):
#         folder_paths.append(folder_name)
    
#     return folder_paths

# # Example usage: Extract all folder paths in a given folder
# base_folder = r'D:\Hand Gesture Recognition\Frame_Data\Eklopan'

# all_folders = extract_folder_paths(base_folder)

# # Mirror .npy files in each folder
# for folder_path in all_folders:
#     input_folder_name = os.path.basename(folder_path)
#     if input_folder_name.isdigit():
#         print(input_folder_name)
#         mirror_arrays_in_folder(folder_path, direction='horizontal')



import os
import numpy as np
import matplotlib.pyplot as plt

def mirror_arrays_in_folder(input_folder, direction='horizontal'):
    # Get the name of the input folder
    input_folder_name = os.path.basename(input_folder)

    c = int(input_folder_name) + 50
    # Create the output folder in the same location as the input folder
    output_folder = os.path.join(os.path.dirname(input_folder), str(c))
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all .npy files in the input folder
    npy_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.npy')]

    # Mirror each .npy file in the input folder
    for npy_file in npy_files:
        # Build the input and output paths
        input_path = os.path.join(input_folder, npy_file)
        output_path = os.path.join(output_folder, npy_file)

        # Load the numpy array
        array = np.load(input_path)

        # Mirror the array horizontally or vertically
        if direction == 'horizontal':
            mirrored_array = np.flip(array)
        elif direction == 'vertical':
            mirrored_array = np.flipud(array)
        else:
            print("Invalid direction. Please use 'horizontal' or 'vertical'.")
            return

        # Save the mirrored array
        np.save(output_path, mirrored_array)
        print(f"Mirrored array saved to {output_path}")

        # Plot the original and mirrored arrays
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        if array.ndim == 1:  # If 1D array
            axs[0].plot(array, color='black')
            axs[0].set_title('Original Array')
            axs[1].plot(mirrored_array, color='black')
            axs[1].set_title('Mirrored Array')
        elif array.ndim == 2:  # If 2D array
            axs[0].imshow(array, cmap='gray')
            axs[0].set_title('Original Array')
            axs[1].imshow(mirrored_array, cmap='gray')
            axs[1].set_title('Mirrored Array')
        else:
            print("Invalid array shape. Please use 1D or 2D arrays.")
            return

        plt.show()

def extract_folder_paths(base_folder):
    folder_paths = []
    
    # Walk through the directory and get all folder paths
    for folder_name, _, _ in os.walk(base_folder):
        folder_paths.append(folder_name)
    
    return folder_paths

# Example usage: Extract all folder paths in a given folder
base_folder = r'D:\Hand Gesture Recognition\Frame_Data\Eklopan'

all_folders = extract_folder_paths(base_folder)

# Mirror .npy files in each folder
for folder_path in all_folders:
    input_folder_name = os.path.basename(folder_path)
    if input_folder_name.isdigit():
        print(input_folder_name)
        mirror_arrays_in_folder(folder_path, direction='horizontal')
