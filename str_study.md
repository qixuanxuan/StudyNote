# strcspn

**strcspn(const char *str1, const char *str2)** 检索字符串 **str1** 开头连续有几个字符都不含字符串 **str2** 中的字符。 一般判断两字符串是否有重复字符。 

* strlen(startChar) == strcspn(startChar, arr)  表示不存在重复字符
* strlen(startChar)  !=  strcspn(startChar, arr)  表示存在重复字符

# strstr()

C 库函数 **char \*strstr(const char \*haystack, const char \*needle)** 在字符串 **haystack** 中查找第一次出现字符串 **needle** 的位置，不包含终止符 '\0'。

## 参数

- **haystack** -- 要被检索的 C 字符串。
- **needle** -- 在 haystack 字符串内要搜索的小字符串。

```c++
#include <stdio.h>
#include <string.h>
int main()
{
   const char haystack[20] = "RUNOOB";
   const char needle[10] = "NOOB";
   char *ret;
 
   ret = strstr(haystack, needle);
 
   printf("子字符串是： %s\n", ret);
   
   return(0);
}
```

# strtok()

C 库函数 **char \*strtok(char \*str, const char \*delim)** 分解字符串 **str** 为一组字符串，**delim** 为分隔符。

## 参数

- **str** -- 要被分解成一组小字符串的字符串。
- **delim** -- 包含分隔符的 C 字符串。

```c
#include <string.h>
#include <stdio.h>
int main () {
   char str[80] = "This is - www.runoob.com - website";
   const char s[2] = "-";
   char *token;
   
   /* 获取第一个子字符串 */
   token = strtok(str, s);
   
   /* 继续获取其他的子字符串 */
   while( token != NULL ) {
      printf( "%s\n", token);
    
      token = strtok(NULL, s);
   }
   
   return(0);
}
```

# string 转 str

注意：strlen 不包含“\0”

```c
int main()
{
	string stringTest = "111";
	char* strTest = (char*)stringTest.c_str();
	cout << "stringTest len = " << stringTest.length()<< endl;
	cout << "strTest    len = " << strlen(strTest) << endl;
	return(0);
}
```

