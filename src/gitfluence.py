import sys
import json
import urllib.request





# 获取输入内容
query = sys.argv[1]


def main():
    # 构造请求数据
    data = {"prompt": query}
    data = json.dumps(data).encode('utf-8')

    # 构造请求对象
    req = urllib.request.Request(url="https://www.gitfluence.com/api/generate", data=data, headers={'Content-Type': 'application/json'})

    # 发送POST请求
    response = urllib.request.urlopen(req)

    # 获取响应结果
    responseText = response.read().decode('utf-8')

    # 输出结果
    print(responseText.replace('```','').replace('\n',''))


if __name__ == "__main__":
    main()
