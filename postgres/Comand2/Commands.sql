CREATE TABLE starlink_satellites (
	spacetrack jsonb NULL,
	"version" text NULL,
	launch text NULL,
	longitude numeric NULL,
	latitude numeric NULL,
	height_km numeric NULL,
	velocity_kms numeric NULL,
	id text NOT NULL,
	dt_insert timestamp DEFAULT date_trunc('hour'::text, now())::timestamp without time zone NULL,
	CONSTRAINT starlink_satellites_pk PRIMARY KEY (id)
);
CREATE SUBSCRIPTION starlink_sub CONNECTION 'host=server_public port=5432 user=postgres password=gfh0km dbname=replica_logical' PUBLICATION starlink_pub;