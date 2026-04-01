#include<stdio.h>
#include<string.h>
// int main()
// {
// int i,j,la,lb,num=0;
// char c,a[12],b[45];
// while((c=getchar())!='\n') 
//     a[num++]=c;
// a[num]='\0';
// printf("The str1 is:\n");
// printf("%s",a);
// printf("\n");
// num=0;
// while((c=getchar())!='\n') 
//     b[num++]=c;
// b[num]='\0';
// printf("\nThe str2 is:\n");
// printf("%s",b);
// printf("\n");
// la=strlen(a);
// lb=strlen(b);
// for(i=0;(lb-i)>=la;i++)
// {
//     if(b[i]==a[0])
//     {
//         for(j=0;j<la;j++)
//             if(b[i+j]!=a[j]) 
//                 break;
//         if(j==la) {
//             printf("\nPosition: %d\n",i);
//             return 0;
        
//     }
//     }
// }
// printf("\nNot found!\n");
// }




int main() {
    char a[12], b[45];

    // update- read in input safely
    if (fgets(a, sizeof(a), stdin) == NULL) return 1;
    if (fgets(b, sizeof(b), stdin) == NULL) return 1;
    // Remove newline characters
    a[strcspn(a, "\n")] = '\0';
    b[strcspn(b, "\n")] = '\0';

    // update- print using %s
    printf("\nThe str1 is: %s\n", a);
    printf("\nThe str2 is: %s\n", b);

    int la = strlen(a);
    int lb = strlen(b);
    // update- empty substring case
    if (la == 0) {
        printf("Position: 0 because the substring is empty\n");
        return 0;
    }

    for (int i = 0; (lb-i) >= la; i++) {
        if (b[i]==a[0]) {
            int j;
            for (j = 0; j < la; j++) {
                if (b[i + j] != a[j]) break;
            }
            if (j == la) {
                printf("\nPosition: %d\n", i);
                return 0;
            }
        }
    }
    printf("\nNot found!\n");
    return 0;
}
