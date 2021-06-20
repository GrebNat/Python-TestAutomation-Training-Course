class KeyValueStorage:
    def __init__(self, file_path: str):
        with open(file_path) as file:
            lines = file.readlines()
            for line in lines:
                self.__setattr__(line.split("=")[0].strip(), line.split("=")[1].strip())

    def __setattr__(self, key, value):
        if key.isnumeric():
            raise ValueError("incorrect key " + key)
        self.__dict__[key] = int(value) if value.isnumeric() else value

    def __getitem__(self, item):
        return storage.__dict__[item]


storage = KeyValueStorage('task1.txt')

assert storage['name'] == 'kek'and storage.song == 'shadilay'and storage.power == 9001
