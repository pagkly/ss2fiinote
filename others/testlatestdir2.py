#b'blob 481\x00
def getlatestdir():
    import os
    directory = "C:\\\\Users\\\\SP3\\\\AppData\\\\Roaming\\\\FiiNote\\\\@pagkly\\\
otes"
    alldirlist=[os.path.join(directory,d) for d in os.listdir(directory)]
    for f in alldirlist:
        if (".nti" in f) or ("andimages" in f) or (".pc" in f):
            alldirlist.remove(f)
    latestdir=max(alldirlist, key=os.path.getmtime)
    if "AOWNLPC0000020180808143255.notz" in latestdir:
        print("correct")
    return latestdir
print(getlatestdir())
'