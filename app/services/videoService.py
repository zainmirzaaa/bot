import random

class VideoService:
    def __init__(self, pendingFolder, sentFolder):
        self.pendingFolder = pendingFolder
        self.sentFolder = sentFolder
        print("zain")

def getVideoInfo(vid):
    pass

    # find vid file path

    # rerturn path

def markAsSent(path):
    pass

    # remove path from folder

    # add path to used video folder



def getRandomVideo(folder):

    if folder is None:
        return

    randomVideo = random.choice(folder)
    path = getVideoInfo(randomVideo)
    markAsSent(path)

    return randomVideo


