import requests
import os,json
from os.path import join
from PIL import Image
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
MOUDULE_PATH = os.path.dirname(__file__)
def get_info(proxies=None):
     #获取卡牌信息
     url = 'https://shadowverse-portal.com/api/v1/cards'
     a = requests.get(url,params={"format":"json","lang":"zh-tw"},proxies=proxies)
     tw = json.loads(a.text)["data"]["cards"]
     nonamecard = []
     for i in tw:
          if i["card_name"] == None:
               print(f'remove  {i["card_id"]}')
               nonamecard.append(i)#筛选无名卡牌，一般为其他卡牌的激奏和结晶占位
          else:
               print(i["card_name"])
          if i["char_type"] == 3:
               i["char_type"] = 2
     for i in nonamecard:
          tw.remove(i)#删除无名卡
     with open(join(MOUDULE_PATH,"cardinfo_tw.json"),'w', encoding="utf-8") as f:
          json.dump(tw, f, indent=4, ensure_ascii=False)
     #获取图片
     #获取图片
     img_url_e = 'https://shadowverse-portal.com/image/card/phase2/common/E/E_'#进化卡牌图片
     img_url_c = 'https://shadowverse-portal.com/image/card/phase2/common/C/C_'#卡牌图片
     img_url_l = 'https://shadowverse-portal.com/image/card/phase2/common/L/L_'#卡图片段
     name_url_tw = 'https://shadowverse-portal.com/image/card/phase2/zh-tw/N/N_'#卡牌名称
     cost_url = 'https://shadowverse-portal.com/public/assets/image/common/global/cost_'#cost图片
     cardnum = len(tw)
     count = 1
     if not os.path.exists(f'pic/'):
          os.mkdir('pic/')
     if not os.path.exists(f'cost/'):
          os.mkdir('cost/')
     if not os.path.exists(f'lpic/'):
          os.mkdir('lpic/')
     with ThreadPoolExecutor(max_workers=100) as t:
          def downcost(i, proxies):
               # 获取cost图片
               if not os.path.exists(join(MOUDULE_PATH, f'cost/{i}.png')):
                    cost_pic = requests.get(f'{cost_url}{i}.png', proxies=proxies)
                    print(f'downloading cost{i}.png')
                    with open(join(MOUDULE_PATH, f'cost/{i}.png', ), 'wb') as img:
                         img.write(cost_pic.content)
                    print(f'savied cost{i}.png')
               else:
                    print(f'cost{i} already exists,pass')
          for i in range(0, 31):
               t.submit(downcost,i,proxies)
          def downpic_L(i,count,proxies):
               #获取卡图片段
               if not os.path.exists(join(MOUDULE_PATH, f'lpic/L_{i["card_id"]}.jpg')):
                    card_pic = requests.get(f'{img_url_l}{i["card_id"]}.jpg',proxies=proxies)
                    print(f'downloading {i["card_name"]}-L ({count}/{cardnum})')
                    with open(join(MOUDULE_PATH, f'lpic/L_{i["card_id"]}.jpg', ), 'wb') as img:
                         img.write(card_pic.content)
                    print(f'saved {i["card_name"]}-L ({count}/{cardnum})')
               else:
                    print(f'{i["card_name"]}-L already exists,pass ({count}/{cardnum})')
               #获取卡牌图片
          def downpic_C(i,count,proxies):
               if not os.path.exists(join(MOUDULE_PATH, f'pic/C_{i["card_id"]}.png')):
                    if i["card_id"] == 910441030:
                         card_pic = requests.get(f'{img_url_c}{i["card_id"] - 10}.png', proxies=proxies)
                         # 爆破模式没有进化前卡面，另外两个有，替代一下
                    else:
                         card_pic = requests.get(f'{img_url_c}{i["card_id"]}.png', proxies=proxies)

                    card_name = requests.get(f'{name_url_tw}{i["card_id"]}.png', proxies=proxies)
                    print(f'generating {i["card_name"]}-C ({count}/{cardnum})')
                    pic = Image.open(BytesIO(card_pic.content))
                    name = Image.open(BytesIO(card_name.content))
                    xn, yn = name.size
                    # 调整文字大小
                    k = 40 / yn
                    newsize = (int(xn * k), 40)
                    move = False
                    if xn * k >= 300:
                         k = 340 / xn
                         newsize = (340, int(yn * k))
                         move = True
                    name = name.resize(newsize, resample=Image.LANCZOS)
                    xn, yn = name.size
                    if move:
                         left = int(290 - xn / 2)
                    else:
                         left = int(268 - xn / 2)
                    top = int(95 - yn / 2)
                    pic.paste(name, (left, top), name)
                    pic.save(join(MOUDULE_PATH, f'pic/C_{i["card_id"]}.png'), 'PNG')
                    print(f'saved {i["card_name"]}-C:pic/E_{i["card_id"]}.png({count}/{cardnum})')
               else:
                    print(f'{i["card_name"]}-C already exidsts,pass ({count}/{cardnum})')
               #获取进化卡牌图片
          def downpic_E(i,count,proxies):
               if i["char_type"] == 1:
                    if not os.path.exists(join(MOUDULE_PATH, f'pic/E_{i["card_id"]}.png')):
                         card_pic = requests.get(f'{img_url_e}{i["card_id"]}.png', proxies=proxies)
                         card_name = requests.get(f'{name_url_tw}{i["card_id"]}.png', proxies=proxies)
                         print(f'generating {i["card_name"]}-E ({count}/{cardnum})')
                         pic = Image.open(BytesIO(card_pic.content))
                         name = Image.open(BytesIO(card_name.content))
                         xn, yn = name.size
                         # 调整文字大小
                         k = 40 / yn
                         newsize = (int(xn * k), 40)
                         move = False
                         if xn * k >= 300:
                              k = 340 / xn
                              newsize = (340, int(yn * k))
                              move = True
                         name = name.resize(newsize, resample=Image.LANCZOS)
                         xn, yn = name.size
                         if move:
                              left = int(290 - xn / 2)
                         else:
                              left = int(268 - xn / 2)
                         top = int(95 - yn / 2)
                         pic.paste(name, (left, top), name)
                         pic.save(join(MOUDULE_PATH, f'pic/E_{i["card_id"]}.png'), 'PNG')
                         print(f'saved {i["card_name"]}-E:pic/E_{i["card_id"]}.png({count}/{cardnum})')
                    else:
                         print(f'{i["card_name"]}-E already exists,pass ({count}/{cardnum})')
          for i in tw:
               t.submit(downpic_L, i, count,proxies)
               t.submit(downpic_C, i, count, proxies)
               t.submit(downpic_E, i, count, proxies)
               count = count+1
     print("all finished!")
     return 0

if __name__=='__main__':
     proxies = {'http':'http://127.0.0.1:4780'}
     get_info(proxies=proxies)