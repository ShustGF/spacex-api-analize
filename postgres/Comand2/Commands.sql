CREATE TABLE test(id int PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, descr text);
CREATE SUBSCRIPTION test_sub CONNECTION 'host=server_public port=5432 user=postgres password=gfh0km dbname=replica_logical' PUBLICATION test_pub;