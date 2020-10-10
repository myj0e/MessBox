#include <iostream>
#include <cmath>
#include<cstdlib>
#include<iomanip>
using namespace std;


/****************************************************************************************/
/****************************************************************************************/
/*******************************************class****************************************/
/****************************************************************************************/
/****************************************************************************************/

//****************************************定义T数据类型***********************************
class T
{
    double value; //T的值
    double param; //T运算的参数

  public:
    //初始化参数
    void parm(double pic = 12, double eta = 0.868)
    {
        param = (1.005 * 288 * (pow(pic, (0.4 / 1.4)) - 1)) / (1.158 * (1 - 1 / pow(2.5, (0.33 / 1.33))) * eta * 0.9 * 0.98);
    }

    //运行T的函数，得到值存入value
    double run(double Beta)
    {
        value = param / Beta;
    }

    //返回value值
    double show()
    {
        return value;
    }
};

//*********************************************define a type H********************
class H
{
    double value;
    double a, c, d;

  public:
    //constructor,initialise a,c,d
    H(double A, double C, double D) : a(A), c(C), d(D) {}

    //run function of H with parameter B,store the result into value
    double run(double B)
    {
        value = a * pow(B, 2) + c * B + d;
    }

    //return value of value
    double show()
    {
        return value;
    }
};

//**********************************************defin a class Q*********************
class Q
{
    double a, b, c;
    double value;

  public:
    Q() : value(0.744072) {}
    double pic()
    {
        return (-22190 * pow(value, 2) + 33075 * value - 12304);
    }
    double eta()
    {
        return (-247.44 * pow(value, 2) + 371.71 * value - 138.95);
    }
    double show()
    {
        return value;
    }
    double add(double x)
    {
        if(x<2) value+=0.0000001;
        else value+=1;
    }
};

/****************************************************************************************/
/****************************************************************************************/
/***************************************function()***************************************/
/****************************************************************************************/
/****************************************************************************************/

//function f(),ruturn the result
double f(double h3a, double h2a, double h3)
{
    return (h3a - h2a) / (0.97 * 42900 - h3 + h2a);
}

/****************************************************************************************/
/****************************************************************************************/
/*******************************************main()***************************************/
/****************************************************************************************/
/****************************************************************************************/

int main()
{
    double beta_1, beta = 1;
    T t3;
    t3.parm();
    H h3(0.0005, 2.0678, -301.67), h3a(0.0001, 0.9114, 20.011), h2a(0.0001, 0.9114, 20.011);

    //第一部分循环
    do
    {
        t3.run(beta);
        h3.run(t3.show());
        h3a.run(t3.show());
        h2a.run(631.0);
        beta_1 = 0.98 + f(h3a.show(), h2a.show(), h3.show());
        beta += 0.0001;
    } while (abs(beta - 0.0001 - beta_1) > 0.0001);
    cout << "beta=" << beta-0.0001 << endl;
    cout << "T3*=" << t3.show() << endl;

    //第二部分循环
    double cd = 12 / (sqrt((pow(12, 0.4 / 1.4) - 1) / 0.868) * 0.8652 * sqrt(beta));
    cout<<cd<<endl;
    
    Q q;
    double pic, eta, t2, beta2, c,beta1;
    H h_3(0.0005, 2.0678, -301.67), h_3a(0.0001, 0.9114, 20.011), h_2a(0.0001, 0.9114, 20.011);
    T t_3;
    int cx=1;
    do
    {
        pic = q.pic();
        eta = q.eta();
        t_3.parm(pic, eta);
        beta1 = 1;
        do
        {
            t_3.run(beta1);
            h_3.run(t_3.show());
            h_3a.run(t_3.show());
            t2 = 288 * (1 + (pow(pic, 0.4 / 1.4) - 1) / eta);
            h_2a.run(t2);
            beta2 =0.98+ f(h_3a.show(), h_2a.show(), h_3.show());//赋值beta2=0.98+f'
            beta1 += 0.0001;
            cout << beta1<<","<<beta2 << endl;//debug用，查看beta1，beta2的动态变化
            if (cx++ >1000000000)return 0;//限制循环次数为1000000000(十亿)次，防止死循环
        } while (abs(beta1 - 0.0001 - beta2) > 0.0001);
//        cout << "done" << endl;//当内层循环结束时输出表示内层非死循环
        cout << "beta_1=" << beta1 << endl;
        cout << "T3*\'=" << t_3.show() << endl;

        c = pic / (sqrt((pow(pic, 0.4 / 1.4) - 1) / eta) * q.show() * sqrt(beta));
        q.add(abs(c-cd));
        cout<<c<<","<<cd<<endl;//debug用，观察c,cd动态变化
    } while (abs(c - cd) > 0.0001);
    cout.flags(ios::left);
    cout << setfill('=') << setw(38) << "=" << endl;
    cout << setw(20) << setfill(' ') << "|| beta_1" <<"| "<< setw(15) << beta1 << "||" << endl;
    cout << setw(20) << setfill(' ')<< "|| T3*\'" <<"| "<< setw(15) << t_3.show() << "||" << endl;
    cout << setw(20) << setfill(' ')<< "|| q(lambda_1)" <<"| "<< setw(15) << q.show() << "||" << endl;
    cout << setw(20) << setfill(' ')<< "|| pi_c *" <<"| "<< setw(15) << pic << "||" << endl;
    cout << setw(20) << setfill(' ')<< "|| eta_c *" <<"| "<< setw(15) << eta << "||" << endl;
    cout << setfill('=') << setw(38) << "=" << endl;
//    system("PAUSE");
}
