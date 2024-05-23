# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the last 12 months of precipitation data as JSON."""
    session = Session(engine)
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()
    session.close()
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations from the dataset as JSON."""
    session = Session(engine)
    stations = session.query(Base.classes.Station.station).all()
    session.close()
    station_list = [station for (station,) in stations]
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return temperature observations for the previous year of data for the most active station as JSON."""
    session = Session(engine)
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()
    most_active_station_id = most_active_station[0]
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station_id).\
        filter(Measurement.date >= one_year_ago).all()
    session.close()
    tobs_list = [{"date": date, "tobs": tobs} for date, tobs in tobs_data]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def temp_stats_start(start):
    """Return TMIN, TAVG, and TMAX for all dates greater than or equal to the start date."""
    session = Session(engine)
    temp_stats = session.query(func.min(Measurement.tobs),
                                func.avg(Measurement.tobs),
                                func.max(Measurement.tobs)).\
                                filter(Measurement.date >= start).all()
    session.close()
    temp_stats_list = [{"TMIN": tmin, "TAVG": tavg, "TMAX": tmax} for (tmin, tavg, tmax) in temp_stats]
    return jsonify(temp_stats_list)

@app.route("/api/v1.0/<start>/<end>")
def temp_stats_start_end(start, end):
    """Return TMIN, TAVG, and TMAX for dates between the start and end date inclusive."""
    session = Session(engine)
    temp_stats = session.query(func.min(Measurement.tobs),
                                func.avg(Measurement.tobs),
                                func.max(Measurement.tobs)).\
                                filter(Measurement.date >= start).\
                                filter(Measurement.date <= end).all()
    session.close()
    temp_stats_list = [{"TMIN": tmin, "TAVG": tavg, "TMAX": tmax} for (tmin, tavg, tmax) in temp_stats]
    return jsonify(temp_stats_list)

if __name__ == "__main__":
    app.run(debug=True)