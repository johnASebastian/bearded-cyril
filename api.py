from bottle import *
import os

_zones = []
app = Bottle()

@app.route("/static/<file>")
def statics(file):
    path = os.getcwd() + "/static"
    return static_file(filename, root=path)

@app.route("/zones")
def zones():
    return {"zones": _zones}

@app.route("/zones/<zone:int>")
def zone(zone):
    if zone > 0 and zone <= len(_zones):
        return _zones[zone]
    else:
        abort(404)

@app.route("/zones/<zone:int>", method="PUT")
def new_zone(zone=None):
    config = request.json
    config['number'] = zone
    print config
    _zones[zone - 1] = config

@app.route("/zones/<zone:int>/schedule")
def zone_schedule(zone=None):
    print 'getting schedule for %s' % zone
    return _zones[zone].get('schedule', {})

@app.route("/zones/<zone:int>/schedule", method="PUT")
def update_schedule(zone=None):
    print 'updating zone %s with schdule %s' % (zone, request.json)
    _zones[zone].schedule = request.json

def run():
    app.run(debug=True, port=5000, reloader=True)

if __name__ == "__main__":
    _zones = 8 * [None]
    run()
