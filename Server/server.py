# import sqlite3
from flask import Flask, render_template,jsonify,request,abort,Response
import requests
import json
from flask_cors import CORS
import draw_graph
import base64
import mysql.connector
from mysql.connector import Error
import change

connection = mysql.connector.connect(host='localhost',
                                         database='aquajal1',
                                         user='root',
                                         password='',buffered =True)
mycursor = connection.cursor()

app=Flask(__name__)

CORS(app)

# psum=0;
# csum=0;
# lsum=0;
# casum=0;
# tsum=0;
# preform=0;
count=0
array_of_1L=[0 for i in range(5)]
array_of_2L=[0 for i in range(5)]
array_of_halfL=[0 for i in range(5)]
array_of_20L=[0 for i in range(6)]
# print(array_of_1L,"all zeros")


@app.route("/")
def testing():
    return "hello"
@app.route("/api/check",methods=["POST"])
def t_table():
    name=request.form.get("username")
    pwd=request.form.get("pwd")
    print(name,pwd)
    sql = "SELECT * FROM admin WHERE username = "+"'"+name +"'"+" AND pwd = "+"'"+pwd+"'"

    mycursor.execute(sql)
    connection.commit()
    rows=mycursor.fetchall()
    print(len(rows),"sdfghjk")
    if(len(rows) == 1):
        return "1"
    else:   
        return "0"

@app.route("/api/1L_static_details",methods=["GET"])
def static_Data_1L():
    psum=csum=casum=lsum=preform=tsum=0
    sql="SELECT * from raw_material where product_code='1L' ";
    print(sql)
    mycursor.execute(sql)
    connection.commit()
    rows=mycursor.fetchall()
    print(len(rows),"sdfghjk")
    print(rows)

    for i in rows:
        if(i[7]=="added"):
              psum=psum+i[1]
              lsum=lsum+i[2]
              csum=csum+i[3]
              casum=casum+i[4]
              tsum=tsum+i[5]
        elif(i[7]=="altered"):
            print("hiiiiiiiiii")
            psum=psum-i[1]
            lsum=lsum-i[2]
            csum=csum-i[3]
            casum=casum-i[4]
            tsum=tsum-i[5]
        print(psum,"jjjjjjjjjjjjjjjjjjjj")

    preform=psum*(1000/20.5)

    array_of_1L[0]=preform
    array_of_1L[1]=lsum
    array_of_1L[2]=csum
    array_of_1L[3]=casum
    array_of_1L[4]=tsum
  
    print(array_of_1L,"arrrrrrrrrrrrrrrrr")
    # print(array_of_1L,"static_array")
    return jsonify(array_of_1L)

@app.route("/api/2L_static_details",methods=["GET"])
def static_Data_2L():
    psum=csum=casum=lsum=preform=tsum=0
    sql="SELECT * from raw_material where product_code='2L' ";

    mycursor.execute(sql)
    connection.commit()
    rows=mycursor.fetchall()
    print(len(rows),"sdfghjk")
    print(rows)

    for i in rows:
        if(i[7]=="added"):
              psum=psum+i[1]
              lsum=lsum+i[2]
              csum=csum+i[3]
              casum=casum+i[4]
              tsum=tsum+i[5]
        elif(i[7]=="altered"):
            psum=psum-i[1]
            lsum=lsum-i[2]
            csum=csum-i[3]
            casum=casum-i[4]
            tsum=tsum-i[5]
    preform=psum*(1000/30)

    array_of_2L[0]=preform
    array_of_2L[1]=lsum
    array_of_2L[2]=csum
    array_of_2L[3]=casum
    array_of_2L[4]=tsum
 
    # print(array_of_1L,"static_array")
    return jsonify(array_of_2L)

@app.route("/api/half-L_static_details",methods=["GET"])
def static_Data_halfL():
    psum=csum=casum=lsum=preform=tsum=0
    sql="SELECT * from raw_material where product_code='1/2L' ";

    mycursor.execute(sql)
    connection.commit()
    rows=mycursor.fetchall()
    print(len(rows),"sdfghjk")
    # print(rows)

    for i in rows:
        if(i[7]=="added"):
              psum=psum+i[1]
              lsum=lsum+i[2]
              csum=csum+i[3]
              casum=casum+i[4]
              tsum=tsum+i[5]
        elif(i[7]=="altered"):
            psum=psum-i[1]
            lsum=lsum-i[2]
            csum=csum-i[3]
            casum=casum-i[4]
            tsum=tsum-i[5]
    preform=psum*(1000/13)

    array_of_halfL[0]=preform
    array_of_halfL[1]=lsum
    array_of_halfL[2]=csum
    array_of_halfL[3]=casum
    array_of_halfL[4]=tsum
 
    # print(array_of_1L,"static_array")
    return jsonify(array_of_halfL)

@app.route("/api/add_alter_data",methods=["POST"])
def add_alter_data():
    connection = mysql.connector.connect(host='localhost',
                                         database='aquajal1',
                                         user='root',
                                         password='',buffered =True)
    mycursor = connection.cursor()
    product_code_r=request.form.get("product_code")
    preform_r=request.form.get("preform")
    label_r=request.form.get("label")
    cap_r=request.form.get("cap")
    carton_r=request.form.get("carton")
    tape_r=request.form.get("tape")
    date_r=request.form.get("raw_date")
    status_r=request.form.get("status")
    # sql = "INSERT INTO raw_material (product_code,preform,Lebel,cap,carton,tape,raw_date,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # val=("'"+product_code_r+"',"+"'"+preform_r+"',"+"'"+label_r+"',"+"'"+cap_r+"',"+"'"+carton_r+"',"+"'"+tape_r+"',"+"'"+date_r+"',"+"'"+status+"'")
    print(status_r,type(status_r))
    sql = "INSERT INTO raw_material VALUES ("+"'"+product_code_r+"'"+","+preform_r+","+label_r+","+cap_r+","+carton_r+","+tape_r+","+"'"+date_r+"'"+","+"'"+status_r+"'"+")"
    print(sql)
    mycursor.execute(sql)
    connection.commit()

    return "1"





@app.route("/api/add_alter_data_2L_1/2L",methods=["POST"])
def add_alter_data_2L_half_L():
    connection = mysql.connector.connect(host='localhost',
                                         database='aquajal1',
                                         user='root',
                                         password='',buffered =True)
    mycursor = connection.cursor()
    product_code_r=request.form.get("product_code")
    preform_r=request.form.get("preform")
    label_r=request.form.get("label")
    cap_r="0"
    carton_r=request.form.get("carton")
    tape_r="0"
    date_r=request.form.get("raw_date")
    status_r=request.form.get("status")
    # sql = "INSERT INTO raw_material (product_code,preform,Lebel,cap,carton,tape,raw_date,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # val=("'"+product_code_r+"',"+"'"+preform_r+"',"+"'"+label_r+"',"+"'"+cap_r+"',"+"'"+carton_r+"',"+"'"+tape_r+"',"+"'"+date_r+"',"+"'"+status+"'")
    print(status_r,type(status_r))
    print(product_code_r,preform_r,label_r,cap_r,carton_r,tape_r,date_r,status_r)
    sql = "INSERT INTO raw_material VALUES ("+"'"+product_code_r+"'"+","+preform_r+","+label_r+","+cap_r+","+carton_r+","+tape_r+","+"'"+date_r+"'"+","+"'"+status_r+"'"+")"
    print(sql)
    mycursor.execute(sql)
    connection.commit()

    return "1"


@app.route("/api/total_details",methods=["POST"])
def static_data_total():
    # psum=csum=casum=lsum=preform=tsum=
    value=request.form.get("search")
    print(value,"serached value")
    if(value=="0"):
        sql="SELECT * from raw_material"
    elif(value=="2L"):
        sql="SELECT * from raw_material where product_code='2L' "
    elif(value=="1L"):
        sql="SELECT * from raw_material where product_code='1L' "
    elif(value=="1/2L"):
        sql="SELECT * from raw_material where product_code='1/2L' "
    elif(value=="1"):
        sql="SELECT * from twyl_raw"
    mycursor.execute(sql)
    connection.commit()
    rows=mycursor.fetchall()


 
    # print(array_of_1L,"static_array")
    return jsonify(rows)


@app.route("/api/20L_static_details",methods=["GET"])
def static_Data_20L():
    psum=csum=casum=lsum=preform=tsum=cold=0
    sql="SELECT * from twyl_raw where product_code='20L' ";

    mycursor.execute(sql)
    connection.commit()
    rows=mycursor.fetchall()
    print(len(rows),"sdfghjk")
    print(rows)

    for i in rows:
        if(i[8]=="added"):
              psum=psum+i[1]
              lsum=lsum+i[4]
              csum=csum+i[3];
              casum=casum+i[2];
              tsum=tsum+i[5];
              cold=cold+i[6];

        elif(i[8]=="altered"):
            psum=psum-i[1]
            lsum=lsum-i[2]
            csum=csum-i[3];
            casum=casum-i[4];
            tsum=tsum-i[5];
            cold=cold-i[6];
    # preform=psum*(1000/30)

    array_of_20L[0]=psum
    array_of_20L[1]=lsum
    array_of_20L[2]=csum
    array_of_20L[3]=casum
    array_of_20L[4]=tsum
    array_of_20L[5]=cold
 
    # print(array_of_1L,"static_array")
    return jsonify(array_of_20L)
    
@app.route("/api/add_alter_data_20L",methods=["POST"])
def add_alter_data_20L():
    connection = mysql.connector.connect(host='localhost',
                                         database='aquajal1',
                                         user='root',
                                         password='',buffered =True)
    mycursor = connection.cursor()
    product_code_r=request.form.get("product_code")
    preform_r=request.form.get("cans")
    label_r=request.form.get("dispenser")
    cap_r=request.form.get("twyL_cap")
    carton_r=request.form.get("twyL_Lebel")
    tape_r=request.form.get("slews")
    date_r=request.form.get("coldcans")
    status_r=request.form.get("r_date")
    status_togori=request.form.get("status")
    # sql = "INSERT INTO raw_material (product_code,preform,Lebel,cap,carton,tape,raw_date,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # val=("'"+product_code_r+"',"+"'"+preform_r+"',"+"'"+label_r+"',"+"'"+cap_r+"',"+"'"+carton_r+"',"+"'"+tape_r+"',"+"'"+date_r+"',"+"'"+status+"'")
    print(status_r,type(status_r))
    sql = "INSERT INTO twyl_raw VALUES ("+"'"+product_code_r+"'"+","+preform_r+","+label_r+","+cap_r+","+carton_r+","+tape_r+","+"'"+date_r+"'"+","+"'"+status_r+"'"+","+"'"+status_togori+"'"+")"
    print(sql)
    mycursor.execute(sql)
    connection.commit()

    return "1"

@app.route("/api/recommend",methods=["POST"])
def add_alter_recommend():
    connection = mysql.connector.connect(host='localhost',
                                         database='aquajal1',
                                         user='root',
                                         password='',buffered =True)
    mycursor = connection.cursor()
    date=request.form.get("search")
    product_r=request.form.get("product_code")
    print(date,product_r)

    # SELECT * FROM raw_material WHERE MONTH(raw_date)=4
    array=[]
    sql="SELECT avg(preform) as preform,avg(Lebel) as lebel,avg(cap) as cap,avg(carton) as carton,avg(tape) as tape from raw_material where product_code="+"'"+product_r+"'"+"AND "+"MONTH(raw_date)="+"'"+date+"'"
    mycursor.execute(sql)
    connection.commit()
    rows=mycursor.fetchall()
    # print(len(rows[0][0]))
    # print(rows[0][0]==None)
    if(rows[0][0]==None):
        return jsonify(["","","","",""])
    else:
        for i in range(5):
            array.append(int(rows[0][i]))
        # print(array[0])
        return jsonify(array)

@app.route("/api/graph",methods=["POST"])
def graph():
    # app.run(port=8080)
    month=request.form.get("month")
    year=request.form.get("year")
    product_code=request.form.get("product_code")
    print(month,year,product_code)
    array=[]
    sql="SELECT sum(preform) as preform,sum(Lebel) as lebel,sum(cap) as cap,sum(carton) as carton,sum(tape) as tape from raw_material where product_code="+"'"+product_code+"'"+"AND "+"MONTH(raw_date)="+"'"+month+"'"+"AND "+"YEAR(raw_date)="+"'"+year+"'"
    print(sql,"aaaaaaaaaaaaa")
    mycursor.execute(sql)
    connection.commit()
    rows=mycursor.fetchall()
    print(rows)
    if(rows[0][0]==None):
        return "failed"
    else:
        for i in range(5):
            array.append(int(rows[0][i]))
        draw_graph.display(array)
        img=open("result.png","rb")
        change=open("change.py","w+")
        change.write("1")
        change.close()
        # return base64.b64encode(img.read())
        return base64.b64encode(img.read())

if __name__ == '__main__':
	app.debug=True
	app.run(port=8080)