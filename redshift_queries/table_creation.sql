DROP TABLE IF EXISTS hospprocoder;
CREATE TABLE hospprocoder(
proccode varchar(6) encode bytedict,
proceduredescription varchar(30) distkey,
inpout varchar(2) encode text255,
rate decimal encode delta,
year int encode delta,
provider_number varchar(5) encode bytedict,
hospital_name varchar(45) sortkey,
state varchar(2) encode raw,
zip_code varchar(6) encode bytedict,
county varchar(12) encode text255,
phone_number varchar(10) encode text255,
hospital_type varchar(20) encode text255,
hopital_ownership varchar(40) encode text255,
emergency_services varchar(20) encode text255
);
ROW FORMAT DELIMITED FIELDS TERMINATED BY '|' STORED AS TEXTFILE;
location 's3://medicalclaims-data';
