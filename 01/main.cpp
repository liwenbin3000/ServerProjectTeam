#include "widget.h"
#include "ui_widget.h"
#include <QSqlDatabase>
#include<QSqlQuery>
#include<QVariantList>//泛型任意类型
#include<QDebug>
#include<QMessageBox>
#include<QSqlError>
#include<QDialog>
#include<QSqlRecord>
#include<QList>
Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    qDebug()<<QSqlDatabase::drivers();
    QSqlDatabase db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("127.0.0.1");
    db.setUserName("root");
    db.setPassword("");
    db.setDatabaseName("info");
    if(!db.open())
    {
        QMessageBox::warning(this,"error",db.lastError().text());
        return;
    }
    model = new QSqlTableModel(this);
    model->setTable("student");//指定访问的数据库中的表
    ui->tableView->setModel(model);//把model放到view中
    model->select();//显示表中的内容

    model->setHeaderData(0,Qt::Horizontal,"学号");//设置列名
    model->setEditStrategy(QSqlTableModel::OnManualSubmit);//设置在修改表数据之后，只有手动提交才能生效
    //ui->tableView->setEditTriggers(QAbstractItemView::NoEditTriggers);这个设置可以使得在ui的地方无法修改表中的内容


}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_pushButtonadd_clicked()
{
   QSqlRecord record = model->record() ;//获取一个新行
   int row = model->rowCount();//获取表中的最大数据行
   model->insertRecord(row,record);//在最后插入新行

}

void Widget::on_pushButtonsure_clicked()
{
    model->submitAll();//确认操作时，将提交刚才的所有操作
}

void Widget::on_pushButtoncansal_clicked()
{
    model->revertAll();//删除时先撤销所有操作
    model->submitAll();//再提交以上所有操作
}

void Widget::on_pushButtondel_clicked()
{
    QItemSelectionModel* smodel = ui->tableView->selectionModel();//获取选中的模型
    QModelIndexList list = smodel->selectedRows();//取出选中模型的索引列表
    for(int i=0;i<list.size();++i)
    {
        model->removeRow(list.at(i).row());//删除i所在的索引的行号
    }
}

void Widget::on_pushButtonfind_clicked()
{
    QString name = ui->lineEdit->text();//获取要查询的名字
    QString str = QString("name = '%1'").arg(name);//组一个sql语句包
    model->setFilter(str);//设置查询条件
    model->select();//显示查询结果
}
————————————————
版权声明：本文为CSDN博主「爱学习的人啊」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_44565518/article/details/103372267
