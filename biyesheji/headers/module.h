#ifndef MODULE_H
#define MODULE_H
#include <string>
#include <iostream>

class Base
{
public:
    Base();
    virtual void exec(std::string input,std::string *output) = 0 ;

protected:
    int step;
};

class dhcp : public Base{
public:
    void exec(std::string input,std::string *output) override;
};

class dns : public Base{
public:
    void exec(std::string input,std::string *output) override;
};

class ftp : public Base{
public:
    void exec(std::string input,std::string *output) override;
};

class http : public Base{
public:
    void exec(std::string input,std::string *output) override;
};

class samba : public Base{
public:
    void exec(std::string input,std::string *output) override;
};

class nfs : public Base{
public:
    void exec(std::string input,std::string *output) override;
};

class smtp : public Base{
public:
    void exec(std::string input,std::string *output) override;
};





#endif

