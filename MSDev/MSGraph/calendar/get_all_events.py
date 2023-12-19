import httpx
import json
import toml
from pathlib import Path

# 解析 config.toml
CONFIG_PATH = Path(__file__).parent / "config.toml"
CONFIG = toml.load(CONFIG_PATH)
TOKEN = CONFIG["token"]

# Setting up the headers as specified in the PowerShell request
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "Bearer " + TOKEN,  # Replace with actual token
    "DNT": "1",
    "Origin": "https://developer.microsoft.com",
    "Referer": "https://developer.microsoft.com/",
    "SdkVersion": "GraphExplorer/4.0, graph-js/3.0.7 (featureUsage=6)",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "X-Edge-Shopping-Flag": "1",
    "cache-control": "no-cache",
    "client-request-id": "65109419-c2d2-dcc7-c2bf-5c29e824b4c9",
    "pragma": "no-cache",
    "prefer": "ms-graph-dev-mode",
    "sec-ch-ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

# Specifying the user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"


def decode_unicode_to_chinese(unicode_str):
    """
    Decodes a Unicode escape sequence to its corresponding Chinese characters.

    :param unicode_str: A string containing Unicode escape sequences.
    :return: A string of Chinese characters.
    """
    # 尝试将 unicode_str 转换为 unicode 编码
    try:
        decode_str = unicode_str.encode("latin1").decode("unicode-escape")
    except Exception as e:
        decode_str = unicode_str
        print(f"Error: {e}\nunicode_str: {unicode_str}")
    return decode_str


# Example usage
# input_unicode = "\\u54b8\\u9c7c\\u578b"
# decoded_chinese = decode_unicode_to_chinese(input_unicode)
# decoded_chinese


def get_recent_10_events_in_my_calendar():
    url = "https://graph.microsoft.com/v1.0/me/events?$select=subject,body,bodyPreview,organizer,attendees,start,end,location"

    # Creating the HTTP client with the specified user agent
    client = httpx.Client(headers={"User-Agent": user_agent})

    # Making the GET request
    response = client.get(url, headers=headers).json()

    # 解析返回的 json, 将其分割为 data_context_link, value_list, data_next_link
    data_context_link = response["@odata.context"]
    value_list = response["value"]
    # 如果返回的 json 中有 @odata.nextLink, 则将其赋值给 data_next_link, 否则将其赋值为 None
    if "@odata.nextLink" in response:
        data_next_link = response["@odata.nextLink"]
    else:
        data_next_link = None
    return value_list, data_next_link


def get_all_events_in_my_calendar():
    # 获取最近 10 个日历事件
    value_list, data_next_link = get_recent_10_events_in_my_calendar()

    # 如果 data_next_link 不为 None, 则继续获取后续的日历事件
    while data_next_link is not None:
        # 创建 HTTP 客户端
        client = httpx.Client(headers={"User-Agent": user_agent})

        # 发送 GET 请求
        response = client.get(data_next_link, headers=headers).json()

        # 解析返回的 json, 将其分割为 data_context_link, value_list, data_next_link
        value_list += response["value"]
        # 如果返回的 json 中有 @odata.nextLink, 则将其赋值给 data_next_link, 否则将其赋值为 None
        if "@odata.nextLink" in response:
            data_next_link = response["@odata.nextLink"]
        else:
            data_next_link = None

    print(f"len(value_list): {len(value_list)}\n==========\nvlaue_list: {value_list}")
    return value_list


if __name__ == "__main__":
    get_all_events_in_my_calendar()
