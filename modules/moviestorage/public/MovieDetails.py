class MovieDetails:

    def __init__(self, id_move, name, description, url):
        self._id = id_move
        self._name = name
        self._description = description
        self._url = url

    def copy(self):
        return MovieDetails(self._id, self._name, self._description, self._url)

    def get_id(self):
        return self._id

    def set_id(self, id_move):
        copy = self.copy()
        copy._id = id_move
        return copy

    def get_name(self):
        return self._name

    def set_name(self, name):
        copy = self.copy()
        copy._name = name
        return copy

    def get_description(self):
        return self._description

    def set_description(self, description):
        copy = self.copy()
        copy._description = description
        return copy

    def get_url(self):
        return self._url

    def set_url(self, url):
        copy = self.copy()
        copy._url = url
        return copy
