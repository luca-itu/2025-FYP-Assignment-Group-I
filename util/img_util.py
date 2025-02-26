import random
import os
import cv2


def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False


class ImageDataLoader:
    def __init__(self, directory, shuffle=False, transform=None):
        self.directory = directory
        self.shuffle = shuffle
        self.transform = transform

        # get a sorted list of all files in the directory
        # fill in with your own code below

        self.file_list = sorted([os.path.join(self.directory, file)
                         for file in os.listdir(self.directory)
                         if file.endswith(('.png', '.jpg', '.jpeg'))])

        #handling empty dictionaries
        if not self.file_list:
            raise ValueError("No image files found in the directory.")

        # shuffle file list if required (the list will be randomized)
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of batches (images)
        self.num_batches = len(self.file_list)

        if not self.file_list:
            raise ValueError("No image files found in the directory.")

        # shuffle file list if required
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of batches
        self.num_batches = len(self.file_list)

    def __len__(self):
        return self.num_batches

    def __iter__(self):
        # fill in with your own code below

            for file_path in self.file_list:
                from PIL import Image
                image = Image.open(file_path)  # Open the image

                if self.transform:
                    image = self.transform(image)  # Apply transformations (like resizing or converting to tensors)

                yield image  # Yield the processed image
