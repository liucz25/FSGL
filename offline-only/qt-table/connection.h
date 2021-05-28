#ifndef CONNECTION_H
#define CONNECTION_H

#include <QMessageBox>
#include <QSqlDatabase>
#include <QSqlError>
#include <QSqlQuery>
static bool createConnetction(){
    QSqlDatabase db=QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("HumanResourcesManager.s3db");
    if(!db.open()){
        QMessageBox::critical(nullptr, QObject::tr("Cannot open database"),
                    QObject::tr("Unable to establish a database connection.\n"
                                "This example needs SQLite support. Please read "
                                "the Qt SQL driver documentation for information how "
                                "to build it.\n\n"
                                "Click Cancel to exit."), QMessageBox::Cancel);
                return false;}

    db.close();
    return true;
}
#endif // CONNECTION_H
