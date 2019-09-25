import os


########################################################################
def list_files_in_folder(folder, format='xml'):
    """
    list_of_files = list_files_in_folder(folder="furg_fire_dataset", format='xml')
    """
    list_of_files = []
    files_name = []

    for file in os.listdir(folder):
        if file.endswith(format):
            list_of_files.append(os.path.join(folder, file))
            files_name.append(file)
    return list_of_files, files_name


########################################################################
folderImages = "build/darknet/x64/data/obj/"

list_of_images, images_name = list_files_in_folder(folderImages, 'jpg')

path_all_images = folderImages + "train.txt"
print(path_all_images)
txt_file = open(path_all_images, 'w')

for image_name in images_name:
    imagePath = "data/obj/" + image_name
    txt_file.write(imagePath + '\n')

txt_file.close()
print("[INFO] Done !")
# ########################################################################
# folderImages = "validation/annotations/"
# list_of_annotations, txt_files_name = list_files_in_folder(folderImages, 'txt')

# path_all_images = folderImages + "path_of_all_annotations.txt"
# txt_file = open(path_all_images, 'w')

# for txt_file in txt_files_name:

#     # bbox = lire   1 ligne of txt

#     for line in txt_file:
#             [frameNumber, x_center, y_center, w, h] = [
#                 float(v) for v in line.strip().split()]

#     txt_file.write(bbox + '\n')

# txt_file.close()

# ########################################################################
