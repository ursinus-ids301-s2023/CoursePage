import subprocess

fin = open("out.txt")

for line in fin.readlines():
    line = line.lstrip()
    line = line.strip()
    if line[0:4] == "path":
        line = line[7::]
        cmd = ["git", "rm", "--cached", line]
        print(cmd)
        subprocess.call(cmd)

fin.close()
