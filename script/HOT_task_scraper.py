import requests
import time
#total number of tasks as on 5th January is 1418.
#Change this to the current task number

for task in range(1,1419):

    response = requests.get("http://tasks.hotosm.org/project/"+str(task)+".json")
    print task
    print response
    
    # one second pause to make sure we do not hit api hard
    time.sleep(1)
    
    # reponse status will be 200 i.e okay if the task exists
    if response.status_code==200:

        body=response.text
        

        # save the file in test directory as <task number>.json
        f = open('test/'+str(task)+'.json', 'w')
        f.write(body)
        


        f.close()
    






