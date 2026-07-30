import threading
import time
import hashlib
import os
import tempfile
from pathlib import Path

import pyperclip
from PIL import Image, ImageGrab


class ClipboardWatcher:
    """Watches clipboard for changes and updates IO placeholder (supports text and images)"""

    def __init__(self, io, verbose=False):
        self.io = io
        self.verbose = verbose
        self.stop_event = None
        self.watcher_thread = None
        self.last_clipboard = None
        self.last_image_hash = None
        self.io.clipboard_watcher = self

    def start(self):
        """Start watching clipboard for changes"""
        self.stop_event = threading.Event()
        self.last_clipboard = pyperclip.paste()
        try:
            initial_img = ImageGrab.grabclipboard()
            if isinstance(initial_img, Image.Image):
                self.last_image_hash = hashlib.md5(initial_img.tobytes()).hexdigest()
        except Exception:
            pass

        def watch_clipboard():
            while not self.stop_event.is_set():
                try:
                    # 1. Check for Image in clipboard first
                    try:
                        image = ImageGrab.grabclipboard()
                        if isinstance(image, Image.Image):
                            img_hash = hashlib.md5(image.tobytes()).hexdigest()
                            if img_hash != self.last_image_hash:
                                self.last_image_hash = img_hash
                                
                                # Save clipboard image to a temp file
                                temp_dir = tempfile.mkdtemp()
                                temp_file_path = os.path.join(temp_dir, "clipboard_image.png")
                                image.save(temp_file_path, "PNG")
                                abs_file_path = str(Path(temp_file_path).resolve())
                                
                                # If coder is available, add to file context
                                if hasattr(self.io, "coder") and self.io.coder:
                                    existing_file = next(
                                        (f for f in self.io.coder.abs_fnames if Path(f).name == "clipboard_image.png"), None
                                    )
                                    if existing_file:
                                        self.io.coder.abs_fnames.remove(existing_file)
                                    
                                    self.io.coder.abs_fnames.add(abs_file_path)
                                    self.io.interrupt_input()
                                    self.io.tool_action("Read", "clipboard_image.png")
                                    self.io.tool_output("Added clipboard image to the chat context.")
                                    # Sleep to prevent double trigger
                                    time.sleep(0.5)
                                    continue
                    except Exception as img_err:
                        if self.verbose:
                            print(f"Image grab clipboard watch error: {img_err}")

                    # 2. Check for text in clipboard
                    current = pyperclip.paste()
                    if current != self.last_clipboard:
                        self.last_clipboard = current
                        self.io.interrupt_input()
                        self.io.placeholder = current
                        if len(current.splitlines()) > 1:
                            self.io.placeholder = "\n" + self.io.placeholder + "\n"

                    time.sleep(0.5)
                except Exception as e:
                    if self.verbose:
                        from klyro.dump import dump
                        dump(f"Clipboard watcher error: {e}")
                    continue

        self.watcher_thread = threading.Thread(target=watch_clipboard, daemon=True)
        self.watcher_thread.start()

    def stop(self):
        """Stop watching clipboard for changes"""
        if self.stop_event:
            self.stop_event.set()
        if self.watcher_thread:
            self.watcher_thread.join()
            self.watcher_thread = None
            self.stop_event = None


def main():
    """Example usage of the clipboard watcher"""
    from klyro.io import InputOutput

    io = InputOutput()
    watcher = ClipboardWatcher(io, verbose=True)

    try:
        watcher.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped watching clipboard")
        watcher.stop()


if __name__ == "__main__":
    main()
