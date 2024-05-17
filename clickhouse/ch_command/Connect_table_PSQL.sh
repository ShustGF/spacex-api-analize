#!/bin/bash
set -e

clickhouse-client -q "CREATE TABLE my_database.starlink_satellites ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'starlink_satellites', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
clickhouse-client -q "CREATE TABLE my_database.launches (
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
clickhouse-client -q "CREATE TABLE my_database.capsules
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'capsules', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
clickhouse-client -q "CREATE TABLE my_database.cores 
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'cores', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
clickhouse-client -q "CREATE TABLE my_database.crew 
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'crew', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
clickhouse-client -q "CREATE TABLE my_database.landpads 
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'landpads', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
clickhouse-client -q "CREATE TABLE my_database.launchpads 
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'launchpads', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
clickhouse-client -q "CREATE TABLE my_database.payload 
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'payload', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
clickhouse-client -q "CREATE TABLE my_database.ships 
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'ships', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"
clickhouse-client -q "CREATE TABLE my_database.rockets 
ENGINE = PostgreSQL('server_subscription:5432', 'postgres_subscriber', 'rockets', 'postgres', '$POSTGRES_SUBSCRIPTION_PASSWORD');"