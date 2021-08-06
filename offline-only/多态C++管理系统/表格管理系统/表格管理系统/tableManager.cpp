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
	cout << "********欢迎---请选择******" << endl;
	cout << "**********0--退出**********" << endl;
	cout << "**********1--添加**********" << endl;
	cout << "**********2--显示**********" << endl;
	cout << "**********3--删除**********" << endl;
	cout << "**********4--修改**********" << endl;
	cout << "**********5--查找**********" << endl;
	cout << "**********6--排序**********" << endl;
	cout << "**********7--清空**********" << endl;
}
void TableManager::exitSystem()
{
	cout << "欢迎下次使用" << endl;
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
