import pytest
import snowflake.connector

@pytest.fixture
def connection():
    return snowflake.connector.connect(
        user="your_user",
        password="your_password",
        account="your_account"
    )

def test_table_exists(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES LIKE 'TEST_TABLE'")
    assert len(cursor.fetchall()) > 0

def test_data_exists(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM TEST_TABLE")
    assert cursor.fetchone()[0] > 0
