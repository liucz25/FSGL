#include "table.h"
#include<sstream>
Table::Table() {
	m_ColumnCount = 3;
	m_RowCount = 4;

	for (int i = 0; i < m_RowCount; i++) {
		vector<double> tmp;
		for (int j = 0; j < m_ColumnCount; j++) {
			tmp.push_back(i + j);
		}
		tableBody.push_back(tmp);
		tmp.clear();
	};
	for (int i = 0; i < m_ColumnCount; i++) {
		totalH.push_back(100);
	}

}

Table::~Table()
{
}

void Table::update() {
	getBackTotalH();
	getBack();
	getTotalV();
	getToalTotal();
	getWhole();
}
double Table::get(int row, int column)
{
	//update();	
	return WholeTable[row][column];
}
void Table::getWhole() {
	WholeTable.clear();
	int m_C = m_ColumnCount + 1;
	int m_R = m_RowCount + 1;

	for (int i = 0; i < m_R; i++) {
		vector<double> tmp;
		for (int j = 0; j < m_C; j++) {
			tmp.push_back(0);
		}
		WholeTable.push_back(tmp);
		tmp.clear();
	}
	//cout << WholeTable.size() << "---------" << WholeTable[0].size() << endl;
	for (int i = 0; i < m_RowCount; i++) {
		for (int j = 0; j < m_ColumnCount; j++) {
			WholeTable[i][j] = tableBody[i][j];
		}
	}

	for (int i = 0; i < m_ColumnCount; i++) {
		//cout << "+++++++++++" << i << endl;
		WholeTable[m_R - 1][i] = totalH[i];
	}
	for (int i = 0; i < m_RowCount; i++) {
		//cout << "-------" << i << endl;
		WholeTable[i][m_C - 1] = totalV[i];
	}
	WholeTable[m_R - 1][m_C - 1] = totalTotal;
}
void Table::setValue(int row, int column, double value)
{
	//cout << "setvalue--------row:" << row << "    column:" << column << "    WholeTable[0].size()" << WholeTable[0].size() << endl;
	if (row == WholeTable[0].size()) {
		totalH[column] = value;
	}
	else
	{
		tableBody[row][column] = value;
	}
}
string Table::doubleConverToString(double d)
{
	ostringstream ostmp;
	if (ostmp << d) return ostmp.str();
	return "invalid conversion";
	
}
double Table::stringConverTodouble(string str)
{
	istringstream iss(str);

	double  x;
	if (iss >> x) return x;
	return 0.0;
}
void Table::getBackTotalH()
{
	totalBackH.clear();
	for (int i = 0; i < m_ColumnCount; i++) {
		totalBackH.push_back(0);
	}

	for (int i = 0; i < m_RowCount; i++) {

		for (int j = 0; j < m_ColumnCount; j++) {
			totalBackH[j] += tableBody[i][j];
		}
	}
}
void Table::getBack()
{
	tableBack.clear();
	for (int i = 0; i < m_RowCount; i++) {
		vector<double> tmp;
		for (int j = 0; j < m_ColumnCount; j++) {
			tmp.push_back(0);
		}
		tableBack.push_back(tmp);
	}
	for (int i = 0; i < m_RowCount; i++) {

		for (int j = 0; j < m_ColumnCount; j++) {
			tableBack[i][j] = tableBody[i][j] / totalBackH[j] * totalH[j];
		}
	}


}
void Table::getTotalV()
{
	totalV.clear();
	for (int i = 0; i < m_RowCount; i++) {
		totalV.push_back(0);
	}
	//cout << "totalV-size" << totalV.size() << endl;
	for (int i = 0; i < m_RowCount; i++) {
		for (int j = 0; j < m_ColumnCount; j++) {
			totalV[i] += tableBack[i][j];
		}
	}
}
void Table::getToalTotal()
{
	totalTotal = 0;
	for (int i = 0; i < totalV.size(); i++) {
		totalTotal += totalV[i];
	}
}
void Table::showInfo()
{


	cout << "***********tableBody******************" << endl;
	int columnCount = tableBody[0].size();
	int rowCount = tableBody.size();
	cout << "columcount:" << columnCount << "rowcount:" << rowCount << endl;
	for (int i = 0; i < rowCount; i++) {

		for (int j = 0; j < columnCount; j++) {
			cout << i << ":" << j << "=" << tableBody[i][j] << "    ";
		}
		cout << endl;
	};
	cout << "***********tableBackH******************" << endl;
	int c = totalBackH.size();
	for (int i = 0; i < c; i++) {
		cout << i << ":" << "=" << totalBackH[i] << endl;
	}
	cout << "***********totalH******************" << endl;
	int d = totalH.size();
	for (int i = 0; i < d; i++) {
		cout << "totalH" << i << ":" << "=" << totalH[i] << endl;
	}
	cout << "***********tableBack******************" << endl;
	int cCount = tableBack[0].size();
	int rCount = tableBack.size();
	cout << "columcount:" << cCount << "rowcount:" << rCount << endl;
	for (int i = 0; i < rCount; i++) {
		for (int j = 0; j < cCount; j++) {
			cout << i << ":" << j << "=" << tableBack[i][j] << "    ";
		}
		cout << endl;
	};
	cout << "***********totalV******************" << endl;
	int e = totalV.size();
	for (int i = 0; i < e; i++) {
		cout << "totalV" << i << ":" << "=" << totalV[i] << endl;
	}
	cout << "***********totalTotal******************" << endl;
	cout << "totalTotal=" << totalTotal << endl;


	cout << "***********Wholetable******************" << endl;
	int columnC = WholeTable[0].size();
	int rowC = WholeTable.size();
	cout << "columcount:" << columnC << "rowcount:" << rowC << endl;
	for (int i = 0; i < rowC; i++) {
		for (int j = 0; j < columnC; j++) {
			cout << i << ":" << j << "=" << WholeTable[i][j] << "    ";
		}
		cout << endl;
	};
}
