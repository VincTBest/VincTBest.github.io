# this is a demo app.
isGuest = None


def init():
    global isGuest
    isGuest = False


def meta():
    metadata = {"name": "File Explorer", "id": "fileexplorer", "showGuest": False, "showUser": True}
    return metadata


def guest():
    global isGuest
    isGuest = True


def main():
    global isGuest
    if isGuest:
        pass
    print("download successful!!!")
