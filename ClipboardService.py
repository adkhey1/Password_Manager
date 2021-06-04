import clipboard
import time


class ClipboardService:

    def copy_to_clipboard(self, text):
        clipboard.copy(text)
        self.delete_after_seconds(20)

    def delete_after_seconds(self, seconds):
        time.sleep(20)
        self.copy_to_clipboard("")

