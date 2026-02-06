# Import the os module so we can work with the files and folders
import os

# The value used to count and name the invoices
num = 1
# The name of the folder containing the files
folder_path = "Dummy Data"

# Gets a list of everything inside of the folder
items = os.listdir(folder_path)

# Loops through each item within the folder
for item in items:
    # Creates the full path to the current item
    old_path = os.path.join(folder_path, item)

    # A check to see if the item is NOT a file
    if not os.path.isfile(old_path):
        print("Skipped")
        # Skips to the next item
        continue

    # Splits the file into its name and its extension
    name, ext = os.path.splitext(item)
    # Creates the new file name user the counter
    new_name = f"invoice{num}{ext}"
    # Creates the new path for the new filename
    new_path = os.path.join(folder_path, new_name)

    # Renames the file to the updated name
    os.rename(old_path, new_path)
    # Increases the counter so the next file gets a different number
    num += 1

# Prints once the loop is finished
print("Done!")