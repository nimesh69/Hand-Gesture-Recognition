import gdown

# Direct download link with the file ID
file_url = 'https://drive.google.com/uc?export=download&id=1rR1DhktE53hVUbah1R-H_qFX7owNSrz3'

# Path where the file will be saved
output_file = 'D:\Hand Gesture Recognition'  # Change this to your desired file path and name

# Download the file using gdown
gdown.download(file_url, output_file, quiet=False)
