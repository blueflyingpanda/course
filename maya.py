import pandas as pd
import requests

API_KEY = "2JJbLdqDi6f9yp9nPMQdCzGjGLk"
BASE_URL = "https://api.glassnode.com/v1/metrics/addresses/"
TIMEOUT = 300

links_for_request = {
    "001": "active_count",
    "002": "sending_count",
    "003": "receiving_count",
}

# Initialize an empty DataFrame
result = pd.DataFrame({"t": [1]})

# Iterate over the links_for_request dictionary
for k, v in links_for_request.items():
    res = requests.get(
        BASE_URL + v, params={"a": "BTC", "api_key": API_KEY}, timeout=TIMEOUT
    )
    if not res.ok:
        raise Exception("Request failed")
    df = pd.read_json(res.text, convert_dates=["t"])
    df.rename(columns={"v": k}, inplace=True)
    if k == "001":
        result = df
    else:
        result = pd.merge(result, df, how="outer", on="t")
