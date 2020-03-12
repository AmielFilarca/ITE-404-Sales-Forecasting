reader = open("remove_duplicate.csv", "r")
lines = reader.read().split("\n")
reader.close()
 
writer = open("no_duplicate.csv", "w")
for line in set(lines):
    writer.write(line + "\n")
writer.close()