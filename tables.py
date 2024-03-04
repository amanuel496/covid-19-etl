FACT_COVID_TABLE = """
        CREATE TABLE "fact_covid" (
            "index" INTEGER,
            "fips" REAL,
            "province_state" TEXT,
            "country_region" TEXT,
            "confirmed" REAL,
            "deaths" REAL,
            "recovered" REAL,
            "active" REAL,
            "date" INTEGER,
            "positive" INTEGER,
            "negative" REAL,
            "hospitalizedcurrently" REAL,
            "hospitalized" REAL,
            "hospitalizeddischarged" REAL
        )
    """

DIM_REGION_TABLE = """
        CREATE TABLE "dim_region" (
            "index" INTEGER,
            "fips" REAL,
            "province_state" TEXT,
            "country_region" TEXT,
            "latitude" REAL,
            "longitude" REAL,
            "county" TEXT,
            "state" TEXT
        )
    """

DIM_DATE_TABLE = """
        CREATE TABLE "dim_date" (
            "index" INTEGER,
            "fips" REAL,
            "date" TIMESTAMP,
            "year" INTEGER,
            "month" INTEGER,
            "day_of_week" INTEGER
        )
    """

DIM_HOSPITAL_TABLE = """
        CREATE TABLE "dim_hospital" (
            "index" INTEGER,
            "fips" REAL,
            "state_name" TEXT,
            "latitude" REAL,
            "longtitude" REAL,
            "hq_address" TEXT,
            "hospital_name" TEXT,
            "hospital_type" TEXT,
            "hq_city" TEXT,
            "hq_state" TEXT
        )
    """
