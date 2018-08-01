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
    rdr = list(csv.reader(csvfile))
    sub = re.split("\d\.",rdr[14][0])[1:]+re.split("\d\.",rdr[15][0])[1:]
    no2sub = rdr[8][0].count("--->")
    for row in range(17,len(rdr),62):
        for sr in range(0,28,9):
            if '-------' not in rdr[row+sr][0]:
                name_ls=rdr[row+sr][0].split()
                res_a+=name_ls[0]+", "+ " ".join(name_ls)[len(name_ls[0]):-36] +", "
                a,b,c=get_matrix(rdr[row+sr+2][0]+rdr[row+sr+2][1][:2],rdr[row+sr+3][0]+rdr[row+sr+3][1][:2] ,rdr[row+sr+4][0]+rdr[row+sr+4][1][:2])
                for i in range(len(a)):
                    res_a+=str(a[i])+", "+str(b[i])+","+str(c[i])+", "
                res = rdr[row+sr+5][1]
                res_a+=res[:2]+", "+res[4:7]+", "+res[7:]+", "+ rdr[row+sr+3][1][2:]+", "+ "\n"
    a=[rdr[9][0][i:i+9].replace("---","-"*9) for i in range(0, len(rdr[9][0]), 9)]  + [rdr[9][1][:9]]
    b=[rdr[10][0][i:i+9].replace("---","-"*9) for i in range(0, len(rdr[10][0]), 9)]+ [rdr[10][1][:9]]
    c=[rdr[11][0][i:i+3].replace("---","-"*3) for i in range(0, len(rdr[11][0]), 3)]+ [rdr[11][1][:3]]

with open(sys.argv[1]+".csv","w") as csvfile:
    sub_str = " Sr No. , Name , "
    for i in sub:
        if no2sub>0:sub_str+=i+", , , , , , ";no2sub-=1
        else:sub_str+=i+", , , "
    csvfile.write(sub_str+"\n")
    res_b=" , , "
    for i in range(len(a)):
        res_b+=str(a[i])+", "+str(b[i])+","+str(c[i])+", "
    csvfile.write(res_b+"\n"+res_a)
