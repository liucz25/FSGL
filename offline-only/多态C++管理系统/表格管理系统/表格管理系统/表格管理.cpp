#include <iostream>

#include "TableManager.h"

using namespace std;
int main() {
	TableManager tm;
	int choice = 0;
	while (true)
	{
		tm.Show_Menu();
		cout << "����������ѡ��" << endl;
		cin >> choice;
		switch (choice)
		{
		case 0://�˳�
			tm.exitSystem();
		case 1://���
			tm.test();
		case 2://��ʾ
			tm.test02();
		case 3://ɾ��
			break;
		case 4://�޸�
			break;
		case 5://��ѯ
			break;
		case 6://����
			break;
		case 7://���
			break;
		default:
			system("cls");
			break;
		}
	}
	system("pause");
	return 0;
}

//�û���ͨ �����н���
// �Ա����ɾ�Ĳ�
//�ļ�����  ����  ��ȡ�ļ�
//
