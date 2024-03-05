import pywifi
import time
import requests
#抓post包  补充下面信息
url = "http://10.101.2.205:8081/aaa-auth/api/v1/auth"
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://10.101.2.194:6060",
    "Referer": "http://10.101.2.194:6060/",
    "User-Agent": "curl/7.68.0"
}
data = {
    "campusCode": "3def184ad8f4755ff269862ea77393dd,1afa34a7f984eeabdbb0a7d494132ee5,65ded5353c5ee48d0b7d48c591b8f430",
    "username": "",
    "password": "",
    "operatorSuffix": ""
}

def isConnected():
    if ifaces.status() == pywifi.const.IFACE_CONNECTED:
        print("成功连接")
        return True
    else:
        print("连接失败")
        return False

if __name__ == "__main__":
    wifi = pywifi.PyWiFi()  # 创建一个无线对象
    ifaces = wifi.interfaces()[0]  # 取一个无线网卡
    print(ifaces.name())  # 输出无线网卡名称
    ifaces.disconnect()  # 断开网卡连接
    time.sleep(0.5)  # 缓冲0.5秒

    profile = pywifi.Profile()  # 配置文件
    profile.ssid = "WiFi名称"  # WiFi名称
    ifaces.remove_all_network_profiles()  # 删除其他配置文件
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
    ifaces.connect(tmp_profile)  # 连接
    time.sleep(0.5)  # 等待0.5秒后检查是否成功连接

    if isConnected():
        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            print("请求成功！")
            print("响应内容：", response.text)
        else:
            print("请求失败，状态码：", response.status_code)

        baidu=requests.get('https://www.baidu.com')
        print(baidu.status_code)    
    input()
