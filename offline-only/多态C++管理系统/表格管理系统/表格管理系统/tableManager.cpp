#include "tableManager.h"
TableManager::TableManager()
{
	//cout << "TableManager init" << endl;
}
TableManager::~TableManager()
{

}
void TableManager::Show_Menu()
{
	cout << "********��ӭ---��ѡ��******" << endl;
	cout << "**********0--�˳�**********" << endl;
	cout << "**********1--���**********" << endl;
	cout << "**********2--��ʾ**********" << endl;
	cout << "**********3--ɾ��**********" << endl;
	cout << "**********4--�޸�**********" << endl;
	cout << "**********5--����**********" << endl;
	cout << "**********6--����**********" << endl;
	cout << "**********7--���**********" << endl;
}
void TableManager::exitSystem()
{
	cout << "��ӭ�´�ʹ��" << endl;
	system("pause");
	exit(0);
}
void TableManager::test() {

	Table t;
	t.update();
	t.showInfo();
	t.setValue(0, 1, 9);
	t.setValue(4, 2, 200);
	t.update();
	t.showInfo();

}

void TableManager::Serialize(std::ostream& os, const std::vector<int>& val)
{
	os.write((const char*)val.data(), val.size() * sizeof(int));

}

void TableManager::Deserialize(std::istream& is, const std::vector<int>& val)
{
	is.read((char*)&val, sizeof(int));
	
}

void TableManager::test02()
{
	ofstream ofs;
	ofs.open("ofs.txt", ios::out | ios::binary);
	vector<int> v;
	v.push_back(22);
	v.push_back(33);

	//cout <<v[0]<<"VVVVVVVVVVVVVVVV"<<v[1] << endl;

	Serialize(ofs,v);
	ofs.close();
	vector<int> v1;
	ifstream ifs;
	ifs.open("ofs.txt", ios::in | ios::binary);
	Deserialize(ifs, v1);
	cout << v1[0] << "v1111111111111111" << endl;
}
