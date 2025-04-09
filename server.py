from flask import Flask, request, jsonify
import json


json_data = {}
name_lst = ["faq", "tags", "ownermap",]
name_lst2 = ["hotkey_ai","usually_ai","age_ai"]
for i in name_lst:
    with open(f"{i}.json", "r", encoding="utf-8") as f:
        json_data[i] = json.loads(f.read().replace('\n', '').replace(' ', ''))
for i in name_lst2:
    with open(f"{i}.json", "r", encoding="utf-8") as f:
        json_data[i] = f.read()


app = Flask(__name__)

# 基础路由示例：访问根路径返回欢迎信息
@app.route('/')
def home():
    return "Welcome to the server! Send requests to /api"

# 处理 GET 请求示例
@app.route('/api', methods=['GET'])
def handle_get():
    # 获取请求参数
    auth_token = request.headers.get('hahahaxixixi')
    if auth_token != 'aabbcc':
        return jsonify({"error": "Unauthorized"}), 401
    name = request.args.get('name', 'Guest')
    return jsonify({"message": json_data, "method": "GET"})


# 处理 POST 请求示例
@app.route('/api', methods=['POST'])
def handle_post():
    # 获取 JSON 请求体
    data = request.json
    return jsonify({"received_data": data, "method": "POST"})

# # 自定义响应路由
# @app.route('/custom', methods=['GET'])
# def custom_response():
#     return jsonify({"status": "success", "code": 200})


if __name__ == '__main__':
    # 启动服务 (默认端口 5000)
    app.run(host='172.17.200.162', port=11234, debug=True)