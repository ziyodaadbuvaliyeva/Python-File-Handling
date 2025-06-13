file=open('input.txt')

text=file.read()
file.close()

file=open('output.txt''w')

file.write('salom' +text)
file.close()
