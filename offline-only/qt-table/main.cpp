#include "connection.h"
#include "myqsqltablemodel.h"
#include <QApplication>
#include <QSqlTableModel>
#include <QTableView>
#include <stdlib.h>

void initModel(MyQSqlTableModel *model){
    model->setTable("person");
    model->setEditStrategy(QSqlTableModel::OnFieldChange);
    model->select();
//    model->setHeaderData(0,Qt::Horizontal,QObject::tr("中文"));
}
QTableView * createView(MyQSqlTableModel *model,const QString &title=""){
    QTableView *view=new QTableView;
    view->setModel(model);
    view->setWindowTitle(title);
    return view;
}
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    if(!createConnetction())
        return EXIT_FAILURE;
    MyQSqlTableModel model;
    initModel(&model);
    QTableView *view=createView(&model,QObject::tr("Table Model"));
    view->show();
    return a.exec();
}
