import pandas as pd
import os

def getarray() :
    try : 
        name = str(input("Excel name, extension is required ?(Check if the array is on the right folder) "))
        name = name.split(".")
        if name[1] != "xlsx" :
            print("Extension error : not ", name[1],".Need xlsx")
            getarray()
        else :
            return name[0]
    except ValueError:
        print("The name must be a str")
        getarray()


def read_excel(name):
    df = pd.read_excel("./excel/" + str(name) + ".xlsx")

    col = df.columns
    n_col = len(col)

    tbl = df.to_numpy()
    n_tbl = len(tbl)

    return [tbl, n_tbl, col, n_col]


def generate_sql(tbl, n_tbl, col, n_col, name):

    fl = str(input("SQL File Name (Extension didn't require): "))
    wtr = ['SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";', 'SET time_zone = "+00:00";']
    fp = open( "./sql file/"+ fl + '.sql', 'w',encoding='utf-8')
    for x in wtr :
        fp.write(x + "\n")
        
  
    fp.write("\n" + "CREATE TABLE `" + name + "` (")
    fp.write("\n" + "\t" + "`id` int(11) NOT NULL,")
    for i in range(0, n_col) :
        if i != (n_col - 1) :
            fp.write("\n" + "\t" + "`" + col[i] + "` text NOT NULL,")
        else :
            fp.write("\n" + "\t" + "`" + col[i] + "` text NOT NULL")
    fp.write("\n" + ") ENGINE=MyISAM DEFAULT CHARSET=utf8;")

    #columns generation
    l = "(`id`,"
    
    for i in range(0, n_col) :
        if i != (n_col - 1) :
            l += "`" + col[i] + "`,"
        else :
            l += "`" + col[i] + "`)"
    fp.write("\n" + "\n" "INSERT INTO `" + name + "`" + l + " VALUES")

    r = 0
    #line geration
    for i in range(0, n_tbl) :
        if i != (n_tbl - 1) :
            l = str(r)
            for n in range(0, n_col) :
                if n != (n_col - 1) :
                    l += "," + "'" + str(tbl[i][n]) + "'"
                else :
                    l += "," + "'" +str(tbl[i][n]) + "'"
            fp.write("\n"+ "(" + l + ")" + "," )
        else :
              l = str(r)
              for n in range(0, n_col) :
                if n != (n_col - 1) :
                    l += "," + "'" + str(tbl[i][n]) + "'"
                else :
                    l += "," + "'" + str(tbl[i][n]) + "'"
              fp.write("\n"+ "(" + l + ")" + ";" )
        r += 1
    fp.write("\n" + "\n" + "ALTER TABLE `" + name + "`")
    fp.write("\n" + "\t" + "ADD PRIMARY KEY (`" + "id" + "`);")

    fp.write("\n" + "\n" + "ALTER TABLE `" + name + "`")
    fp.write("\n" + "\t" + "MODIFY `" + "id" + "` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=" + str(r) + ";")
 
    fp.close()
    print("The file was perfectly create !")

def drop() :
    name = str(input("Wich file you want to delete (Extension Required): "))
    name = name.split(".")

    if name[1] == "xlsx" :
        if os.path.exists('./excel/' + str(name[0]) + '.xlsx'):
            os.remove('./excel/' + str(name[0]) + '.xlsx')
            print("File " + str(name[0]) + str(name[1]) + " deleted.")
        else:
            print("The file doesn't exist.")
    elif name[1] == "sql" :
        if os.path.exists('./sql file/' + str(name[0]) + '.sql'):
            os.remove('./sql file/' + str(name[0]) + '.sql')
            print("File " + str(name[0]) + str(name[1]) + " deleted.")
        else:
            print("The file doesn't exist.")

