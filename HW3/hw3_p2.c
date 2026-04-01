#include <stdio.h>
#include <string.h>
void length_check(char *str)
{
   printf("The concatenated string is: %s \nThe length of the concatenated string is: %d\n",str, (int) strlen(str));
}
// int main()
// {
//     char result[10];
//     char str1[10];
//     char str2[10];
//     memset(result,'\0',10);
//     gets(str1);
//     gets(str2);
//     strcpy(result, str1);
//     strcat(result, str2);
//     length_check(result);
//     return(0);
// }


int main()
{
    char result[20];
    char str1[10];
    char str2[10];
    memset(result,'\0',20);
    if (fgets(str1, 10, stdin) == NULL) return 1;
    if (fgets(str2, 10, stdin) == NULL) return 1;
    // remove null terminators since fgets keeps it 
    str1[strcspn(str1, "\n")] = '\0';
    str2[strcspn(str2, "\n")] = '\0';
    strncpy(result, str1, sizeof(result) - 1);
    // ensure null termination after strncpy since it may not 
    result[sizeof(result) - 1] = '\0'; 
    strncat(result, str2, sizeof(result) - strlen(result) - 1);
    length_check(result);
    return(0);
}

