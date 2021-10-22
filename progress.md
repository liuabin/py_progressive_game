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

## 1017 Mota

* 提交一个小版本，完成了对 input, display 的封装
* 以此纪念小时候永远的回忆《魔塔》

## 1018 Update

* 每秒帧率：52 57 47 47 55 53 53 50 54 50
* 输入暂时用的 hook，随后发现（移动）数据必须每帧更新不能依附输入
* 实现了 Unity 的 **Update**, FixedUpdate 暂时没有实现的思路
* 加上数据更新帧率基本没变

## 1020 Closures

* 锁帧 30
* 将 handler 改造成了闭包函数，有异常时回调 game_should_close
* 导师把我孤立在实验室大活外了，麻了

## 1021 

* 删除了最初的 handler
* 加上了 map dsl 写的有点乱临时交一版

