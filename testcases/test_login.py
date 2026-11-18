import requests

def test_httpbin_smoke():
    # 带上 User-Agent 伪装成浏览器（好习惯）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # 使用 httpbin 这个专门供测试使用的接口，它一定会返回 200
    response = requests.get("https://httpbin.org/get", headers=headers)

    print("\n响应内容:", response.text)

    # 断言状态码
    assert response.status_code == 200
    # 断言返回的 JSON 中 url 字段正确
    assert response.json()["url"] == "https://httpbin.org/get"