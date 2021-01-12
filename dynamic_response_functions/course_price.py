from flask import Flask,request,make_response,jsonify
import mysql.connector
def results():
    req = request.get_json(force=True)

    intent=req["queryResult"]["intent"]["displayName"]
    if(intent=="course_price"):
        parameter=req["queryResult"]["parameters"]["course_price"]
        print(parameter)
        print(type(parameter))
        mydata=mydb = mysql.connector.connect(host="localhost",user="rayhan",password="123",database="practice")
        with mydata.cursor() as mycursor:
            sqldata = f"""SELECT price FROM `course_price`
                     WHERE `course_name` = '{parameter}'
                  """
            mycursor.execute(sqldata)
            price=mycursor.fetchall()
        try:
            return {'fulfillmentText': 'Price of {} course is {}'.format(parameter,price[0][0])}
        except Exception as e:
            return {'fulfillmentText': 'I dont know.Currently it is unavailable'}
# fetch action from jso
#     action = req.get('queryResult').get('action')
# return a fulfillment response
    return {'fulfillmentText': 'I am Legend'}