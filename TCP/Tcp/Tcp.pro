#-------------------------------------------------
#
# Project created by QtCreator 2018-07-12T20:36:55
#
#-------------------------------------------------

QT       += core gui
QT       += network


greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Tcp
TEMPLATE = app


SOURCES += main.cpp\
        serverwidget.cpp

HEADERS  += serverwidget.h

FORMS    += serverwidget.ui
CONFIG +=C++11
