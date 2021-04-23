import requests


if __name__ == '__main__':

    url = "http://10.1.3.29:9111/superset/explore_json/?form_data=%7B%22slice_id%22%3A1%7D"

    payload = {}
    headers = {
      'Connection': 'keep-alive',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
      'X-CSRFToken': '',
      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryiX9xjdT8zOzlivYf',
      'Accept': '*/*',
      'Origin': 'http://10.1.3.29:9111',
      'Referer': 'http://10.1.3.29:9111/superset/explore/?form_data=%7B%22datasource%22%3A%221__kylin%22%2C%22slice_id%22%3A1%2C%22url_params%22%3A%7B%7D%2C%22viz_type%22%3A%22table%22%2C%22adhoc_filters%22%3A%5B%5D%2C%22groupby%22%3A%5B%5D%2C%22metrics%22%3A%5B%22V_REVENUE_SUM%22%5D%2C%22timeseries_limit_metric%22%3Anull%2C%22order_desc%22%3Atrue%2C%22row_limit%22%3A10000%2C%22granularity_sqla_timeshift%22%3Anull%2C%22time_grain_timeshift%22%3A%22%22%2C%22concurrent_values%22%3A%5B%5D%2C%22growth_values%22%3A%5B%5D%2C%22growth_rates%22%3A%5B%5D%2C%22month_to_date%22%3A%5B%5D%2C%22year_to_date%22%3A%5B%5D%2C%22page_length%22%3A100%2C%22include_search%22%3Afalse%7D',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cookie': 'session=.eJw1j01qxDAMha8SvJ6F7fhHylUmYbAtiRTSaYnjTYe5ewWlGz099CQ-vcxDjtJ37ma5v8x0qZg-WuPezc2sIybhdQAkmO7rSJGtVrB5HQgIbps0QuLXEYRI-xrBbO_tpndP7rtZrnOwug8yiyHvSp1DSBLCbGML1dcWskNGyHm2niRnJoZYUysCAtHFgCVWi8V5wdmiECbmwomSVGkFKTXvlI9jVQ8UnO7N7Cm5QBllTtZHRqnO6kePbz4_y5Of1z_a8dXKwUr3s-t8dD7_YJ15_wJIhFWS.X4XP5w.4M7Qo3btauC3efC3UXnQZxI2vQs; session=.eJwlzjEKwzAMQNG7eM5g2bJs5TLBsiRSCBSSZmnp3Wvo-IYP_xM2P-3aw_o6b1vC9tCwBk3QJSOSI-ZYBkqSgRXYuNWaY1Kv1dRaERrdm7cCBbkXidwhOefIrkxm3UjJxUdnpZGgUbMi000RZpctKQFqZc8UUzF2gRiWcDxHP2y-vPep-7Lzvwbh-wNtMDPW.X4XcAw.wzqVEoStDg3LYwhc59bLQWU6mSU',
      'Authorization': 'Basic QURNSU46a3lsaW5AMjAyMA=='
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
