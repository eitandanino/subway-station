import requests
from flask import Flask, render_template, request

app = Flask(__name__)


page_link = "http://mtaapi.herokuapp.com/stations"
response = requests.get(page_link).json()
result = response["result"]
# print(result[0])

# specific_station_api = "http://mtaapi.herokuapp.com/stop?id=120S"
# response2 = requests.get(specific_station_api).json()
# print(response2)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/stations")
def all_stations():
    return render_template("stations.html", result=result)


@app.route("/specific_stations", methods=['GET', 'POST'])
def specific_station():
    get_id = request.form.get("id")
    specific_station_api = f"http://mtaapi.herokuapp.com/api?id={get_id}"
    response2 = requests.get(specific_station_api).json()
    station_name = response2["result"]["name"]
    station = response2["result"]["arrivals"]
    return render_template("specificStation.html", times=station, name=station_name)


@app.route("/time", methods=['GET', 'POST'])
def specific_time():
    get_hour = request.form.get("hour")
    get_min = request.form.get("minutes")
    time_api = f"http://mtaapi.herokuapp.com/times?hour={get_hour}&minute={get_min}"
    response3 = requests.get(time_api).json()
    print(response3["result"])
    time = response3["result"]
    return render_template("hour.html", time=time)


if __name__ == "__main__":
    app.run(debug=True)

