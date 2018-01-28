from flask import Flask,render_template,request,redirect,send_file
import requests,json,wit,sys,ast
client = wit.Wit('ROMP5H3YEJBXQ76GNQHQYG4VHD2YGJ2D')

Client_msgs = []
Wit_Responses = []

cnt = 0

app = Flask(__name__)

@app.route("/")
def fInput():
    return render_template('sam.html')

@app.route("/",methods=['POST','GET'])
def fProcess():
    global cnt
    Client_msgs.append(request.form['text'])
    client_query = Client_msgs[cnt]
    
    cnt+=1

    received_response = client.message(client_query)

    #print(received_response['entities'])

    print(len(received_response['entities']))

    for i in range(len(received_response['entities'])):
        entity = None
        value = None
        try:
            entity = list(received_response['entities'])[i]
            value = received_response['entities'][entity][0]['value']
        except:
            pass
        Wit_Responses.append([entity,value])
    return render_template('sam.html',my_list = Wit_Responses)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)