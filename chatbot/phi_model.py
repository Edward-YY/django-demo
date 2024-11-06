from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class PhiModel:
    def __init__(self):
        # 将模型和分词器加载到 GPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # 加载模型和分词器
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3.5-mini-instruct")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3.5-mini-instruct").to(self.device)

    def generate_response(self, input_text):
        # 将输入文本编码为模型的输入格式
        #inputs = self.tokenizer.encode(input_text, return_tensors="pt")

        #对输入进行编码
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True).to(self.device)
        # 手动添加 attention_mask
        attention_mask = inputs['attention_mask']

        # 使用模型生成回复
        with torch.no_grad():
            outputs = self.model.generate(inputs["input_ids"], attention_mask=attention_mask, max_length=50)
        
        # 解码并返回生成的文本
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return response
