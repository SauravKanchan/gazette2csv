import os,sys,csv,re
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
    sub = re.split("\d\.",reader[14][0])[1:]+re.split("\d\.",reader[15][0])[1:]
    no2sub = reader[8][0].count("--->")
    for row in range(17,len(reader),62):
        for sp_row in range(0,28,9):
            if '-------' not in reader[row+sp_row][0]:
                name_ls=reader[row+sp_row][0].split()
                res_a+=name_ls[0]+", "+ " ".join(name_ls)[len(name_ls[0]):-36] +", "
                a,b,c=get_matrix(reader[row+sp_row+2][0]+reader[row+sp_row+2][1][:2], reader[row+sp_row+3][0]+reader[row+sp_row+3][1][:2] ,reader[row+sp_row+4][0]+reader[row+sp_row+4][1][:2])
                for i in range(len(a)):
                    res_a+=str(a[i])+", "+str(b[i])+","+str(c[i])+", "
                res_a+="\n"
    a=[reader[9][0][i:i+9].replace("---","-"*9) for i in range(0, len(reader[9][0]), 9)]   + [reader[9][1][:9]]
    b=[reader[10][0][i:i+9].replace("---","-"*9) for i in range(0, len(reader[10][0]), 9)]  + [reader[10][1][:9]]
    c=[reader[11][0][i:i+3].replace("---","-"*3) for i in range(0, len(reader[11][0]), 3)] + [reader[11][1][:3]  ]

with open(sys.argv[1]+".csv","w") as csvfile:
    sub_str = " , , "
    for i in sub:
        if no2sub>0:sub_str+=i+", , , , , , ";no2sub-=1
        else:sub_str+=i+", , , "
    csvfile.write(sub_str+"\n")
    res_b=" , , "
    for i in range(len(a)):
        res_b+=str(a[i])+", "+str(b[i])+","+str(c[i])+", "
    csvfile.write(res_b+"\n")
    csvfile.write(res_a)
