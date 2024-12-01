import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)

# bash eval.sh  /path/to/your/config /path/to/your/checkpoint
# bash eval.sh  configs/resnet_50_culane.py checkpoints/model_res50_normal
