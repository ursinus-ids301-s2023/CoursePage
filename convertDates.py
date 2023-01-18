import datetime

delta = datetime.date(2023, 1, 18) - datetime.date(2020, 1, 22)
print(delta)

fin = open("syllabus_content_assignments.txt")
lines = fin.readlines()
fin.close()


fout = open("out.txt", "w")
for i, line in enumerate(lines):
    if i%3 == 2:
        date = datetime.date(*[int(x) for x in line.split("-")]) + delta
        fout.write(date.isoformat() + "\n")
    else:
        fout.write(line)
fout.close()
