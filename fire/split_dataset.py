import glob
import os
import tkinter
import tkinter.constants
import tkinter.filedialog

while True:
    print("Please select your image directory.")
    # current_dir = tkinter.filedialog.askdirectory()
    current_dir = "/media/amine/DATA/AI_lab/CV_datasets/fire-dataset/train/images"
    print("[INFO] You selected the directory: {}".format(current_dir))

    if current_dir == None or current_dir == "":
        print("You must select a directory.")
        continue
    break

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title, ext)
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1
print("[INFO] train.txt and test.txt have been created")
print(ext)
file_train.close()
file_test.close()
print("[INFO] Done!")
