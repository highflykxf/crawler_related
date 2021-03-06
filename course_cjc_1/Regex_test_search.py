#-*- coding:utf-8 -*-
#导入re模块
import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = re.search(pattern,'hello world!')
if match:
    # 使用Match获得分组信息
    print match.group()
### 输出 ###
# world

pattern = re.compile(r'\d+')
print re.split(pattern,'one1two2three3four4')

print re.findall(pattern,"one1two2three3four4")

for m in re.finditer(pattern,'one1two2three3four4'):
    print m.group()