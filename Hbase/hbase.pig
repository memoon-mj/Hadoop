users = LOAD '/user/maria_dev/data3/u.user'
        USING PigStorage('|')
        AS (userID:int, age:int, gender:chararray, occupation:chararray, zip:int);

STORE users INTO 'hbase://users'
    USING org.apache.pig.backend.hadoop.hbase.HBaseStorage (
        'userinfo:age, userinfo:gender, userinfo:occupation, userinofo:zip');