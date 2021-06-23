import glob
import subprocess
import os

if __name__ == '__main__':
    files = glob.glob("*.wav")
    for f in files:
        fmp3 = f.split(".wav")[0] + ".mp3"
        if not os.path.exists(fmp3):
            subprocess.call(["ffmpeg", "-i", f, fmp3])
