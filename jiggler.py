import pyautogui as pag
import os
import random
import re

pause = 0.5 # 10秒待機させる？


def main():
  # main関数
  pag.PAUSE = pause
  width, height = pag.size() # 画面のサイズを取得
  width_range = monitor_length(width)
  height_range = monitor_length(height)
  current_dir = os.getcwd().replace(os.sep,'/') + '/' # pyファイル配下までのパスを取得
  path = current_dir + 'famous_quotes.xlsx'

  print("休んでくだされ～。")
  print('やめるときはコマンドプロンプト/ターミナルを閉じるか、\nコマンドプロンプト/ターミナル上で ctr + c やでー。\n')

  curr_width = 0
  curr_height = 0
  moved_width = 0
  moved_height = 0
  while True:
    try:
      if moved_width != curr_width or moved_height != curr_height:
          # カーソルが移動していたら操作不要
          curr_width, curr_height = pag.position() # 現在位置を更新
          moved_width, moved_height = pag.position()
          print('操作検知。アプリを30秒停止します。終了の場合は閉じるか ctr + c を押してください。')
          pag.sleep(30)
          continue
      moved_width = random.choice(width_range)
      moved_height = random.choice(height_range)
      pag.moveTo(moved_width, moved_height, duration=1) # カーソルをランダムに動かす
      pag.sleep(10)
      curr_width, curr_height = pag.position() # 現在位置を取得
    except:
      print('\nお仕事頑張ってな！！！ほな！')
      pag.sleep(2)
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

if re.compile('__main__').search(__name__):
  main()
