#!/bin/bash
set -e

clickhouse-client -q "CREATE TABLE ${CLICKHOUSE_DB}.launches (
	fairings String NULL,
	links String NULL,
	static_fire_date_utc DateTime NULL,
	static_fire_date_unix Decimal(38, 19) NULL,
	tbd bool NULL,
	net bool NULL,
	"window" Decimal(38, 19) NULL,
	rocket String NULL,
	success bool NULL,
	failures String NULL,
	details String NULL,
	crew String NULL,
	ships String NULL,
	capsules String NULL,
	payloads String NULL,
	launchpad String NULL,
	auto_update bool NULL,
	flight_number Decimal(38, 19) NULL,
	"name" String NULL,
	date_utc timestamp NULL,
	date_unix Decimal(38, 19) NULL,
	date_local String NULL,
	date_precision String NULL,
	upcoming bool NULL,
	cores String NULL,
	id String NULL
)
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'launches', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"

for table in starlink_satellites capsules cores crew landpads launchpads payload ships rockets
do
clickhouse-client -q "CREATE TABLE ${CLICKHOUSE_DB}.$table ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', '$table', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
done