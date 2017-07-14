--credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' replace ABC and XYZ with user credentials
--Copy data from S3 into tables


--truncate Hospital data
copy hospdata from 's3://parimala-killada-bucket/original/hospital_data.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

--truncate Procedure code rates
copy proccode from 's3://parimala-killada-bucket/original/proccode.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

--truncate insurance details 
copy insurance from 's3://parimala-killada-bucket/original/final141516_v1.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

--truncate table claimsdata
copy claimsdata from 's3://medicalclaims-data/' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;
