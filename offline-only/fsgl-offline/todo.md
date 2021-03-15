计划：
用最简单的方法，本地数据文件，本地vue文件，vue中的计算属性，实现一个奖金分配的最简单版本，用以验证，vue计算属性可以代替excel的公式。

已完成：
    vue计算属性的调用
    表格内计算属性的调用，每一行都直接计算出相应数据
    本地配置文件的调用

存在问题：
    vue调用本地文件需要用cli 不能离线应用    //可以了，只需正常生成项目，然后把 dist中的index。html文件，修改，<link href="./    <script src="./   注意/前方加. 即可>
    easytable的vue组件在2版本不再支持单元格编辑

思路：

element UI 可以实现可编辑表格，可以用cdn 估计能离线使用

vxe-table 可以实现编辑表格，但是data不变

element UI也不变，可能的虚拟dom的原因

表格内容变了，是变量，需要重新打印查看。用浏览器终端，输出vue对象即可查看



目前考虑用 vxe-talbe



github 问题：
export https_proxy="http://127.0.0.1:10809"设置代理

电脑软件需要打开http代理，端口见软件
