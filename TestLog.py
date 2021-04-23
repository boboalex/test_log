#!/root/.pyenv/shims/python3
import os


class TestLog:
    def __init__(self):
        pass

    def count_sqls(self):
        file_path = "/home/qa/bozhang/Kyligence-Insight-1.2.5-testing/logs/studio.log"
        sql = """
SELECT SUM ("P_LINEORDER"."V_REVENUE") AS "V_REVENUE_SUM"
FROM "SSB_SF1"."P_LINEORDER" AS "P_LINEORDER"
LEFT OUTER JOIN "SSB_SF1"."DATES" AS "DATES" ON "P_LINEORDER"."LO_ORDERDATE" = "DATES"."D_DATEKEY"
LEFT OUTER JOIN "SSB_SF1"."CUSTOMER" AS "CUSTOMER" ON "P_LINEORDER"."LO_CUSTKEY" = "CUSTOMER"."C_CUSTKEY"
LEFT OUTER JOIN "SSB_SF1"."SUPPLIER" AS "SUPPLIER" ON "P_LINEORDER"."LO_SUPPKEY" = "SUPPLIER"."S_SUPPKEY"
LEFT OUTER JOIN "SSB_SF1"."PART" AS "PART" ON "P_LINEORDER"."LO_PARTKEY" = "PART"."P_PARTKEY"
ORDER BY "V_REVENUE_SUM" DESC
LIMIT 10000        
        """
        with open(file_path) as f:
            for line in f:
                if "LIMIT 10000" in line:
                    print(line)
if __name__ == '__main__':
    printlog = TestLog()
    printlog.count_sqls()