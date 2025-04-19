import os
from PIL import Image, ImageStat

image_folder = r"C:\Users\90537\Desktop\some pics\AC'17 Tampere"
image_files = [_ for _ in os.listdir(image_folder) if _.endswith("jpg")]


duplicate_files = []

print("beginning")

for index, file_org in enumerate(image_files):
    print("image {0} of {1}".format(index, len(image_files)))
    if not file_org in duplicate_files:
        print("found file...")
        image_org = Image.open(os.path.join(image_folder, file_org))
        pix_mean1 = ImageStat.Stat(image_org).mean

        for file_check in image_files:
            image_check = Image.open(os.path.join(image_folder, file_check))
            pix_mean2 = ImageStat.Stat(image_check).mean

            if pix_mean1 == pix_mean2:
                print("found duplicate")
                duplicate_files.append(file_org)
                duplicate_files.append(file_check)

print("printing duplicates..................")
print(duplicate_files)