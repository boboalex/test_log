#!/root/.pyenv/shims/python3

import requests
import multiprocessing

class BatchClient:
    def __init__(self):
        self._headers = {'Accept': 'application/vnd.apache.kylin-v2+json',
                         'Accept-Language': 'en',
                         'Content-Type': 'application/json;charset=utf-8'
                         }
        self._auth = ('ADMIN', 'kylin@2020')

    def batch_query(self):
        sql = """
            SELECT SUM ("P_LINEORDER"."V_REVENUE") AS "V_REVENUE_SUM"
            FROM "SSB_SF1"."P_LINEORDER" AS "P_LINEORDER"
            LEFT OUTER JOIN "SSB_SF1"."DATES" AS "DATES" ON "P_LINEORmuDER"."LO_ORDERDATE" = "DATES"."D_DATEKEY"
            LEFT OUTER JOIN "SSB_SF1"."CUSTOMER" AS "CUSTOMER" ON "P_LINEORDER"."LO_CUSTKEY" = "CUSTOMER"."C_CUSTKEY"
            LEFT OUTER JOIN "SSB_SF1"."SUPPLIER" AS "SUPPLIER" ON "P_LINEORDER"."LO_SUPPKEY" = "SUPPLIER"."S_SUPPKEY"
            LEFT OUTER JOIN "SSB_SF1"."PART" AS "PART" ON "P_LINEORDER"."LO_PARTKEY" = "PART"."P_PARTKEY"
            ORDER BY "V_REVENUE_SUM" DESC
            LIMIT 10000        
                """
        payload = {

        }
        url = "http://10.1.3.29:9111/superset/explore_json/?form_data=%7B%22slice_id%22%3A1%7D"
        resp = requests.request("GET", url=url, headers=self._headers, params=payload, auth=self._auth)
        print(resp.status_code)
count = 0
def execute(request, n):
    for i in range(n):
        global count
        count += 1
        request.batch_query()

if __name__ == '__main__':
    client = BatchClient()
    p = multiprocessing.Pool(10)
    for i in range(10):
        p.apply_async(execute, args=(client, 1,))
    p.close()
    p.join()
    print(f"executing count is {count}")


