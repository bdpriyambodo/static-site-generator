import os
import shutil

def remove_and_copy(source, destination):

    if os.path.isabs(source):
        abs_source = source
    else:
        abs_source = os.path.abspath(source)

    if os.path.isabs(destination):
        abs_destination = destination
    else:
        abs_destination = os.path.abspath(destination)

    # check destination
    destination_exist = os.path.exists(destination)
    source_exist = os.path.exists(source)
    if not destination_exist:
        print('Destination is not exist')
    else:
        shutil.rmtree(destination)
        os.makedirs(destination)
    
    # check source
    if not source_exist:
        print('Source is not exist')

    if destination_exist and source_exist:
        print('Both source and destination exist\n')

    contents = (os.listdir(source))

    for content in contents:
        join_path_source = os.path.join(abs_source, content)
        join_path_destination = os.path.join(abs_destination, content)
        if os.path.isfile(join_path_source):
            shutil.copy(join_path_source, abs_destination)
            print(f'{join_path_source} is copied to {join_path_destination}\n')
        else:
            os.mkdir(join_path_destination)
            print(f'Directory {join_path_destination} is created\n')
            remove_and_copy(join_path_source, join_path_destination)



if __name__ == "__main__":
    remove_and_copy("static","public")

