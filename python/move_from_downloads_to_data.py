import os

os.chdir("/Users/albinjonfelt/Documents/programmering/aktier/python/")
download_folder = "/Users/albinjonfelt/Downloads"
data_path = os.path.join(os.path.dirname(os.getcwd()), 'data')
entire_download_contents = os.listdir(download_folder)

clean_files = list()
for file_name in entire_download_contents:
    if ("OMXSTO" in file_name or "BATS" in file_name) and ".csv" in file_name:
        clean_files.append(file_name)

for file_name in clean_files:
    os.replace(os.path.join(download_folder, file_name), os.path.join(data_path, file_name))
