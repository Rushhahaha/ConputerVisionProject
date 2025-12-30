import os
import numpy as np
from PIL import Image
import random

# 创建测试数据集
def create_test_dataset():
    # 创建目录
    os.makedirs('data/mini_places/train_large', exist_ok=True)
    
    # 创建100张测试图片
    for i in range(100):
        # 随机大小 224-512之间
        size = random.randint(224, 512)
        # 随机颜色图片
        img_array = np.random.randint(0, 255, (size, size, 3), dtype=np.uint8)
        img = Image.fromarray(img_array)
        
        # 保存为jpg
        img.save(f'data/mini_places/train_large/{i:06d}.jpg')
    
    print(f"创建了100张测试图片到 data/mini_places/train_large/")
    
    # 创建目录结构文件（如果需要）
    with open('data/mini_places/train.txt', 'w') as f:
        for i in range(100):
            f.write(f'train_large/{i:06d}.jpg\n')

if __name__ == '__main__':
    create_test_dataset()