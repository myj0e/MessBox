#include "../headers/module.h"

Base::Base(){
    step =0;
}

void dhcp::exec(std::string input,std::string *output)
{
    if(1==1){
        *output="Unpacking libirs-export141 (1:9.10.3.dfsg.P4-8ubuntu1.15) ...\nSelecting previously unselected package isc-dhcp-server.\nPreparing to unpack .../isc-dhcp-server_4.3.3-5ubuntu12.10_amd64.deb ...\nUnpacking isc-dhcp-server (4.3.3-5ubuntu12.10) ...\nProcessing triggers for libc-bin (2.23-0ubuntu5) ...\nProcessing triggers for systemd (229-4ubuntu16) ...\nProcessing triggers for ureadahead (0.100.0-19) ...\nProcessing triggers for man-db (2.7.5-1) ...\nSetting up libisccfg-export140 (1:9.10.3.dfsg.P4-8ubuntu1.15) ...\nSetting up libirs-export141 (1:9.10.3.dfsg.P4-8ubuntu1.15) ...\nSetting up isc-dhcp-server (4.3.3-5ubuntu12.10) ...\nGenerating /etc/default/isc-dhcp-server...\nProcessing triggers for libc-bin (2.23-0ubuntu5) ...\nProcessing triggers for systemd (229-4ubuntu16) ...\nProcessing triggers for ureadahead (0.100.0-19) ...";

    }
}

int main(){
    dhcp a;
    std::string x = "default";
    a.exec("hello",&x);
    std::cout << x << std::endl;
}