# # # import os

# # # # Folder path jisme files hain
# # # folder_path = input("Enter the folder path: ")

# # # # Check karein agar folder exists karta hai
# # # if not os.path.exists(folder_path):
# # #     print("Error: Folder does not exist!")
# # #     exit()

# # # # New file naming pattern
# # # prefix = input("Enter a prefix for the new filenames: ")  # Example: "Project_"
# # # extension = input("Enter the file extension to rename (e.g., .txt, .jpg, .pdf, etc.): ")

# # # # Folder ke andar saari files ko rename karein
# # # for count, filename in enumerate(os.listdir(folder_path), start=1):
# # #     file_ext = os.path.splitext(filename)[1]  # Get file extension
# # #     if file_ext.lower() == extension.lower():
# # #         new_name = f"{prefix}{count}{file_ext}"
# # #         old_path = os.path.join(folder_path, filename)
# # #         new_path = os.path.join(folder_path, new_name)

# # #         os.rename(old_path, new_path)
# # #         print(f"Renamed: {filename} → {new_name}")

# # # print("✅ Bulk renaming complete!")

# # # --------------------------------------------------------------------

# # import os

# # folder_path = input("📂 Enter the full folder path: ").strip()

# # if not os.path.exists(folder_path):
# #     print("❌ Error: Folder does not exist!")
# #     exit()

# # prefix = input("📝 Enter a prefix for the new filenames: ").strip()
# # extension = input("🔍 Enter the file extension (e.g., .txt, .jpg, .pdf): ").strip().lower()

# # # Safe renaming with error handling
# # count = 1
# # for filename in os.listdir(folder_path):
# #     file_path = os.path.join(folder_path, filename)

# #     # Skip if it's not a file
# #     if not os.path.isfile(file_path):
# #         continue

# #     # Check if extension matches
# #     _, file_ext = os.path.splitext(filename)
# #     if file_ext.lower() != extension:
# #         continue

# #     new_name = f"{prefix}{count}{file_ext}"
# #     new_path = os.path.join(folder_path, new_name)

# #     try:
# #         os.rename(file_path, new_path)
# #         print(f"✅ Renamed: {filename} → {new_name}")
# #         count += 1
# #     except PermissionError:
# #         print(f"🚫 Permission denied: {filename}")
# #     except FileNotFoundError:
# #         print(f"⚠️ File not found (maybe already moved?): {filename}")
# #     except Exception as e:
# #         print(f"❌ Error renaming {filename}: {e}")

# # print("🎉 Bulk renaming complete!")


# import os

# folder_path = input("📂 Enter the full folder path: ").strip()

# # Check if the folder exists
# if not os.path.exists(folder_path):
#     print("❌ Error: Folder does not exist!")
#     exit()

# prefix = input("📝 Enter a prefix for the new filenames: ").strip()
# extension = input("🔍 Enter the file extension (e.g., .txt, .jpg, .pdf): ").strip().lower()

# # Safe renaming with error handling
# count = 1
# for filename in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, filename)

#     # Skip if it's not a file
#     if not os.path.isfile(file_path):
#         continue

#     # Check the extension of the file
#     _, file_ext = os.path.splitext(filename)
#     print(f"🔍 Found file: {filename} (Extension: {file_ext})")  # Debugging line

#     # Check if the file extension matches
#     if file_ext.lower() == extension:
#         new_name = f"{prefix}{count}{file_ext}"
#         new_path = os.path.join(folder_path, new_name)

#         # Debugging line to see the old and new paths
#         print(f"🔧 Renaming: {file_path} → {new_path}")  # Debugging line

#         try:
#             os.rename(file_path, new_path)
#             print(f"✅ Renamed: {filename} → {new_name}")
#             count += 1
#         except PermissionError:
#             print(f"🚫 Permission denied: {filename}")
#         except FileNotFoundError:
#             print(f"⚠️ File not found (maybe already moved?): {filename}")
#         except Exception as e:
#             print(f"❌ Error renaming {filename}: {e}")
#     else:
#         print(f"⚠️ Skipping {filename} (does not match the extension)")

# print("🎉 Bulk renaming complete!")


import os

def rename_files(folder_path, prefix, file_extension):
    # If the folder_path is a file, process that file directly
    if os.path.isfile(folder_path):
        files_to_rename = [folder_path]
    else:
        # If it's a directory, get all files with the specified extension
        files_to_rename = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(file_extension)]

    # Renaming files
    for count, file_path in enumerate(files_to_rename, start=1):
        if os.path.isfile(file_path):
            directory, filename = os.path.split(file_path)
            new_name = f"{prefix}{count}{file_extension}"
            new_path = os.path.join(directory, new_name)
            
            print(f"🔧 Renaming: {file_path} → {new_path}")
            os.rename(file_path, new_path)
            print(f"✅ Renamed: {filename} → {new_name}")
    print("🎉 Bulk renaming complete!")

# Get user input
folder_path = input("📂 Enter the full folder path (or file path): ").strip()
prefix = input("📝 Enter a prefix for the new filenames: ").strip()
file_extension = input("🔍 Enter the file extension (e.g., .txt, .jpg, .pdf): ").strip()

rename_files(folder_path, prefix, file_extension)
