import yadisk
import sys
import os
import posixpath


def pushDir(client: yadisk.Client, dirPath: str):
    for root, dirs, files in os.walk(dirPath):
        p = root.split(dirPath)[1].strip(os.path.sep)
        dir_path = posixpath.join(dirPath, p)
        try:
            client.mkdir(dir_path)
        except yadisk.exceptions.PathExistsError:
            pass

        for file in files:
            file_path = posixpath.join(dir_path, file)
            print(file_path)
            p_sys = p.replace("/", os.path.sep)
            in_path = os.path.join(dirPath, p_sys, file)

            try:
                client.upload(in_path, file_path, overwrite=True)
            except yadisk.exceptions.PathExistsError:
                pass


def pullDir(client: yadisk.Client, dirPath: str):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    try:
        for item in client.listdir(dirPath):
            item_path = os.path.join(dirPath, item.name)
            if item.type == 'file':
                print(item_path)
                client.download(item_path, item_path)
            if item.type == 'dir':
                pullDir(client, item_path)
    except:
        print(f'Dir {dirPath} not found!')


if __name__ == "__main__":
    args = sys.argv
    token = args[1]
    dir2Sync = args[2]
    action = args[3]
    t = 'y0_AgAAAAA55mLKAAuODAAAAAEAsofMAAD5sTrXi-tFsJRqoIx7jQoFXuLcNA' 
    if action == 'push':
        with yadisk.Client(token=token) as Client:
            if Client.check_token():
                pushDir(Client, dir2Sync)
            else:
                print('Token is not walid')
    if action == 'pull':
        with yadisk.Client(token=token) as Client:
            if Client.check_token():
                pullDir(Client, dir2Sync)
            else:
                print('Token is not walid')

