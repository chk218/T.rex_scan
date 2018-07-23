＃T.rex_scan
脚本在其0.2版本中，T.rex_scan仅在审核网页时促进可视化，其下一版本将允许研究人员只需单击一下即可进行攻击并生成报告


使用此脚本，您可以优化时间，减少审核页面Web的时间，因为T.rex_scan执行您指定的任务并过滤结果。当我们不得不审计一个网页并且我们不得不打开许多控制台来运行每个工具的工具时，这个想法诞生了，除此之外我们必须逐个分析日志并获取我们需要的信息，T.rex_scan瑞士军刀是一种日常使用的工具，可以过滤结果。

<h2>最终版</ h2>

预计该下一版本的脚本将分析一个网页，如果这是易受攻击的，那么访问您的密码和信息的攻击将最终提供一份报告，其中包含分析中的内容。

<h2>将实施的改进：</ h2>
 
*显示审计页面的漏洞
*启动端口扫描
*显示与页面漏洞相关的CVE
*搜索与域关联的电子邮件
*显示IP地址和托管服务器位置

此脚本使用并依赖于以下工具进行操作：

* WPScan V 2.9.3
* Nmap V 7.60
* Theharvester V 2.7
* WhatWeb V 0.4.9
* Colorama
* tqdm

这个脚本利用正则表达式来过滤我们需要的数据，使用库（os，time，re，time，color，tqdm和sleep）

重要的是要记住，如果你打算使用Kali linux，你应该只安装tqdm库，但是如果要使用Windows，你必须使用选项pip install安装所有库。

安装/使用

* git clone https://github.com/davenisc/T.rex_scan/tree/0.2
* cd T.rex_scan
* pip install -r requirements.txt
* python T.rex_scan.py
* option 5 for more details of T.rex_scan

<a href="https://ibb.co/eEMVuc"><img src="https://preview.ibb.co/mB1Vuc/actualizacion.png" alt="actualizacion" border="0"></a>

<a href="https://ibb.co/jSLFuc"><img src="https://preview.ibb.co/n2eVSx/details_new.png" alt="details_new" border="0"></a>

Analyzing the website

<a href="https://ibb.co/fTLZtS"><img src="https://preview.ibb.co/ewk0YS/2.png" alt="2" border="0"></a><br /><a target='_blank' href=''></a><br />

Port analysis

<a href="https://ibb.co/j9d9Sn"><img src="https://preview.ibb.co/ejZinn/3.png" alt="3" border="0"></a><br /><a target='_blank' href=''></a><br />

Mail search

<a href="https://ibb.co/fxPYnn"><img src="https://preview.ibb.co/gNH8L7/4.png" alt="4" border="0"></a><br /><a target='_blank' href=''></a><br />

Results

<a href="https://ibb.co/cBPhV7"><img src="https://preview.ibb.co/dhFZcn/5.png" alt="5" border="0"></a><br /><a target='_blank' href=''></a><br />

<a href="https://ibb.co/caUoL7"><img src="https://preview.ibb.co/ghPcDS/6.png" alt="6" border="0"></a><br /><a target='_blank' href=''></a><br />

<a href="https://ibb.co/cvQNV7"><img src="https://preview.ibb.co/g2LBOS/7.png" alt="7" border="0"></a><br /><a target='_blank' href=''></a><br />

The logs can be analyzed also without the tool

<a href="https://ibb.co/cuxQiS"><img src="https://preview.ibb.co/nKxQiS/8.png" alt="8" border="0"></a><br /><a target='_blank' href=''></a><br />


“车轮已经发明了，所以再次发明它？如果它已经被创造出来，我们可以用它来加快速度。”

致谢：@elcodigok @ Sebastianf94 @LuisRamirezMe @whitepadawan

谢谢你的贡献。

我的信息：
- sysvd@protonmail.com
- Twitter @DaveNISC

<br>
汉化：Shihun<br>
博客：<a href="https://blog.csdn.net/chk218">点击访问</a>
