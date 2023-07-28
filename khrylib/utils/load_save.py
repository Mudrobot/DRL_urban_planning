import yaml
import glob
import pickle
import os
import socket


def get_file_path(file_path):
    hostname = socket.gethostname()
    if hostname == 'fib':
        file_path = os.path.join('/data2/mas/nijingchen/workspace', file_path)
    elif hostname == 'rl2' or hostname == 'LEGION':
        file_path = os.path.join('/data2/nijingchen/workspace', file_path)
    elif hostname == 'rl3':
        file_path = os.path.join('/data2/nijingchen/workspace', file_path)
    elif hostname == 'rl4':
        file_path = os.path.join('/data2/nijingchen/workspace', file_path)
    elif hostname == 'DL4':
        file_path = os.path.join('/data2/nijingchen/workspace', file_path)
    else:
        raise ValueError('Unknown hostname: {}'.format(socket.gethostname()))
    return file_path


def load_yaml(file_path):
    file_path = get_file_path(file_path)
    files = glob.glob(file_path, recursive=True)
    # print("now:::",file_path)
    # print(len(files))
    assert(len(files) == 1)
    cfg = yaml.safe_load(open(files[0], 'r'))
    return cfg


def load_pickle(file_path):
    file_path = get_file_path(file_path)
    files = glob.glob(file_path, recursive=True)
    assert(len(files) == 1)
    data = pickle.load(open(files[0], 'rb'))
    return data

if __name__ == '__main__':
    load_yaml('')