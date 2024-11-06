from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .phi_model import PhiModel  # 假设 phi_model.py 文件在同一应用中

# 初始化模型
model = PhiModel()

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            
            # 调用模型生成回复
            model_response = model.generate_response(user_message)
            
            # 返回模型的响应
            return JsonResponse({'response': model_response}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def chat_test(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # 解析请求体中的 JSON 数据
            message = data.get("message", "")
            # 处理消息并生成回复
            response = {"reply": f"Received: {message}"}
            return JsonResponse(response)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

