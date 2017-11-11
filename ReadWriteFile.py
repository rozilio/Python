'''
Code to read and write from files
'''

fr = open("read.txt", "r")
fw = open ("write.txt", "w")

text = fr.read()
fw.write(text)
fr.close()
fw.close()