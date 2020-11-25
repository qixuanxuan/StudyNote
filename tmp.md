#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <set>
#include <string.h>
#include <cstring>
#include <set>
#include <utility>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <stdint.h>
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

void AddStringToDictTree(string& str)
{
	int pos;
	DictTreeNode* p = g_root;
	for (int i = 0; i < str.size(); i++) {
		pos = str[i] - 'a';
		if (p->childrens[pos] == NULL) {
			p->childrens[pos] = MalllocNewDictTreeNode();
		}
		p = p->childrens[pos];
	}
	p->endCnt++;
}
void CreateDictTree(vector<string>& dictionary)
{
	g_root = MalllocNewDictTreeNode();
	for (int i = 0; i < dictionary.size(); i++) {
		AddStringToDictTree(dictionary[i]);
	}
}

bool SearchStringInDictTree(DictTreeNode* p, string str, int& cnt)
{
	if (p->childrens[str[0] - 'a'] == NULL || str.size() == 0) {
		return false;
	}
	if (p->childrens[str[0] - 'a'] && p->childrens[str[0] - 'a']->endCnt == 1) {
		return true;
	}
	cnt++;
	return SearchStringInDictTree(p->childrens[str[0] - 'a'], str.substr(1, str.size()), cnt);
}

bool SearchSameExcOneWordInDictTree(DictTreeNode* p, string str, int& cnt)
{
	if (str.size() == 0) {
		return false;
	}
	if (cnt > 1) {
		return false;
	}

	if (p->childrens[str[0] - 'a'] && cnt == 0) {
		return false;
	}
	if (p->endCnt && str.size() > 0) {
		return false;
	}

	if (p->childrens[str[0] - 'a']->endCnt && cnt == 1 && p->childrens[str[0] - 'a']) {
		return true;
	}
	if (p->childrens[str[0] - 'a']->endCnt && cnt == 0 && p->childrens[str[0] - 'a'] == NULL) {
		return true;
	}
	for (int i = 0; i < MAX_CHILDRENS_LEN; i++) {
		if (p->childrens[i] == NULL) {
			continue;
		}
		if (i != str[0] - 'a') {
			cnt++;
		}
		SearchSameExcOneWordInDictTree(p->childrens[i], str.substr(1, str.size()), cnt);
		if (i != str[0] - 'a') {
			cnt--;
		}
	}
	return false;
}

class Solution {
public:
	string replaceWords(vector<string>& dictionary, string sentence) {
		CreateDictTree(dictionary);
		string res = "";
		string tmp;
		stringstream p(sentence);
		int cnt = 1;
		while (p >> tmp)
		{
			if (SearchStringInDictTree(g_root, tmp, cnt)) {
				res += " ";
				res += tmp.substr(0, cnt);
			}
			else {
				res += " ";
				res += tmp;
			}

			cnt = 1;
		}
		return res == "" ? "": res.substr(1, res.size());
	}
};

int main()
{
	vector<string> dictionary = { "hello", "leetcode" };
	string sentence = "hhllo";
	int cnt = 0;
	CreateDictTree(dictionary);

	cout << SearchSameExcOneWordInDictTree(g_root, sentence, cnt) << endl;


	return 0;
}

