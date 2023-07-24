MERGE INTO airflow_challenge.exchange_rate AS dst
USING (
    SELECT CAST(timestamp as TIMESTAMP) as timestamp, from_cur, to_cur, rate
    FROM airflow_challenge.exchange_rate_staging
) AS src
ON dst.timestamp = src.timestamp
AND dst.from_cur = src.from_cur
AND dst.to_cur = src.to_cur
WHEN MATCHED THEN
    UPDATE SET dst.rate = src.rate
WHEN NOT MATCHED THEN
    INSERT (timestamp, from_cur, to_cur, rate)
    VALUES (timestamp, from_cur, to_cur, rate)