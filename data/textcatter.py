from os import listdir

filenames = [f for f in listdir("./")]
print(filenames[:10])
with open('./fullJayZ.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
print("Done catting.")
