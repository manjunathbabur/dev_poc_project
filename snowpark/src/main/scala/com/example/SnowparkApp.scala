package com.example

import com.snowflake.snowpark._

object SnowparkApp {
  def main(args: Array[String]): Unit = {
    // Create a Snowflake session
    val session = Session.builder.configFile("application.conf").create()

    // Query the test table
    val df = session.sql("SELECT * FROM test_table")
    df.show()

    // Close the session
    session.close()
  }
}
