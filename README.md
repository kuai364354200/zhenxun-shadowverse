# shadowverse-index
适用于[hoshino](https://github.com/Ice9Coffee/HoshinoBot)的影之诗卡牌图鉴插件
> 卡牌信息来自[shadowverse-portal](https://shadowverse-portal.com/?lang=zh-tw)
做了zhenxunbot的移植
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
1. git clone本插件（注：一定要git clone，不要下载压缩包，另外请确保git环境变量正常）：

    在 HoshinoBot\hoshino\modules 目录下使用以下命令拉取本项目
    ```
    git clone https://github.com/Nao-desu/shadowverse-index.git
    ```
2. 安装依赖：

    到HoshinoBot\hoshino\modules\shadowverse-index目录下，管理员方式打开powershell
    ```
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --user
    ```
3. 在 HoshinoBot\hoshino\config\ `__bot__.py` 文件的 MODULES_ON 加入 'shadowverse-index'

4. 下载图片资源(约4GB)，有两种选择：
- 启动update.bat，可以自动下载
- [百度网盘下载](https://pan.baidu.com/s/1L6QglA5ICrte_JzD0ffEVA?pwd=szbb),下载完后将图片解压到shadowverse-index/pic文件夹下,并启动update.bat确认资源完整性

5. 重启hoshino