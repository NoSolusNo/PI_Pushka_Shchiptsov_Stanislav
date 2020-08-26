import os

file_path = "./for_dz_8(9)"


def get_filename_and_folder_path(file_path):
    path_to_file = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    return file_name, path_to_file


def get_files_from_folder(folder_path="./"):
    folder_list = os.listdir(folder_path)
    files_folder_list = []
    for file in folder_list:
        if os.path.isfile(os.path.join(folder_path, file)):
            files_folder_list.append(file)
    return files_folder_list


def get_foldres_from_folder(folder_path="./"):
    folder_list = os.listdir(folder_path)
    folders_folder_list = []
    for file in folder_list:
        if not os.path.isfile(os.path.join(folder_path, file)):
            folders_folder_list.append(file)
    return folders_folder_list


def get_path_dict(folder_path="./"):
    path_dict = {
        "files": get_files_from_folder(folder_path=folder_path),
        "folders": get_foldres_from_folder(folder_path=folder_path)
    }
    return path_dict


def create_folders(folder_path="./"):
    folders_for_create = get_foldres_from_folder(folder_path=folder_path)
    if not len(folders_for_create):
        os.mkdir(os.path.join(folder_path, "tmp"))
    else:
        for folder in folders_for_create:
            new_folder = folder+"_tmp"
            os.mkdir(os.path.join(folder_path, new_folder))

filename, folder_path = get_filename_and_folder_path(file_path)
files = get_files_from_folder(file_path)
folders = get_foldres_from_folder(file_path)
files_dict = get_path_dict(file_path)
create_folders(file_path)
print(files)
print(folders)
print(files_dict)
