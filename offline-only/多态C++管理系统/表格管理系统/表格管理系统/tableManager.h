#pragma once
#include <iostream>
#include "table.h"
#include<fstream>

//�û���ͨ �����н���
// �Ա����ɾ�Ĳ�
//�ļ�����  ����  ��ȡ�ļ�
//

using namespace std;

class TableManager
{
public:
	TableManager();
	void Show_Menu();
	void exitSystem();

	void test();

	
	void Serialize(std::ostream& os, const std::vector<int>& val);  //  ���л�


	void Deserialize(std::istream& is, const std::vector<int>& val);  //  �����л�
	void test02();
	~TableManager();
};


