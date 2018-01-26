from flask import Flask,render_template,request,redirect,send_file
import requests,json
client = wit.Wit('NLDSCMV6XWVD7K7PID3EXWXIHNWCNRZQ')

Client_msgs = []
Wit_Responses = []

cnt = 0
@app.route("/",methods=['POST','GET'])
def fProcess():
    Client_msgs.append(request.form['text'])
    client_query = Client_msgs[cnt]
    cnt+=1

    received_response = client.message(client_query)
    Wit_Responses[cnt-1] = received_response

    #print(received_response['entities'])
    if 'wit_test' in received_response['entities']:
        if 'subject' in received_response['entities']:
            if 'query_all' in received_response['entities']:
                # show all the tests for that subject
                temp = str(received_response['entities']['subject'][0]['value'])+str(received_response['entities']['query_all'][0]['value'])
                return render_template('sam.html',my_list=temp)
                print('yeah '+str(received_response['entities']['subject'][0]['value'])+str(received_response['entities']['query_all'][0]['value']))
            else:
                # show the next test for that subject
                print('yeah '+str(received_response['entities']['subject'][0]['value'])+str(received_response['entities']['query_next'][0]['value']))

        else:
            if 'query_all' in received_response['entities']:
                # show all tests
                print('bleh')
            else:
                # show the next test overall
                print('code')
    elif 'wit_homework_read' in received_response['entities']:
        if 'subject' in received_response['entities']:
            if 'query_all' in received_response['entities']:
                # show all the homework for that subject
                print('code')
            else:
                # show the next homework for that subject
                print('code')
        else:
            if 'query_all' in received_response['entities']:
                # show all homework
                print('code')
            else:
                # show the next homework overall
                print('code')
    elif 'wit_timetable_read' in received_response['entities']:
        # show the timetable
        print('code')
    else:
        # some code
        print(received_response)
        # for i in received_response['entities']:
        #   print(i[0]['value'])

# print(st['msg_id'])
#client.interactive()


    # print('Logged Info ',Responses)
    # return render_template('sam.html',my_list=Responses)