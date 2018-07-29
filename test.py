import os,sys,csv
os.system("java -jar tabula-1.0.2-jar-with-dependencies.jar -p all -o {0}.csv {0}.pdf".format(sys.argv[1]))
res_a=""
def get_matrix(row1, row2 ,row3):
    row_list1 = [];row_list2 = [];row_list3 = []
    for i in range(0,len(row3)-1,2):
        try:row_list1.append(int(row1[i:i+2]))
        except:row_list1.append(row1[i:i+2])
        try:row_list3.append(int(row3[i:i+2]))
        except:row_list3.append(row3[i:i+2])
        try:row_list2.append(int(row3[i:i+2])-int(row1[i:i+2]))
        except:row_list2.append(row2[i:i+2])
    return row_list1,row_list2,row_list3

with open(sys.argv[1]+'.csv') as csvfile:
    reader = list(csv.reader(csvfile))
    for row in range(17,len(reader),62):
        for sp_row in range(0,28,9):
            if '-------' not in reader[row+sp_row][0]:
                name_ls=reader[row+sp_row][0].split()
                res_a+=name_ls[0]+", "+ " ".join(name_ls)[len(name_ls[0]):-36] +", "
                a,b,c=get_matrix(reader[row+sp_row+2][0]+reader[row+sp_row+2][1][:2], reader[row+sp_row+3][0]+reader[row+sp_row+3][1][:2] ,reader[row+sp_row+4][0]+reader[row+sp_row+4][1][:2])
                for i in range(len(a)):
                    res_a+=str(a[i])+", "+str(b[i])+","+str(c[i])+", "
                res_a+="\n"

with open(sys.argv[1]+".csv","w") as csvfile:
    csvfile.write(res_a)
