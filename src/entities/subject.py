class Subject:
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def to_dict(self):
        return {
            "id": self.__id
        }