CREATE TABLE starlink_satellites (
	spacetrack jsonb NULL,
	"version" text NULL,
	launch text NULL,
	longitude numeric NULL,
	latitude numeric NULL,
	height_km numeric NULL,
	velocity_kms numeric NULL,
	id text NOT NULL,
	CONSTRAINT starlink_satellites_pk PRIMARY KEY (id)
);
CREATE PUBLICATION starlink_pub FOR TABLE starlink_satellites;