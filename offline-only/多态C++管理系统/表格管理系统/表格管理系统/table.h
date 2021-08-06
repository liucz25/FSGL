#pragma once
#include <iostream>
#include<string>
#include<vector>

using namespace std;

class Table
{
public:
	Table();
	~Table();
	void getBackTotalH();
	void getBack();
	void getTotalV();
	void getToalTotal();
	void showInfo();
	void update();
	void getWhole();

	double get(int row, int column);
	void setValue(int row, int column, double value);


	//double -->string
	string doubleConverToString(double d);
	double stringConverTodouble(string str);

	int m_ColumnCount;
	int m_RowCount;
	vector<vector <double> >tableBody;
	vector<string> tableHeadV;
	vector<string> tableHeadH;
	vector<double> totalH;

	vector<vector <double> > tableBack;
	vector<double> totalBackH;
	vector<double> totalV;
	double totalTotal;

	vector<vector <double> > WholeTable;

};