package com.example

import org.scalatest.funsuite.AnyFunSuite
import com.snowflake.snowpark._

class SnowparkAppTest extends AnyFunSuite {
  test("Snowflake connection test") {
    val session = Session.builder.configFile("application.conf").create()
    val df = session.sql("SELECT 1 AS test_value")
    assert(df.collect()(0).getInt(0) == 1)
    session.close()
  }
}
