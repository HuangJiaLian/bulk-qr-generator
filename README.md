# bulk-qr-generator

## 介绍

这是一个QR码批量生成器。按行读取文本中的字符，批量生成QR码。

## 使用说明

### 安装`qrcode`库

``` bash
(sudo) pip install qrcode
```

### 批量生成QR码
1. 将要待生成文本按行保存在文本文件(如name.txt)中
```
Nana
Dylan
Jack
Kim
Peter
```
2. 运行
``` python
python QR_Gen.py name.txt
```
那么在当前文件夹下便会批量生成名字对应的QR码。
``` 
Dylan.png  Jack.png  Kim.png  Nana.png  Peter.png
```


 