import os,sys
os.system("java -jar tabula-1.0.2-jar-with-dependencies.jar -p all -o {0}.csv {0}.pdf".format(sys.argv[1]) )
