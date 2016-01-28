import glob, os

#change the dir to one containing all the json for tasks
os.chdir("/Users/pratikyadav/test")


import json

#create an empty list
features = []


for f in glob.glob("*.json"):
    feature = json.load(open(f))
    features.append(feature)

out_geojson = {
    'type': 'FeatureCollection',
    'features': features
}

out_file = open('outfile.geojson', 'w')
out_file.write(json.dumps(out_geojson, indent=2))
out_file.close()
