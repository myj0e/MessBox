#include "../headers/console.h"




void Main::start(void){
    while(true){
        std::string cmd;
        std::cout<<"root@ubuntu:~# ";
        getline(std::cin,cmd);
        parse(cmd);
    }
}

void Main::parse(std::string cmd){
    standard(cmd);
    std::string sub_str;
    int e=cmd.find_first_of(" ");
    if(e==-1) sub_str=cmd;
    else sub_str=cmd.substr(0,e);
    if(sub_str=="help"){
        help();
    }
    else if (sub_str=="apt-get"){
        if(e==-1){
            
        }
    }
    else if (sub_str=="iptables"){
        std::cout<<"Building..."<<std::endl;
    }
    else{
        std::cout<<"Command '"<<sub_str<<"' cannot be found."<<std::endl;
    }
    
}

void Main::trimString(std::string & str )
{
    int s = str.find_first_not_of(" ");
    int e = str.find_last_not_of(" ");
    str = str.substr(s,e-s+1);
    return;
}
 
void Main::help(){
    std::cout<<"help:    help"<<std::endl;
}

void Main::standard(std::string &cmd){
    trimString(cmd);
    // std::cout<<"After trim cmd:|"<<cmd<<"|"<<std::endl;
    // std::cout<<"cmd_lenghth: "<<cmd.length()<<std::endl;
    // std:: string str;
    for (int i =0;i<cmd.length();i++){
        while(i<(cmd.length()-1) && cmd[i]==' ' && cmd[i+1]==' '){
            cmd.erase(i,1);
        }
    }
    // std::cout<<"In standard  str:|"<<cmd<<"|"<<std::endl;
}