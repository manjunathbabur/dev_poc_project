-- Create a simple table
CREATE OR REPLACE TABLE POC_CICD_PY.PUBLIC.test_table (
    id INT,
    name STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
