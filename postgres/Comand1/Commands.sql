CREATE TABLE starlink_satellites (
	spacetrack jsonb NULL,
	"version" text NULL,
	launch text NULL,
	longitude numeric NULL,
	latitude numeric NULL,
	height_km numeric NULL,
	velocity_kms numeric NULL,
	id text NOT NULL
);
CREATE PUBLICATION starlink_pub FOR TABLE starlink_satellites;
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
	id text NULL
);
CREATE PUBLICATION launches_pub FOR TABLE launches;
CREATE TABLE capsules (
	reuse_count numeric NULL,
	water_landings numeric NULL,
	land_landings numeric NULL,
	last_update text NULL,
	launches text[] NULL,
	serial text NULL,
	status text NULL,
	"type" text NULL,
	id text NULL
);
CREATE PUBLICATION capsules_pub FOR TABLE capsules;
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
	id text NULL
);
CREATE PUBLICATION cores_pub FOR TABLE cores;