import os

# Folder path jisme files hain
folder_path = input("Enter the folder path: ")

# Check karein agar folder exists karta hai
if not os.path.exists(folder_path):
    print("Error: Folder does not exist!")
    exit()

# New file naming pattern
prefix = input("Enter a prefix for the new filenames: ")  # Example: "Project_"
extension = input("Enter the file extension to rename (e.g., .txt, .jpg, .pdf, etc.): ")

# Folder ke andar saari files ko rename karein
for count, filename in enumerate(os.listdir(folder_path), start=1):
    file_ext = os.path.splitext(filename)[1]  # Get file extension
    if file_ext.lower() == extension.lower():
        new_name = f"{prefix}{count}{file_ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

print("✅ Bulk renaming complete!")
