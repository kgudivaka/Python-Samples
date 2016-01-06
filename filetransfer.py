#open the input file infile
infile = open('C:\\Users\\Rama\\Desktop\\months.txt','r')
content = infile.read()

#open output file
outfile = open('C:\\Users\\Rama\\Desktop\\output.txt','w')
outfile.write(content)
outfile.close()
