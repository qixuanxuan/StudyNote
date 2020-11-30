# 解决vscode远程连接linux系统无法跳转(f12失效)问题(因远端未安装相应插件导致的）

1、主要原因是远程连接时，本地安装的插件并没有在远程安装，所以只需要在远程安装即可。

如下图，SSH:130-INSTALLED中是远程安装的，JU-INSTALLED是本地安装的，都安装好重新加载窗口即可。

![img](https://img-blog.csdnimg.cn/201909231420510.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI3NzI3MTQ3,size_16,color_FFFFFF,t_70)

以上方法还是不行，可以尝试如下方法。

1、打开键盘快捷方式(在左下角设置里）：

![img](https://img-blog.csdnimg.cn/20190923140059728.png)

2、修改f12键绑定的参数

将editorHasDefinitionProvider && editorTextFocus && !isInEmbeddedEditor

改为editor.action.revealDefinition

3、保存生效
