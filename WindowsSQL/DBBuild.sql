CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'barth010mew';
GO
/*  specify credentials to external data source
*  IDENTITY: user name for external source.  
*  SECRET: password for external source.
*/
CREATE DATABASE SCOPED CREDENTIAL mongovv 
WITH IDENTITY = 'mongotrevor', Secret = 'd1ngbat';
GO
/*  LOCATION: Location string should be of format '<type>://<server>[:<port>]'.
*  PUSHDOWN: specify whether computation should be pushed down to the source. ON by default.
*CONNECTION_OPTIONS: Specify driver location
*  CREDENTIAL: the database scoped credential, created above.
*/  
CREATE EXTERNAL DATA SOURCE mongovv
WITH (
TYPE = BLOB_STORAGE,
LOCATION = 'mongodb://10.211.55.2:6173', --mongotrevor:d1ngbat@10.211.55.2:6173
-- PUSHDOWN = ON | OFF,
 CREDENTIAL = mongovv
);
GO
/*  LOCATION: MongoDB table/view in '<database_name>.<schema_name>.<object_name>' format
*  DATA_SOURCE: the external data source, created above.
*/
CREATE EXTERNAL TABLE Tweets(
Tweets NVARCHAR(MAX) NOT NULL
)
WITH (
LOCATION='Tweets',
DATA_SOURCE= mongovv
);
GO