source insight 安装Quicker.em插件

grimekeep 2021-07-19 15:12:57  19  收藏
文章标签： macos 编辑器 经验分享 windows
版权
Quicker.em插件的安装和使用
一. 将quicke.em文件添加到sourceinsight 安装目录的base目录下
二.打开source insight base工程，**将quicker.em 添加到项目中 **。
三.打开Options->KeyAssignments 找到Macro:AutoExpand。并添加一个热键：一般推荐Ctrl+Enter。可根据个人习惯设置。
这样设置好以后之后创建的任何项目，都可以使用该插件。值得注意的一点是，在其他项目使用该插件时，需要关闭base项目。

快捷键字符串如下：
##
使用方式：在编码区输入以上对应功能字符串后，再输入之前设置好的热键（Crtl+Enter），即可跳转到对应功能。
Quicker.em 适用于4.0版本：源码如下
————————————————
版权声明：本文为CSDN博主「grimekeep」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/grimekeep/article/details/118896305


【设置步骤】

1、将Quicker.em放到 Source Insight 4.0\Projects\Base\目录下；
2、Source Insight 4.0中设置Options >> Key Assignments... >> Macro: AutoExpand快捷键为Alt+Enter(个人习惯)；
3、编码时可输入以下“快捷字符串”后按下快捷键(如Alt+Enter)，即可对应快速输入既定格式内容。

附快捷字符串：
co      弹窗配置语言和姓名
hi      文件顶部注释中新增modification
pn      弹窗定义bugID
abg     添加开始和结束注释行并附带bugID
dbg     删除开始和结束注释行并附带bugID
mbg     修改开始和结束注释行并附带bugID
{       单作用域补全
wh      补全while(){}
else    补全else{}
#ifd    弹窗定义#ifdef
#ifn    弹窗定义#ifndef
#if     弹窗定义#if
cpp     补全兼容C/C++宏定义
if      补全if(){}
ef      补全else if(){}
ife     补全if(){}else{}
ifs     补全if(){}else if(){}else{}
for     弹窗输循环变量名补全for(){}
sw      弹窗输入case数补全switch-case
case    补全单个case语句
do      补全do{}while();
st      弹窗输入结构体名补全_T_STRU
en      弹窗输入枚举名补全_ENUM
fi      弹窗置顶输入文件备注信息
fu      弹窗补全函数备注和格式
tab     弹窗提示替换空格数和是否全部替换
ap      弹窗提示带bugID和描述的双行注释
hd      一键补全头文件注释和兼容C/C++结构
ab      补全待bugID的add注释begin
ae      补全待bugID的add注释end
db      补全待bugID的delete注释begin
de      补全待bugID的delete注释end
mb      补全待bugID的modify注释begin
me      补全待bugID的modify注释end
————————————————
版权声明：本文为CSDN博主「不才Jerry」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/sinat_36184075/article/details/80086923