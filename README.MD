# 团课学习
灵感来源于[tk-auto-study](https://github.com/838239178/tk-auto-study)
## 说明
因为我不能领取百度api的免费额度  
而且验证码比较简单，只有数字，颜色区分度较大  
所以使用了pytesseract进行验证码识别
## 使用方法
###### 1.普通部署
以ubuntu18.04为例  
安装依赖
```
sudo apt update && \
sudo apt install libopenjp2-7 && \
sudo apt install libtiff5 && \
sudo apt install tesseract-ocr
```
```
pip3 install setuptools wheel && \
pip3 install Pillow && \
pip3 install -r requirements.txt
```
设置用户名和密码
```
export USERNAME=用户名 && export PASSWORD=密码
```
运行脚本
```
python3 main.py
```
脚本将在每周一早上十点运行  
请配合tmux systemd等工具使用
###### 2.docker部署
```
docker build . -t auto-tk:1.0.0
docker run -e USERNAME="" -e PASSWORD="" -d auto-tk:1.0.0
```
引号内填入用户名以及密码
###### 3.Actions
1. fork本项目
2. 进入项目的Settings添加secrets
- USERNAME
- PASSWORD
- PUBLIC_KEY 可不填
```MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKf9iZkA5HEFw4zt7MRBkcmgUiz5+r5eqDOKbaurEbScmXd3ZZTtyzirqkYKRIH5mQ+8hq+Wd/pTZNXHS8L0+88CAwEAAQ==```
- MAX_TRIES 默认为5 可不填
3. 手动运行，测试是否可用

## 声明
本项目仅用于python学习，请自己学习团课，请勿偷懒  
富强、民主、文明、和谐;自由、平等、公正、法治;爱国、敬业、诚信、友善