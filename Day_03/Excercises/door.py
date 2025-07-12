class Door:
    def __init__(self,closed):
        self._closed = closed

    @property
    def opened(self):
        return  not self._closed

    @opened.setter
    def opened(self, new_value):
        self._closed = not new_value

opened = Door(True)
print("Try open: ", opened.opened)





