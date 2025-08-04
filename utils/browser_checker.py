import psutil

class ProcessChecker:
    def __init__(self):
        self.attrs = None

    def __iter__(self):
        return psutil.process_iter(self.attrs)


    def check_is_chrome_running(self):
        for proc in psutil.process_iter(self.attrs):
            if proc.name() == "chrome.exe":
                return True
        return None

    def check_is_firefox_running(self):
        for proc in psutil.process_iter(self.attrs):
            if proc.name() == "firefox.exe":
                return True
        return None

