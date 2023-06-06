import shutil
import os


def copy_new_django_sample(sample_path, new_site_path, new_site_name):
    try:
        shutil.copytree(sample_path, os.path.join(os.path.dirname(new_site_path), new_site_name))
        print("Creating a new django website was done")

    except shutil.Error as e:
        print(f"Error creating and renaming a website {e}")

    except OSError as e:
        print(f"Error creating and renaming a website {e}")


sample_path = 'django_sample'


# new_site_path = input(">>> ")
# new_site_name = input(">>> ")
# copy_new_django_sample(sample_path, new_site_path, new_site_name)

# result = os.system('dir')


def rename_project(old_name, new_name, folder_path):
    # Повний шлях до папки
    folder_path_full = os.path.join(folder_path, old_name)

    # Переіменування папки
    new_folder_path = os.path.join(folder_path, new_name)
    os.rename(folder_path_full, new_folder_path)

    files_project = os.listdir(f"{folder_path}/{new_name}")

    for file_name in files_project:
        print(file_name)
        file_path_project = os.path.join(folder_path, folder_path, file_name)
        name_file_project = os.path.basename(file_path_project)

        if name_file_project.endswith(".py"):
            with open(os.path.join(folder_path, new_name, name_file_project), 'r') as file:
                lines = file.readlines()

            with open(os.path.join(folder_path, new_name, name_file_project), 'w') as file:
                for line in lines:
                    new_line = line.replace(old_name, new_name)
                    file.write(new_line)


    return print('Created a new website on django')


def rename_app(old_name, new_name, folder_path):

    folder_path_full = os.path.join(folder_path, old_name)
    new_path_folder = os.path.join(folder_path, new_name)

    os.rename(folder_path_full, new_path_folder)

    files_app = os.listdir(f"{folder_path}/{new_name}")

    for file_name in files_app:
        print(file_name)
        file_path_app = os.path.join(folder_path, new_name, file_name)
        name_file_app = os.path.basename(file_path_app)

        if name_file_app.endswith(".py"):
            with open(os.path.join(folder_path, new_name, name_file_app), 'r') as file:
                lines = file.readlines()

            with open(os.path.join(folder_path, new_name, name_file_app), 'w') as file:
                for line in lines:
                    new_line = line.replace(old_name, new_name)
                    file.write(new_line)

    print("Renaming app was done")



if "__main__" == __name__:
    print("Rename project")
    old_name_project = input("> ")
    new_name_project = input("> ")
    folder_path = input("> ")
    old_name_app = input("> ")
    new_name_app = input("> ")
    rename_project(old_name_project, new_name_project, folder_path)
    rename_app(old_name_app, new_name_app, folder_path)








