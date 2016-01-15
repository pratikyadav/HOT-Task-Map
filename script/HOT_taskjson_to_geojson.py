import glob, os
os.chdir("/Users/pratikyadav/aoi")

hot=""

for file in glob.glob("*.geojson"):
    #a="test/"+file
    f = open(file, 'r')
    #print f.read()
    #print ","
    hot+=str(f.read())
    hot+=str(",")
    f.close()
 
    
yo = open('hot_test.geojson', 'w')

yo.write('{ "type": "FeatureCollection","features": [')
yo.write(hot)
yo.write(']}')
yo.close()   
#print hot