from bottle import *
import os

_zones = []
app = Bottle()
zm = None

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
def new_zone(zone):
    config = request.json
    config['number'] = zone
    print config
    _zones[zone - 1] = config

@app.route("/zones/<zone:int>/schedule")
def zone_schedule(zone):
    print 'getting schedule for %s' % zone
    return _zones[zone].get('schedule', {})

@app.route("/zones/<zone:int>/schedule", method="PUT")
def update_schedule(zone):
    print 'updating zone %s with schdule %s' % (zone, request.json)
    _zones[zone].schedule = request.json

@app.route("/zones/<zone:int>/on", method="POST")
def manual_activation(zone):
    print "manualing starting zone %s for %s minutes" % (zone, request.query.duration or 30)
    zm.activate(zone, request.query.duration or 30)

@app.route("/zones/<zone:int>/off", method="POST")
def manual_deactivation(zone):
    print "manualing stopping zone"
    zm.deactivate(zone)

@app.route("/zones/<zone:int>/delay", method="POST")
def delay(zone):
    print "delaying activation for zone %s for %s" % (zone, request.query.duration or 5)
    zm.delay(zone, request.query.duration or 5)

def run():
    app.run(debug=True, port=5000, reloader=True)

if __name__ == "__main__":
    import yaml
    print "loading config"
    config = yaml.load(open("../config.yml"))    
    print "config", config
    _zones = config['available'] * [None]
    for zone in config['zones']:
        _zones[zone['number'] - 1] = zone
    print "zones", _zones
    run()
