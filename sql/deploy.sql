-- Deploy script to create the table and insert data
!source create_tables.sql;
!source insert_data.sql;

-- Verify the data
SELECT * FROM POC_CICD_PY.PUBLIC.test_table;
