import clipboard


class ClipboardService:

    def copy_to_clipboard(self, text):
        clipboard.copy(text)
        self.delete_after_seconds(30)

    def delete_after_seconds(self, seconds):
        #TODO Start timer and after seconds call:
        #self.copy_to_clipboard("")
        pass
