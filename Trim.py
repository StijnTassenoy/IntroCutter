import os
import subprocess

def getAllVideos(extension):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        if not file.endswith(extension):
            files.remove(file)
    return files        

try:
    season_number = input("Enter season number: ")
    time_to_start_vid = input("Enter time to start video: ")
    extension_type = input("Enter extension type: ")
    allvids = getAllVideos(extension_type)
    print(allvids)
    for i in range(0, len(allvids)):
        print("[", i+1, "] ", allvids[i], sep='')
        episode = "S"+str(season_number).zfill(2)+"E"+str(i+1).zfill(2)+"."+extension_type
        subprocess.call(["ffmpeg", "-ss", time_to_start_vid, "-i", allvids[i], "-c", "copy", episode])
except:
    print("Couldn't find")