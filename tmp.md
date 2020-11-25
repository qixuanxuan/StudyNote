// ConsoleApplication1.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#include <string>
#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>
#include "stdio.h"
using namespace std;

#define MAX_CHILDRENS_LEN 26
typedef struct DictTreeNode_S {
	int endCnt;
	struct DictTreeNode_S* childrens[MAX_CHILDRENS_LEN];
}DictTreeNode;

DictTreeNode* g_root;

DictTreeNode* MalllocNewDictTreeNode() {
	DictTreeNode* NewDictTreeNode = (DictTreeNode*)malloc(sizeof(DictTreeNode));
	for (int i = 0; i < MAX_CHILDRENS_LEN; i++) {
		NewDictTreeNode->childrens[i] = NULL;
	}
	NewDictTreeNode->endCnt = 0;
	return NewDictTreeNode;
}

void addStringToDictTree(string& )
{

}
void CreateDictTree(vector<string>& dictionary)
{
	g_root = MalllocNewDictTreeNode();
	for (int i = 0; i < dictionary.size(); i++) {
		addStringToDictTree(dictionary[i]);
	}
}

class Solution {
public:
	string replaceWords(vector<string>& dictionary, string sentence) {

	}
};
int main()
{
	string stringTest = "111";
	char* strTest = (char*)stringTest.c_str();
	cout << "stringTest len = " << stringTest.length()<< endl;
	cout << "strTest    len = " << strlen(strTest) << endl;
	return(0);

}
