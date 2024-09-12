from PIL import Image
import os


file_path = "output/rubble_1/eval/ours_10000/gt"
# 打开图片文件
files = os.listdir(file_path)
files = [os.path.join(file_path, file) for file in files]
for file in files:
    img = Image.open(file)  # 请将'path_to_your_image.jpg'替换成你的图片文件路径
    # 调整图片大小到1152x864
    img_resized = img.resize((1152, 864))
    # 保存调整大小后的图片
    img_resized.save(file)  # 指定保存路径和文件名