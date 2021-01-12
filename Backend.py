from flask import Flask,request,make_response,jsonify
import mysql.connector
app=Flask(__name__)
from Detect_Intent import detect_intent_texts
from dynamic_response_functions.course_price import results

@app.route('/webhook', methods=['POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))
@app.route('/chat',methods=['POST'])
def chathook():
    req=request.get_json(force=True)
    print(req)
    text=req['text']
    text_list=[]
    text_list.append(text)
    result=detect_intent_texts("legend-tfsf",1,text_list,"en")
    return make_response(jsonify(result))


if __name__=="__main__":
    app.run()