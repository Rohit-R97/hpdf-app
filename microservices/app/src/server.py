from flask import Flask,render_template,request,redirect,send_file
import requests,json,wit,sys,ast
client = wit.Wit('NLDSCMV6XWVD7K7PID3EXWXIHNWCNRZQ')

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
    Wit_Responses.append(received_response)

    #print(received_response['entities'])
    if 'wit_test' in received_response['entities']:
        if 'subject' in received_response['entities']:
            if 'query_all' in received_response['entities']:
                # show all the tests for that subject
                temp = str(received_response['entities']['subject'][0]['value'])+str(received_response['entities']['query_all'][0]['value'])
                return str(received_response)
                return render_template('sam.html',my_list=temp)
                print('yeah '+str(received_response['entities']['subject'][0]['value'])+str(received_response['entities']['query_all'][0]['value']))
            else:
                # show the next test for that subject
                return str(received_response)
                print('yeah '+str(received_response['entities']['subject'][0]['value'])+str(received_response['entities']['query_next'][0]['value']))

        else:
            if 'query_all' in received_response['entities']:
                # show all tests
                return str(received_response)
                print('bleh')
            else:
                # show the next test overall
                return str(received_response)
                print('code')
    elif 'wit_homework_read' in received_response['entities']:
        if 'subject' in received_response['entities']:
            if 'query_all' in received_response['entities']:
                # show all the homework for that subject
                return str(received_response)
                print('code')
            else:
                # show the next homework for that subject
                return str(received_response)
                print('code')
        else:
            if 'query_all' in received_response['entities']:
                # show all homework
                return str(received_response)
                print('code')
            else:
                # show the next homework overall
                return str(received_response)
                print('code')
    elif 'wit_timetable_read' in received_response['entities']:
        # show the timetable
        return str(received_response)
        print('code')
    else:
        # some code
        print(received_response)
        return str(received_response)
        # for i in received_response['entities']:
        #   print(i[0]['value'])

# print(st['msg_id'])
#client.interactive()


    # print('Logged Info ',Responses)
    # return render_template('sam.html',my_list=Responses)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)