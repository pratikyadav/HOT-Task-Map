import requests

task=1

while task<1418:

    r = requests.get("http://tasks.hotosm.org/project/"+str(task)+".json")
    print r
    #print type(r)
    if str(r)=="<Response [200]>":

        body=r.text
        print task


        f = open('pypy/'+str(task)+'.json', 'w')
        f.write(body)
        #task=task+1


        f.close()
    task=task+1






