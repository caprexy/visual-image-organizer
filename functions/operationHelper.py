import os, time

def sortByModifiedDate(filenames, ascending):
    
    originTime = int(time.time())
    increment = 5
    iteration = 0

    if (not ascending.get()):
        filenames.reverse()

    for path in filenames:

        newTime = originTime + increment*iteration

        os.utime(path, (newTime,newTime))

        iteration += 1

def rebuildNames(filenames, ascending):
    
    word = "a-"
    iteration = 0

    if (not ascending.get()):
        filenames.reverse()

    for path in filenames:
        directory, originFilename = os.path.split(path)
        name, extension = os.path.splittext(originFilename)

        os.rename(path, directory+word+str(iteration)+extension)

        iteration += 1