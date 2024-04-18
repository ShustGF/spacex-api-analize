CREATE TABLE starlink_satellites (
	spacetrack jsonb NULL,
	"version" text NULL,
	launch text NULL,
	longitude numeric NULL,
	latitude numeric NULL,
	height_km numeric NULL,
	velocity_kms numeric NULL,
	id text NOT NULL,
	dt_insert timestamp DEFAULT date_trunc('hour'::text, now())::timestamp without time zone NULL
);

CREATE TABLE launches (
	fairings jsonb NULL,
	links jsonb NULL,
	static_fire_date_utc timestamp NULL,
	static_fire_date_unix numeric NULL,
	tbd bool NULL,
	net bool NULL,
	"window" numeric NULL,
	rocket text NULL,
	success bool NULL,
	failures _jsonb NULL,
	details text NULL,
	crew _text NULL,
	ships _text NULL,
	capsules _text NULL,
	payloads _text NULL,
	launchpad text NULL,
	auto_update bool NULL,
	flight_number numeric NULL,
	"name" text NULL,
	date_utc timestamp NULL,
	date_unix numeric NULL,
	date_local text NULL,
	date_precision text NULL,
	upcoming bool NULL,
	cores _jsonb NULL,
	id text NULL,
	dt_insert timestamp DEFAULT date_trunc('hour'::text, now())::timestamp without time zone NULL
);

CREATE TABLE capsules (
	reuse_count numeric NULL,
	water_landings numeric NULL,
	land_landings numeric NULL,
	last_update text NULL,
	launches text[] NULL,
	serial text NULL,
	status text NULL,
	"type" text NULL,
	id text NULL,
	dt_insert timestamp DEFAULT date_trunc('hour'::text, now())::timestamp without time zone NULL
);

CREATE TABLE cores (
	"block" numeric NULL,
	reuse_count numeric NULL,
	rtls_attempts numeric NULL,
	rtls_landings numeric NULL,
	asds_attempts numeric NULL,
	asds_landings numeric NULL,
	last_update text NULL,
	launches text[] NULL,
	serial text NULL,
	status text NULL,
	id text NULL,
	dt_insert timestamp DEFAULT date_trunc('hour'::text, now())::timestamp without time zone NULL
);

CREATE TABLE crew (
	name text NULL,
	agency text NULL,
	image text NULL,
	wikipedia text NULL,
	launches text[] NULL,
	status text NULL,
	id text NULL,
	dt_insert timestamp DEFAULT date_trunc('hour'::text, now())::timestamp without time zone NULL
);

CREATE TABLE landpads (
	name text NULL,
	full_name text NULL,
	status text NULL,
	type text NULL,
	locality text NULL,
	region text NULL,
	latitude numeric NULL,
	longitude numeric NULL,
	landing_attempts integer NULL,
	landing_successes integer NULL,
	wikipedia text NULL,
	details text NULL,
	launches text[] NULL,
	id text NULL
);

CREATE TABLE launchpads (
	name text NULL,
	full_name text NULL,
	locality text NULL,
	region text NULL,
	timezone text NULL,
	latitude numeric NULL,
	longitude numeric NULL,
	launch_attempts integer NULL,
	launch_successes integer NULL,
	rockets text[] NULL,
	launches text[] NULL,
	status text NULL,
	id text NULL
);

CREATE TABLE payload (
	dragon jsonb NULL,
	name text NULL,
	type text NULL,
	reused bool NULL,
	launch text NULL,
	customers text[] NULL,
	norad_ids integer[],
	nationalities text[] NULL,
	manufacturers text[] NULL,
	mass_kg numeric NULL,
	mass_lbs numeric NULL,
	orbit text NULL,
	reference_system text NULL,
	regime text NULL,
	longitude numeric NULL,
	semi_major_axis_km numeric NULL,
	eccentricity numeric NULL,
	periapsis_km numeric NULL,
	apoapsis_km numeric NULL,
	inclination_deg numeric NULL,
	period_min numeric NULL,
	lifespan_years numeric NULL,
	epoch timestamp NULL,
	mean_motion numeric NULL,
	raan numeric NULL,
	arg_of_pericenter numeric NULL,
	mean_anomaly numeric NULL,
	id text NULL
);

CREATE TABLE ships (
	legacy_id text NULL,
	model text NULL,
	type text NULL,
	roles text[] NULL,
	imo integer NULL,
	mmsi integer NULL,
	abs integer NULL,
	class_ship integer NULL,
	mass_kg integer NULL,
	mass_lbs integer NULL,
	year_built integer NULL,
	home_port text NULL,
	status text NULL,
	speed_kn numeric NULL,
	course_deg numeric NULL,
	latitude numeric NULL,
	longitude numeric NULL,
	last_ais_update text NULL,
	link text NULL,
	image text NULL,
	launches text[] NULL,
	name text NULL,
	active bool NULL,
	id text NULL
);

CREATE TABLE rockets (
	height jsonb NULL,
	diameter jsonb NULL,
	mass jsonb NULL,
	first_stage jsonb NULL,
	second_stage jsonb NULL,
	engines jsonb NULL,
	landing_legs jsonb NULL,
	payload_weights jsonb[] NULL,
	flickr_images text[] NULL,
	name text NULL,
	type text NULL,
	active bool NULL,
	stages integer NULL,
	boosters integer NULL,
	cost_per_launch integer NULL,
	success_rate_pct integer NULL,
	first_flight timestamp NULL,
	country text NULL,
	company text NULL,
	wikipedia text NULL,
	description text NULL,
	id text NULL
);

CREATE SUBSCRIPTION db_test_sub CONNECTION 'host=server_public port=5432 user=postgres password=gfh0km dbname=replica_logical' PUBLICATION db_test_pub;