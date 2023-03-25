"""

insta account : mhmd_busaidi

Mohammed Al Busaidi

"""



import csv
def list_to_html_table(list_of_rows):
	hdr=list_of_rows[0]
	d=["    <th>"+rw+"</th>\n" for rw in hdr]
	aq="  <tr>\n"+"".join(d).strip("\n")+"\n  </tr>"
	rest=list_of_rows[1:]
	final_rows=[f_row(rw) for rw in rest]
	y="\n".join(final_rows)
	tb="<table>\n"
	lsttb="\n\n</table>"
	return tb+aq+"\n"+y+lsttb
	#return "<table>\n"+aq+"\n"+y+"\n\n</table>"

def f_row(rw):
	a=["    <td>"+i+"</td>\n" for i in rw]
	aq="  <tr>\n"+"".join(a).strip("\n")+"\n  </tr>"
	return aq



def csv_to_list(file_name):
    so=[]
    with open(file_name,"r") as cv:
        red=csv.reader(cv)
        #d=["<tr>\n"+rw+"\n</tr>\n" for rw in red]
        for rw in red:
                so.append(rw)

    return so


def csv_to_html_table(file_name,out_path,ext="txt"):
    a=csv_to_list(file_name)
    b=list_to_html_table(a)
    #cc=csv_to_html_table(b)
    if ext=="txt":
        with open(out_path+".txt","a",errors="ignore") as vb:
	        print(b,file=vb)
    else:
        htmm="""<html>
<style>
table {
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid black;
}
th {
background-color:;
}
td{
background-color:black;
color:white;
}
</style>
<body>\n
"""+b+"""\n</table>
</body>
</html>"""
        with open(out_path+".html","a") as vb:
	        print(htmm,file=vb)

    



csv_to_html_table(path_of_csv_file,path_of_out,html_OR_txt) # don't type .html in path_of_out   ---- last argumet whether txt or html extension

"""
for example :-


csv_to_html_table("C:/Users/Admin/Downloads/company sales March.csv","C:/Users/Admin/Desktop/nice_formated company sales march","html")

"""


"""

insta account : mhmd_busaidi

Mohammed Al Busaidi


"""
