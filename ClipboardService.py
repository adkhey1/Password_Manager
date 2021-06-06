import clipboard
import threading


class ClipboardService:

    def callback(self):
        self.copy_to_clipboard("")

    def copy_to_clipboard(self, text):
        clipboard.copy(text)
        self.delete_after_seconds()

    def delete_after_seconds(self):
        threading.Timer(30, self.callback).start()

