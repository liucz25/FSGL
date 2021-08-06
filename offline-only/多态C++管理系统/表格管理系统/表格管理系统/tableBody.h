#pragma once
#include <iostream>
using namespace std;
#include "table.h"

class TableBody :public Table
{
public:
	TableBody(int column, int row, double value);
	virtual void ShowInfo();
	virtual string getHeadName();
};