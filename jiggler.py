from random import random
import pyautogui as pag
import os 
import pandas as pd
import random

pause = 0.5 # 10秒待機させる？


def main():
  # main関数
  pag.PAUSE = pause
  width, height = pag.size() # 画面のサイズを取得
  width_range = monitor_length(width)
  height_range = monitor_length(height)
  current_dir = os.getcwd().replace(os.sep,'/') + '/' # pyファイル配下までのパスを取得
  path = current_dir + 'famous_quotes.xlsx'
  df = pd.read_excel(path)
  # print(width_range)
  # print(height_range)
    
  print("休んでくだされ～。暇なので名言で呟いときますわー。")
  print('やめるときはコマンドプロンプト/ターミナルを閉じるか、\nコマンドプロンプト/ターミナル上でctr + c(windows)/cmd + c(mac) やでー。\n')
  
  
  i = 5
  while True:
    try:
      pag.moveTo(random.choice(width_range), random.choice(height_range), duration=1) # カーソルをランダムに動かす
      print(str(random.choice(df['quote'])))
      print(str(random.choice(df['who'])))
      print()
      pag.sleep(10)
      i -= 1
      if i == 0:
        break
    except:
      print('お仕事頑張ってな！！！ほな！')
      break
  
def monitor_length(x):
  # 0 - モニターの長さまでの連続値を取得
  range_lst = []
  for i in range(0, x):
    range_lst.append(i+1)
  return range_lst

def type_random_words(string):
  pag.write(string)
  pag.press('enter')
  
if __name__ == "__main__":
  main()