
class ProjectBuilderError(Exception):
    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message

class ProjectNotFoundError(ProjectBuilderError):
    pass

class FileNotFoundError(ProjectBuilderError):
    pass