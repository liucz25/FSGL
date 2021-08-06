#include <iostream>

#include "TableManager.h"

using namespace std;
int main() {
	TableManager tm;
	int choice = 0;
	while (true)
	{
		tm.Show_Menu();
		cout << "请输入您的选择：" << endl;
		cin >> choice;
		switch (choice)
		{
		case 0://退出
			tm.exitSystem();
		case 1://添加
			tm.test();
		case 2://显示
			tm.test02();
		case 3://删除
			break;
		case 4://修改
			break;
		case 5://查询
			break;
		case 6://排序
			break;
		case 7://清空
			break;
		default:
			system("cls");
			break;
		}
	}
	system("pause");
	return 0;
}

//用户沟通 命令行界面
// 对表格增删改查
//文件交互  保存  读取文件
//
