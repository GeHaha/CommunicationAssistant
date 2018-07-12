/********************************************************************************
** Form generated from reading UI file 'serverwidget.ui'
**
** Created by: Qt User Interface Compiler version 5.6.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SERVERWIDGET_H
#define UI_SERVERWIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ServerWidget
{
public:
    QGridLayout *gridLayout;
    QLabel *labelRecieve;
    QTextEdit *textEditRead;
    QLabel *labelSend;
    QTextEdit *textEditWrite;
    QSpacerItem *horizontalSpacer;
    QPushButton *buttonSend;
    QSpacerItem *horizontalSpacer_3;
    QPushButton *buttonClose;
    QSpacerItem *horizontalSpacer_2;

    void setupUi(QWidget *ServerWidget)
    {
        if (ServerWidget->objectName().isEmpty())
            ServerWidget->setObjectName(QStringLiteral("ServerWidget"));
        ServerWidget->resize(426, 352);
        gridLayout = new QGridLayout(ServerWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        labelRecieve = new QLabel(ServerWidget);
        labelRecieve->setObjectName(QStringLiteral("labelRecieve"));

        gridLayout->addWidget(labelRecieve, 0, 0, 1, 1);

        textEditRead = new QTextEdit(ServerWidget);
        textEditRead->setObjectName(QStringLiteral("textEditRead"));

        gridLayout->addWidget(textEditRead, 1, 1, 1, 3);

        labelSend = new QLabel(ServerWidget);
        labelSend->setObjectName(QStringLiteral("labelSend"));

        gridLayout->addWidget(labelSend, 2, 0, 1, 1);

        textEditWrite = new QTextEdit(ServerWidget);
        textEditWrite->setObjectName(QStringLiteral("textEditWrite"));

        gridLayout->addWidget(textEditWrite, 3, 1, 1, 3);

        horizontalSpacer = new QSpacerItem(67, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 4, 0, 1, 1);

        buttonSend = new QPushButton(ServerWidget);
        buttonSend->setObjectName(QStringLiteral("buttonSend"));

        gridLayout->addWidget(buttonSend, 4, 1, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(91, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 4, 2, 1, 1);

        buttonClose = new QPushButton(ServerWidget);
        buttonClose->setObjectName(QStringLiteral("buttonClose"));

        gridLayout->addWidget(buttonClose, 4, 3, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(67, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 4, 4, 1, 1);


        retranslateUi(ServerWidget);

        QMetaObject::connectSlotsByName(ServerWidget);
    } // setupUi

    void retranslateUi(QWidget *ServerWidget)
    {
        ServerWidget->setWindowTitle(QApplication::translate("ServerWidget", "ServerWidget", 0));
        labelRecieve->setText(QApplication::translate("ServerWidget", "\346\216\245\346\224\266\345\214\272", 0));
        labelSend->setText(QApplication::translate("ServerWidget", "\345\217\221\351\200\201\345\214\272", 0));
        buttonSend->setText(QApplication::translate("ServerWidget", "\345\217\221\351\200\201", 0));
        buttonClose->setText(QApplication::translate("ServerWidget", "\345\205\263\351\227\255", 0));
    } // retranslateUi

};

namespace Ui {
    class ServerWidget: public Ui_ServerWidget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SERVERWIDGET_H
