学习笔记

常用 pip 源地址
豆瓣： https://pypi.doubanio.com/simple/
清华： https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
中科大： https://pypi.mirrors.ustc.edu.cn/simple/
阿里云： https://mirrors.aliyun.com/pypi/simple/
修改方式
临时替换

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

永久替换（先升级 pip：pip install pip -U ）

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple


