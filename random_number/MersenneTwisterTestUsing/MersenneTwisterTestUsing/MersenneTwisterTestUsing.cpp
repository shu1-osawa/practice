#include "stdafx.h"				//visualstudioのヘッダ
#include "MersenneTwister.h"	//メルセンヌツイスターのヘッダ
#include <fstream>
#include <iostream>

using namespace std;

int main(){
	ofstream fout("result.txt");
	if (!fout){
		cout << "This file can not open!!";
		return 1;
	}
	int i;	//カウンタ
	init_genrand(1);	//乱数の初期化
	for (i = 0; i<1000; i++){
		fout << genrand_int32() % 1000 <<endl; //乱数生成
	}	
	return 0;
}

