"""Объявление объектов данных"""

from datetime import datetime

from sqlalchemy import ARRAY, JSON, TIMESTAMP
from sqlalchemy import Boolean, Column, Integer, Numeric, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class StarlinkSat(Base):
    __tablename__ = "starlink_satellites"
    spacetrack = Column(JSON)
    version = Column(String)
    launch = Column(String)
    longitude = Column(Numeric)
    latitude = Column(Numeric)
    height_km = Column(Numeric)
    velocity_kms = Column(Numeric)
    id = Column(String, primary_key=True)

    def __init__(
        self,
        spacetrack,
        version=None,
        launch=None,
        longitude=None,
        latitude=None,
        height_km=None,
        velocity_kms=None,
        id=None,
    ):
        self.spacetrack = spacetrack
        self.version = version
        self.launch = launch
        self.longitude = longitude
        self.latitude = latitude
        self.height_km = height_km
        self.velocity_kms = velocity_kms
        self.id = id


class LaunchesSpaceX(Base):
    __tablename__ = "launches"
    fairings = Column(JSON)
    links = Column(JSON)
    static_fire_date_utc = Column(TIMESTAMP)
    static_fire_date_unix = Column(Numeric)
    tbd = Column(Boolean)
    net = Column(Boolean)
    window = Column(Numeric)
    rocket = Column(String)
    success = Column(Boolean)
    failures = Column(ARRAY(JSON))
    details = Column(String)
    crew = Column(ARRAY(String))
    ships = Column(ARRAY(String))
    capsules = Column(ARRAY(String))
    payloads = Column(ARRAY(String))
    launchpad = Column(String)
    auto_update = Column(Boolean)
    flight_number = Column(Numeric)
    name = Column(String)
    date_utc = Column(TIMESTAMP)
    date_unix = Column(Numeric)
    date_local = Column(String)
    date_precision = Column(String)
    upcoming = Column(Boolean)
    cores = Column(ARRAY(JSON))
    id = Column(String, primary_key=True)

    def __init__(
        self,
        fairings=None,
        links=None,
        static_fire_date_utc=None,
        static_fire_date_unix=None,
        tbd=None,
        net=None,
        window=None,
        rocket=None,
        success=None,
        failures=[],
        details=None,
        crew=None,
        ships=None,
        capsules=None,
        payloads=None,
        launchpad=None,
        auto_update=None,
        flight_number=None,
        name=None,
        date_utc=None,
        date_unix=None,
        date_local=None,
        date_precision=None,
        upcoming=None,
        cores=None,
        id=None,
    ):
        self.fairings = fairings
        self.links = links
        self.static_fire_date_utc = static_fire_date_utc
        self.static_fire_date_unix = static_fire_date_unix
        self.tbd = tbd
        self.net = net
        self.window = window
        self.rocket = rocket
        self.success = success
        self.failures = failures
        self.details = details
        self.crew = crew
        self.ships = ships
        self.capsules = capsules
        self.payloads = payloads
        self.launchpad = launchpad
        self.auto_update = auto_update
        self.flight_number = flight_number
        self.name = name
        self.date_utc = date_utc
        self.date_unix = date_unix
        self.date_local = date_local
        self.date_precision = date_precision
        self.upcoming = upcoming
        self.cores = cores
        self.id = id

        def __current_datetime_utc(value):
            if value is None:
                return None
            else:
                format_time_utc = "%Y-%m-%dT%H:%M:%S.%fZ"
                return datetime.strptime(value, format_time_utc)

        @property
        def static_fire_date_utc(self):
            return self._static_fire_date_utc

        @static_fire_date_utc.setter
        def static_fire_date_utc(self, value):
            self._static_fire_date_utc = __current_datetime_utc(value=value)

        @property
        def date_utc(self):
            return self._date_utc

        @date_utc.setter
        def date_utc(self, value):
            if value is None:
                self._date_utc = __current_datetime_utc(value=value)


class Capsules(Base):
    __tablename__ = "capsules"
    reuse_count = Column(Numeric)
    water_landings = Column(Numeric)
    land_landings = Column(Numeric)
    last_update = Column(String)
    launches = Column(ARRAY(String))
    serial = Column(String)
    status = Column(String)
    type = Column(String)
    id = Column(String, primary_key=True)

    def __init__(
        self,
        reuse_count=None,
        water_landings=None,
        land_landings=None,
        last_update=None,
        launches=None,
        serial=None,
        status=None,
        type=None,
        id=None,
    ):
        self.reuse_count = reuse_count
        self.water_landings = water_landings
        self.land_landings = land_landings
        self.last_update = last_update
        self.launches = launches
        self.serial = serial
        self.status = status
        self.type = type
        self.id = id


class Cores(Base):
    __tablename__ = "cores"
    block = Column(Numeric)
    reuse_count = Column(Numeric)
    rtls_attempts = Column(Numeric)
    rtls_landings = Column(Numeric)
    asds_attempts = Column(Numeric)
    asds_landings = Column(Numeric)
    last_update = Column(String)
    launches = Column(ARRAY(String))
    serial = Column(String)
    status = Column(String)
    id = Column(String, primary_key=True)

    def __init__(
        self,
        block=None,
        reuse_count=None,
        rtls_attempts=None,
        rtls_landings=None,
        asds_attempts=None,
        asds_landings=None,
        last_update=None,
        launches=None,
        serial=None,
        status=None,
        id=None,
    ):
        self.block = block
        self.reuse_count = reuse_count
        self.rtls_attempts = rtls_attempts
        self.rtls_landings = rtls_landings
        self.asds_attempts = asds_attempts
        self.asds_landings = asds_landings
        self.last_update = last_update
        self.launches = launches
        self.serial = serial
        self.status = status
        self.id = id


class Crew(Base):
    __tablename__ = "crew"
    name = Column(String)
    agency = Column(String)
    image = Column(String)
    wikipedia = Column(String)
    launches = Column(ARRAY(String))
    status = Column(String)
    id = Column(String, primary_key=True)

    def __init__(
        self,
        name=None,
        agency=None,
        image=None,
        wikipedia=None,
        launches=None,
        status=None,
        id=None,
    ):
        self.name = name
        self.agency = agency
        self.image = image
        self.wikipedia = wikipedia
        self.launches = launches
        self.status = status
        self.id = id


class Landpads(Base):
    __tablename__ = "landpads"
    name = Column(String)
    full_name = Column(String)
    status = Column(String)
    type = Column(String)
    locality = Column(String)
    region = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    landing_attempts = Column(Integer)
    landing_successes = Column(Integer)
    wikipedia = Column(String)
    details = Column(String)
    launches = Column(ARRAY(String))
    id = Column(String, primary_key=True)

    def __init__(
        self,
        name=None,
        full_name=None,
        status=None,
        type=None,
        locality=None,
        region=None,
        latitude=None,
        longitude=None,
        landing_attempts=None,
        landing_successes=None,
        wikipedia=None,
        details=None,
        launches=None,
        id=None,
    ):
        self.name = name
        self.full_name = full_name
        self.status = status
        self.type = type
        self.locality = locality
        self.region = region
        self.latitude = latitude
        self.longitude = longitude
        self.landing_attempts = landing_attempts
        self.landing_successes = landing_successes
        self.wikipedia = wikipedia
        self.details = details
        self.launches = launches
        self.id = id


class Launchpads(Base):
    __tablename__ = "launchpads"
    name = Column(String)
    full_name = Column(String)
    locality = Column(String)
    region = Column(String)
    timezone = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    launch_attempts = Column(Integer)
    launch_successes = Column(Integer)
    rockets = Column(ARRAY(String))
    launches = Column(ARRAY(String))
    status = Column(String)
    id = Column(String, primary_key=True)

    def __init__(
        self,
        name=None,
        full_name=None,
        locality=None,
        region=None,
        timezone=None,
        latitude=None,
        longitude=None,
        launch_attempts=None,
        launch_successes=None,
        rockets=None,
        launches=None,
        status=None,
        id=None,
    ):
        self.name = name
        self.full_name = full_name
        self.locality = locality
        self.region = region
        self.timezone = timezone
        self.latitude = latitude
        self.longitude = longitude
        self.launch_attempts = launch_attempts
        self.launch_successes = launch_successes
        self.rockets = rockets
        self.launches = launches
        self.status = status
        self.id = id


class Payload(Base):
    __tablename__ = "payload"
    dragon = Column(JSON)
    name = Column(String)
    type = Column(String)
    reused = Column(Boolean)
    launch = Column(String)
    customers = Column(ARRAY(String))
    norad_ids = Column(ARRAY(Integer))
    nationalities = Column(ARRAY(String))
    manufacturers = Column(ARRAY(String))
    mass_kg = Column(Numeric)
    mass_lbs = Column(Numeric)
    orbit = Column(String)
    reference_system = Column(String)
    regime = Column(String)
    longitude = Column(Numeric)
    semi_major_axis_km = Column(Numeric)
    eccentricity = Column(Numeric)
    periapsis_km = Column(Numeric)
    apoapsis_km = Column(Numeric)
    inclination_deg = Column(Numeric)
    period_min = Column(Numeric)
    lifespan_years = Column(Integer)
    epoch = Column(TIMESTAMP)
    mean_motion = Column(Numeric)
    raan = Column(Numeric)
    arg_of_pericenter = Column(Numeric)
    mean_anomaly = Column(Numeric)
    id = Column(String, primary_key=True)

    def __init__(
        self,
        dragon=None,
        name=None,
        type=None,
        reused=None,
        launch=None,
        customers=None,
        norad_ids=None,
        nationalities=None,
        manufacturers=None,
        mass_kg=None,
        mass_lbs=None,
        orbit=None,
        reference_system=None,
        regime=None,
        longitude=None,
        semi_major_axis_km=None,
        eccentricity=None,
        periapsis_km=None,
        apoapsis_km=None,
        inclination_deg=None,
        period_min=None,
        lifespan_years=None,
        epoch=None,
        mean_motion=None,
        raan=None,
        arg_of_pericenter=None,
        mean_anomaly=None,
        id=None,
    ):
        self.dragon = dragon
        self.name = name
        self.type = type
        self.reused = reused
        self.launch = launch
        self.customers = customers
        self.norad_ids = norad_ids
        self.nationalities = nationalities
        self.manufacturers = manufacturers
        self.mass_kg = mass_kg
        self.mass_lbs = mass_lbs
        self.orbit = orbit
        self.reference_system = reference_system
        self.regime = regime
        self.longitude = longitude
        self.semi_major_axis_km = semi_major_axis_km
        self.eccentricity = eccentricity
        self.periapsis_km = periapsis_km
        self.apoapsis_km = apoapsis_km
        self.inclination_deg = inclination_deg
        self.period_min = period_min
        self.lifespan_years = lifespan_years
        self.epoch = epoch
        self.mean_motion = mean_motion
        self.raan = raan
        self.arg_of_pericenter = arg_of_pericenter
        self.mean_anomaly = mean_anomaly
        self.id = id

        def __current_datetime_utc(value):
            if value is None:
                return None
            else:
                format_time_utc = "%Y-%m-%dT%H:%M:%S.%fZ"
                return datetime.strptime(value, format_time_utc)

        @property
        def epoch(self):
            return self._epoch

        @epoch.setter
        def epoch(self, value):
            self._epoch = __current_datetime_utc(value=value)


class Ships(Base):
    __tablename__ = "ships"
    legacy_id = Column(String)
    model = Column(String)
    type = Column(String)
    roles = Column(ARRAY(String))
    imo = Column(Integer)
    mmsi = Column(Integer)
    abs = Column(Integer)
    class_ship = Column(Integer)
    mass_kg = Column(Integer)
    mass_lbs = Column(Integer)
    year_built = Column(Integer)
    home_port = Column(String)
    status = Column(String)
    speed_kn = Column(Numeric)
    course_deg = Column(Numeric)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    last_ais_update = Column(String)
    link = Column(String)
    image = Column(String)
    launches = Column(ARRAY(String))
    name = Column(String)
    active = Column(Boolean)
    id = Column(String, primary_key=True)

    def __init__(
        self,
        legacy_id=None,
        model=None,
        type=None,
        roles=None,
        imo=None,
        mmsi=None,
        abs=None,
        class_ship=None,
        mass_kg=None,
        mass_lbs=None,
        year_built=None,
        home_port=None,
        status=None,
        speed_kn=None,
        course_deg=None,
        latitude=None,
        longitude=None,
        last_ais_update=None,
        link=None,
        image=None,
        launches=None,
        name=None,
        active=None,
        id=None,
    ):
        self.legacy_id = legacy_id
        self.model = model
        self.type = type
        self.roles = roles
        self.imo = imo
        self.mmsi = mmsi
        self.abs = abs
        self.class_ship = class_ship
        self.mass_kg = mass_kg
        self.mass_lbs = mass_lbs
        self.year_built = year_built
        self.home_port = home_port
        self.status = status
        self.speed_kn = speed_kn
        self.course_deg = course_deg
        self.latitude = latitude
        self.longitude = longitude
        self.last_ais_update = last_ais_update
        self.link = link
        self.image = image
        self.launches = launches
        self.name = name
        self.active = active
        self.id = id


class Rockets(Base):
    __tablename__ = "rockets"
    height = Column(JSON)
    diameter = Column(JSON)
    mass = Column(JSON)
    first_stage = Column(JSON)
    second_stage = Column(JSON)
    engines = Column(JSON)
    landing_legs = Column(JSON)
    payload_weights = Column(ARRAY(JSON))
    flickr_images = Column(ARRAY(String))
    name = Column(String)
    type = Column(String)
    active = Column(Boolean)
    stages = Column(Integer)
    boosters = Column(Integer)
    cost_per_launch = Column(Integer)
    success_rate_pct = Column(Integer)
    first_flight = Column(TIMESTAMP)
    country = Column(String)
    company = Column(String)
    wikipedia = Column(String)
    description = Column(String)
    id = Column(String, primary_key=True)

    def __init__(
        self,
        height=None,
        diameter=None,
        mass=None,
        first_stage=None,
        second_stage=None,
        engines=None,
        landing_legs=None,
        payload_weights=None,
        flickr_images=None,
        name=None,
        type=None,
        active=None,
        stages=None,
        boosters=None,
        cost_per_launch=None,
        success_rate_pct=None,
        first_flight=None,
        country=None,
        company=None,
        wikipedia=None,
        description=None,
        id=None
    ):
        self.height = height
        self.diameter = diameter
        self.mass = mass
        self.first_stage = first_stage
        self.second_stage = second_stage
        self.engines = engines
        self.landing_legs = landing_legs
        self.payload_weights = payload_weights
        self.flickr_images = flickr_images
        self.name = name
        self.type = type
        self.active = active
        self.stages = stages
        self.boosters = boosters
        self.cost_per_launch = cost_per_launch
        self.success_rate_pct = success_rate_pct
        self.first_flight = first_flight
        self.country = country
        self.company = company
        self.wikipedia = wikipedia
        self.description = description
        self.id = id
