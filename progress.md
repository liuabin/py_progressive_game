# 游戏开发日记

> 一天 一 commit 

## 1011 init project

* 初始化项目
* 建立主循环

## 1015 main

* 模块化 handler displayer data
* 实现游戏主循环
* 添加了 git ignore 

## 1016 Unityinput

* getchar() 依托于键盘连续字符输入模式，且不能多键输入
  * (游戏输入体验梦回小时候打的《魔塔》)
* 尝试了一下非阻塞键盘输入
* 类似 Unity 在每一帧头检测键盘状态，每一帧强制刷新画面
* data 中 character 类暂时没想好怎么改
* 累了摸了

## 1017 mota

* 提交一个小版本，完成了对 input, display 的封装
* 以此纪念小时候永远的回忆《魔塔》