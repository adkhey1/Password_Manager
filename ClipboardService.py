import clipboard
import threading


class ClipboardService:

    def callback(self):                 # reset the input of the clipboard
        self.copy_to_clipboard("")

    def copy_to_clipboard(self, text):           # copy the password to clipboard
        clipboard.copy(text)
        self.delete_after_seconds()

    def delete_after_seconds(self):                     # set a 30 sec timer until it jumps to the callback method
        threading.Timer(30, self.callback).start()

