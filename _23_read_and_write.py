__author__ = 'royalfiish'

fw = open("test.txt", 'w')
fw.write("added text to file\n")
fw.write("Testing second line\n")
fw.close()

fr = open("test.txt", 'r')
text = fr.read()
print(text)
fr.close()
