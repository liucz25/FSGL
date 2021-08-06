#pragma once
#include <iostream>
#include "table.h"
#include<fstream>

//用户沟通 命令行界面
// 对表格增删改查
//文件交互  保存  读取文件
//

using namespace std;

class TableManager
{
public:
	TableManager();
	void Show_Menu();
	void exitSystem();

	void test();

	
	void Serialize(std::ostream& os, const std::vector<int>& val);  //  序列化


	void Deserialize(std::istream& is, const std::vector<int>& val);  //  反序列化
	void test02();
	~TableManager();
};


