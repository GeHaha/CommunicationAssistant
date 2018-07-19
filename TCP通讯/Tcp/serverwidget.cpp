#include "serverwidget.h"
#include "ui_serverwidget.h"
#include <QFileDialog>
#include <QDebug>
#include <QFileInfo>

ServerWidget::ServerWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ServerWidget)
{
    ui->setupUi(this);
    tcpServer = NULL;
    tcpSocket = NULL;


    //监听套接字,指定父对象，让其自动回收空间
    tcpServer = new QTcpServer(this);
    tcpServer->listen(QHostAddress::Any ,8888);

    setWindowTitle("服务器：8888");
    //两个文件
    ui->buttonfile->setEnabled(false);
    ui->buttonSendFile->setEnabled(true);

    connect(tcpServer, &QTcpServer::newConnection,
            [=]()
    {
        //取出建立好连接的套接字
        tcpSocket = tcpServer->nextPendingConnection();
        //获取对方的ip和端口
        QString ip = tcpSocket->peerAddress().toString();
        qint16 port =tcpSocket->peerPort();
        QString temp = QString("[%1:%2]:客户端成功连接").arg(ip).arg(port);
        ui->textEditRead->setText(temp);//显示到编辑区

        //成功连接后，才能按选择文件
        ui->buttonfile->setEnabled(true);
        }
    );

    connect(&timer, &QTimer::timeout,
            [=]()
    {
        //关闭定时器
        timer.stop();
        //发送文件
       sendData();

    }

            );

        connect(tcpSocket, &QTcpSocket::readyRead,
                [=]()
        {
            //从通信套接字中取出内容
            QByteArray array = tcpSocket->readAll();
            ui->textEditRead->append(array);


        }

                );

    }


ServerWidget::~ServerWidget()
{
    delete ui;
}

void ServerWidget::on_buttonSend_clicked()
{
    if(NULL == tcpSocket)
    {
        return;
    }

    //获取编辑区内容
    QString str = ui->textEditWrite->toPlainText();
    //给对方发送数据，使用套接字是tcpScoket
    tcpSocket->write(str.toUtf8().data());
    }



void ServerWidget::on_buttonClose_clicked()
{
    if(NULL == tcpSocket)
    {
        return;
    }
    //主动和客户端端口连接
     tcpSocket->disconnectFromHost();
     tcpSocket->close();
     tcpSocket = NULL;

}
//选择文件按钮
void ServerWidget::on_buttonfile_clicked()
{
    if(NULL == tcpSocket)
    {
        return;
    }

    //获取编辑区内容
    QString str = ui->textEditWrite->toPlainText();
    //给对方发送数据，使用套接字是tcpScoket
    tcpSocket->write(str.toUtf8().data());

    QString filePath = QFileDialog::getOpenFileName(this,"open","../");
    if(false == filePath.isEmpty())//如果选择文件的路劲有效
        {
          fileName.clear();
          fileSize =0;

        //获取文件信息
          QFileInfo info(filePath);
          fileName = info.fileName();//获取文件名字
          fileSize = info.size();//获取文件大小

          sendSize = 0;//发送文字大小

        //只读方式打开
          //指定文件的名字
          file.setFileName(filePath);
          //打开文件
          bool isOk = file.open(QIODevice::ReadOnly);
          if(false == isOk)
          {
              qDebug() <<"只读方式打开失败 77";

          }
          //提示打开文件的路劲
            ui->textEditWrite->append(filePath);

            ui->buttonfile->setEnabled(false);

            ui->buttonSend->setEnabled(true);

        }
    else
        {
        qDebug() << "选择文件路劲出错 62";

        }

    }
//发送文件按钮
void ServerWidget::on_buttonSendFile_clicked()
{
  //先发送文件头的信息  文件名##文件大小
   QString head = QString("%1##%2").arg(fileName).arg(fileSize);
   //发送头部信息

   //发送真正的文件信息
   qint64 len = tcpSocket->write(head.toUtf8()) ;
   if(len > 0)//头部信息发送成功
       {
       //发送真正的文件信息
       //防止tcp黏包文件
       //需要通过定时器延时20ms
       timer.start(20);

   }
    else
       {
       qDebug() << "头部信息发送失败 110";
       file.close();
       ui->buttonfile->setEnabled(true);
       ui->buttonSendFile->setEnabled(false);

   }

}
void ServerWidget::sendData()
{
    qint64 len = 0;
    do
    {
        //每次发送数据的大小
        char buf[4*1024] = {0};
        len = 0;
        //往文件中读数据
       len = file.read(buf, sizeof(buf));
        //发送数据，读多少发多少
       len = tcpSocket->write(buf, len);
       //发送数据需要累积
       sendSize += len;

    }while( len > 0);
     //是否发送文件完毕
    if(sendSize == fileSize)
    {
      ui->textEditWrite->append("文件发送完毕");
      file.close();
      //把客户端断开
      tcpSocket->disconnectFromHost();
      tcpSocket->close();

    }

}
