/********************************************************************************
** Form generated from reading UI file 'clientwidget.ui'
**
** Created by: Qt User Interface Compiler version 5.6.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CLIENTWIDGET_H
#define UI_CLIENTWIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ClientWidget
{
public:
    QLabel *label;
    QLineEdit *lineEditPort;
    QPushButton *buttonConnect;
    QLabel *label_3;
    QLineEdit *lineEditIP;
    QTextEdit *textEditRead;
    QLabel *label_4;
    QTextEdit *textEditWrite;
    QPushButton *buttonClose;
    QPushButton *buttonSend;
    QLabel *label_2;
    QPushButton *pushButton;
    QPushButton *pushButton_2;

    void setupUi(QWidget *ClientWidget)
    {
        if (ClientWidget->objectName().isEmpty())
            ClientWidget->setObjectName(QStringLiteral("ClientWidget"));
        ClientWidget->resize(415, 557);
        label = new QLabel(ClientWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(9, 9, 72, 16));
        lineEditPort = new QLineEdit(ClientWidget);
        lineEditPort->setObjectName(QStringLiteral("lineEditPort"));
        lineEditPort->setGeometry(QRect(87, 9, 133, 20));
        buttonConnect = new QPushButton(ClientWidget);
        buttonConnect->setObjectName(QStringLiteral("buttonConnect"));
        buttonConnect->setGeometry(QRect(321, 20, 75, 23));
        label_3 = new QLabel(ClientWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(9, 35, 60, 16));
        lineEditIP = new QLineEdit(ClientWidget);
        lineEditIP->setObjectName(QStringLiteral("lineEditIP"));
        lineEditIP->setGeometry(QRect(87, 35, 133, 20));
        textEditRead = new QTextEdit(ClientWidget);
        textEditRead->setObjectName(QStringLiteral("textEditRead"));
        textEditRead->setGeometry(QRect(9, 79, 387, 161));
        textEditRead->setReadOnly(true);
        label_4 = new QLabel(ClientWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(9, 246, 36, 16));
        textEditWrite = new QTextEdit(ClientWidget);
        textEditWrite->setObjectName(QStringLiteral("textEditWrite"));
        textEditWrite->setGeometry(QRect(9, 264, 387, 162));
        buttonClose = new QPushButton(ClientWidget);
        buttonClose->setObjectName(QStringLiteral("buttonClose"));
        buttonClose->setGeometry(QRect(315, 432, 75, 23));
        buttonSend = new QPushButton(ClientWidget);
        buttonSend->setObjectName(QStringLiteral("buttonSend"));
        buttonSend->setGeometry(QRect(9, 432, 75, 23));
        label_2 = new QLabel(ClientWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(9, 61, 36, 16));
        pushButton = new QPushButton(ClientWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(10, 480, 75, 23));
        pushButton_2 = new QPushButton(ClientWidget);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        pushButton_2->setGeometry(QRect(310, 480, 75, 23));

        retranslateUi(ClientWidget);
        QObject::connect(pushButton, SIGNAL(clicked()), textEditRead, SLOT(clear()));
        QObject::connect(pushButton_2, SIGNAL(clicked()), textEditWrite, SLOT(clear()));

        QMetaObject::connectSlotsByName(ClientWidget);
    } // setupUi

    void retranslateUi(QWidget *ClientWidget)
    {
        ClientWidget->setWindowTitle(QApplication::translate("ClientWidget", "Form", 0));
        label->setText(QApplication::translate("ClientWidget", "\346\234\215\345\212\241\345\231\250\347\253\257\345\217\243\357\274\232", 0));
        lineEditPort->setText(QApplication::translate("ClientWidget", "8888", 0));
        buttonConnect->setText(QApplication::translate("ClientWidget", "\350\277\236\346\216\245\346\234\215\345\212\241\345\231\250", 0));
        label_3->setText(QApplication::translate("ClientWidget", "\346\234\215\345\212\241\345\231\250IP\357\274\232", 0));
        lineEditIP->setText(QApplication::translate("ClientWidget", "127.0.0.1", 0));
        label_4->setText(QApplication::translate("ClientWidget", "\345\217\221\351\200\201\345\214\272", 0));
        buttonClose->setText(QApplication::translate("ClientWidget", "\345\205\263\351\227\255\350\277\236\346\216\245", 0));
        buttonSend->setText(QApplication::translate("ClientWidget", "\345\217\221\351\200\201", 0));
        label_2->setText(QApplication::translate("ClientWidget", "\346\216\245\346\224\266\345\214\272", 0));
        pushButton->setText(QApplication::translate("ClientWidget", "\346\270\205\351\231\244\346\216\245\346\224\266", 0));
        pushButton_2->setText(QApplication::translate("ClientWidget", "\346\270\205\351\231\244\345\217\221\351\200\201", 0));
    } // retranslateUi

};

namespace Ui {
    class ClientWidget: public Ui_ClientWidget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CLIENTWIDGET_H
