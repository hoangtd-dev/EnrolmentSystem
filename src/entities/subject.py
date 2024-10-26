class Subject:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name
        }