#include "clientwidget.h"
#include "ui_clientwidget.h"
#include <QHostAddress>
#include <QMessageBox>

ClientWidget::ClientWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ClientWidget)
{
    ui->setupUi(this);

    tcpSocket = NULL;

    //分配空间，指定父对象
    tcpSocket = new QTcpSocket(this);

    isStart = true;

    setWindowTitle("客户端");
    connect(tcpSocket, &QTcpSocket::connected,
           [=]()
         {
           ui->textEditRead->setText("成功和服务器建立好连接");
         }
            );
    connect(tcpSocket, &QTcpSocket::readyRead,
           [=]()
       {
        //获取对方发送的内容
        QByteArray array = tcpSocket->readAll();
        //追加到编辑区中
        ui->textEditRead->append(array);


        //取出接收的内容
        QByteArray buf = tcpSocket->readAll();
        if(true == isStart )
        { //接收头
            isStart = false;

            //解析头部信息 QString buf = "hello"##1204"
           //QString str = "hello##1024##33"
                    // str.section("##", 0, 0)
            //初始化
            fileName =  QString(buf).section("##", 0, 0);
            fileSize =  QString(buf).section("##", 1, 1).toInt();
            recvSize =0;

            //打开文件
            file.setFileName(fileName);
            bool isOk = file.open(QIODevice::WriteOnly);
            if (false == isOk)
            {
                qDebug() << "WriteOnly error 40";
            }

        }
        else//文件信息
            {
             qint64 len = file.write(buf);
             recvSize += len ;
             if (recvSize == fileSize)
             {
                 file.close();
                 QMessageBox::information(this, "完成", "文件接收完成");
                 tcpSocket->disconnectFromHost();
                 tcpSocket->close();

             }
            }

        }

            );

}

ClientWidget::~ClientWidget()
{
    delete ui;
}

void ClientWidget::on_buttonConnect_clicked()
{
    //获取服务器IP和端口
    QString ip = ui->lineEditIP->text();
    qint16 port = ui->lineEditPort->text().toInt();
    //主动和服务器建立连接
    tcpSocket->connectToHost(QHostAddress(ip), port);

}

void ClientWidget::on_buttonSend_clicked()
{
    //获取编辑框内容
    QString str = ui->textEditWrite->toPlainText();
    //发送数据
    tcpSocket->write(str.toUtf8().data());

}

void ClientWidget::on_buttonClose_clicked()
{
    //主动和对方断开连接
    tcpSocket->disconnectFromHost();
    tcpSocket->close();

}

void ClientWidget::on_pushButton_clicked()
{

}
