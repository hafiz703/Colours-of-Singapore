from flask import Flask,jsonify
import requests
import simplejson 
import json

app = Flask(__name__)

@app.route("/")
def home():
    lat = 1.3526
    lng = 103.8352
    url = "https://api.instagram.com/v1/media/search?lat="+str(lat)+"&lng="+str(lng)+"&access_token=247164960.ba4c844.3a1ddcef17ac44bf848c87b3767f0985"
    try:
        uResponse = requests.get(url)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    # print data["data"][0]["images"]["low_resolution"]["url"]
    print url
    print data
    for i in range(len(data["data"])):
    	print data["data"][i]["images"]["low_resolution"]["url"]

    return Jresponse

if __name__ == "__main__":
    app.run(debug = True)