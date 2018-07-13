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
    QSpacerItem *horizontalSpacer_5;
    QPushButton *buttonfile;
    QSpacerItem *horizontalSpacer_4;
    QPushButton *buttonSendFile;
    QSpacerItem *horizontalSpacer_6;
    QSpacerItem *horizontalSpacer_8;
    QPushButton *buttonClear;
    QSpacerItem *horizontalSpacer_7;
    QPushButton *buttonClear2;
    QSpacerItem *horizontalSpacer_10;

    void setupUi(QWidget *ServerWidget)
    {
        if (ServerWidget->objectName().isEmpty())
            ServerWidget->setObjectName(QStringLiteral("ServerWidget"));
        ServerWidget->resize(439, 475);
        gridLayout = new QGridLayout(ServerWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        labelRecieve = new QLabel(ServerWidget);
        labelRecieve->setObjectName(QStringLiteral("labelRecieve"));

        gridLayout->addWidget(labelRecieve, 0, 0, 1, 1);

        textEditRead = new QTextEdit(ServerWidget);
        textEditRead->setObjectName(QStringLiteral("textEditRead"));

        gridLayout->addWidget(textEditRead, 1, 0, 1, 5);

        labelSend = new QLabel(ServerWidget);
        labelSend->setObjectName(QStringLiteral("labelSend"));

        gridLayout->addWidget(labelSend, 2, 0, 1, 1);

        textEditWrite = new QTextEdit(ServerWidget);
        textEditWrite->setObjectName(QStringLiteral("textEditWrite"));

        gridLayout->addWidget(textEditWrite, 3, 0, 1, 5);

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

        horizontalSpacer_5 = new QSpacerItem(74, 17, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_5, 5, 0, 1, 1);

        buttonfile = new QPushButton(ServerWidget);
        buttonfile->setObjectName(QStringLiteral("buttonfile"));

        gridLayout->addWidget(buttonfile, 5, 1, 1, 1);

        horizontalSpacer_4 = new QSpacerItem(91, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_4, 5, 2, 1, 1);

        buttonSendFile = new QPushButton(ServerWidget);
        buttonSendFile->setObjectName(QStringLiteral("buttonSendFile"));

        gridLayout->addWidget(buttonSendFile, 5, 3, 1, 1);

        horizontalSpacer_6 = new QSpacerItem(73, 17, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_6, 5, 4, 1, 1);

        horizontalSpacer_8 = new QSpacerItem(74, 17, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_8, 6, 0, 1, 1);

        buttonClear = new QPushButton(ServerWidget);
        buttonClear->setObjectName(QStringLiteral("buttonClear"));

        gridLayout->addWidget(buttonClear, 6, 1, 1, 1);

        horizontalSpacer_7 = new QSpacerItem(91, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_7, 6, 2, 1, 1);

        buttonClear2 = new QPushButton(ServerWidget);
        buttonClear2->setObjectName(QStringLiteral("buttonClear2"));

        gridLayout->addWidget(buttonClear2, 6, 3, 1, 1);

        horizontalSpacer_10 = new QSpacerItem(73, 17, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_10, 6, 4, 1, 1);


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
        buttonfile->setText(QApplication::translate("ServerWidget", "\351\200\211\346\213\251\346\226\207\344\273\266", 0));
        buttonSendFile->setText(QApplication::translate("ServerWidget", "\345\217\221\351\200\201\346\226\207\344\273\266", 0));
        buttonClear->setText(QApplication::translate("ServerWidget", "\346\270\205\351\231\244\346\216\245\346\224\266", 0));
        buttonClear2->setText(QApplication::translate("ServerWidget", "\346\270\205\351\231\244\345\217\221\351\200\201", 0));
    } // retranslateUi

};

namespace Ui {
    class ServerWidget: public Ui_ServerWidget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SERVERWIDGET_H
