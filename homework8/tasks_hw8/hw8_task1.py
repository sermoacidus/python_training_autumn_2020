"""
Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
storage['name']  # will be string 'kek'
storage.song_name  # will be 'shadilay'
storage.power  # will be integer 9001
"""


class CustomStorageReader:
    def __init__(self, file_path: str):
        self.__dict__["file_path"] = file_path

    def built_in_attr_check(self, key):
        self.opener(key, presence_checker=True)

    def opener(self, item, presence_checker=None):
        with open(self.file_path, "r") as fh:
            for line in fh.readlines():
                line = line.rstrip().split("=", 1)
                if line[0] == item:
                    if presence_checker:
                        raise KeyError(
                            f'The key "{item}" is already present is storage. Its value is "{line[1]}"'
                        )
                    return int(line[1]) if line[1].isdigit() else line[1]

    def writer(self, key, value):
        with open(self.file_path, "a") as fh:
            fh.write(f"\n{key}={value}")

    def __setattr__(self, key, value):
        self.built_in_attr_check(key)
        self.writer(key, value)

    def __setitem__(self, key, value):
        self.built_in_attr_check(key)
        self.writer(key, value)

    def __getattr__(self, item):
        return self.opener(item)

    def __getitem__(self, item):
        return self.opener(item)
