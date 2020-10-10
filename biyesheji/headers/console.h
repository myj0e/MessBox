#ifndef CONSOLE
#define CONSOLE

#include <iostream>
#include <string>
#include "../headers/module.h"

class Main{
public:
    void start();


private:
    void trimString(std::string &str);
    void parse(std::string cmd);
    void standard(std::string &cmd);
    void help();
};


//Dependencies  start()->parse()->standard()->trimString()
//              start()->help()

#endif