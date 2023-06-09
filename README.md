# zhenxunbot-shadowverse-index
适用于[hoshino](https://github.com/Ice9Coffee/HoshinoBot)的影之诗卡牌图鉴插件
> 卡牌信息来自[shadowverse-portal](https://shadowverse-portal.com/?lang=zh-tw)
> 
> 环境 Python 3.10.7
# 做了zhenxunbot的移植
- v1.0 把源码的get_card改成了异步下载，提高了下载速度,可以直接执行py文件，也可以在bot中调用
## 代码来源

https://github.com/Nao-desu/shadowverse-index

## 功能
- `svcard id` 查询对应id的卡牌信息  
- `sv查卡 #条件 关键词` 查询卡牌信息，条件前要加#号进行区分,支持多条件,但是要在每个条件前都加#,关键词在卡牌名称与卡牌技能中匹配  
 支持的条件有:  
- `#3c` 指定费用为3  
- `#AOA` 指定卡包为遥久学园，也可用文字或文字简写  
- `#皇家` 指定职业为皇家  
- `#学园` 指定种类为学院  
- `#随从` 指定为随从卡  
- `#atk3` 指定攻击力为3  
- `#life3` 指定生命值为3  
- `#虹卡` 指定卡牌稀有度为传说

## 插件安装
1. git clone本插件：

    整个插件丢进插件文件夹里
2. 安装依赖：
    ```
    pip install -r requirements.txt
    ```
3. 下载图片资源(约4GB)，有两种选择：
    bot打指令：更新影之诗图片
