import flask
from flask import render_template, Flask, request, jsonify
from flask_cors import CORS
import requests
import polyline

app = Flask(__name__, template_folder="templates-flask-test")
CORS(app)
count=0
def fetching_lat_lng(origin, destination):
    test = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&key=AIzaSyCHttcfy83akWGX0yXCX53DnrVN1anZFEM&alternatives=true").json()
    #test = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&key=AIzaSyAW6U840k0zHzm18XXkXcoCCyHftTm1JHY&alternatives=true").json()

    routes = test['routes']
    #print(len(Lat_and_Lng[4]))
    Lat_and_Lng = []
    for route in routes:
        each_route = []
        for leg in route['legs']:
            for steps in leg['steps']:
                each_route += polyline.decode(steps['polyline']['points'])
                print(polyline.decode(steps['polyline']['points']))
        Lat_and_Lng.append(each_route)

    return Lat_and_Lng

#setting the mode
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 's200195'

@app.route("/")
def start():
   return render_template('index.html')

@app.route("/test", methods=["POST"])
def test():
    from data_processing import analysis
    from KNN import NearestNeighbours
    #from RouteModel import RouteSafer
    Lat_and_Lng = []
    origin = request.get_json(force=True)['locations'][0]
    destination = request.get_json(force=True)['locations'][1]

    Lat_and_Lng = fetching_lat_lng(origin, destination)


    Analyze = analysis(Lat_and_Lng)
    score = []
    for i in Analyze:
        score.append(NearestNeighbours(i))
    #test
    #test = RouteSafer(1,1,1,1,2,2,2)
    return jsonify({'polyline' : Analyze, 'score': score, 'origin': Lat_and_Lng[0][0], 'destination':Lat_and_Lng[0][-1]})


#setting debug to true
if __name__ == "__main__":
    app.run(host = '0.0.0.0')

#http://100.64.196.194:5000/test
