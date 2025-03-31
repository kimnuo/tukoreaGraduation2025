import torch
import torchvision
print(torch.cuda.is_available())  # True이면 GPU 정상 작동
print(torch.cuda.get_device_name(0))  # 사용 중인 GPU 모델 확인
print(torch.version.cuda)  # PyTorch에서 사용하는 CUDA 버전
print(torch.__version__)  # PyTorch 버전
print(torchvision.__version__)  # torchvision 버전