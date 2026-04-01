#include <stdio.h>
// int cmp(short a,short b){
//     short c=a-b;
//     if (c>0) 
//         return 1;
//     else 
//         return 0;
// }
// int main(){
//     short nums[5];
//     for (int i=0;i<5;i++){
//         scanf("%d",&nums[i]);
//     }
//     short largest;
//     largest=nums[0];
//     for (int i=0;i<5;i++){
//        if (cmp(largest,nums[i])==0){
//            largest=nums[i];
//        }
//     }
//     printf("The largest num is: %d\n",largest);
//     return(0);
// }


// update- direct comparison prevents integer overflow
int cmp(short a, short b) {
    if (a > b) 
        return 1;
    else 
        return 0;
}
int main() {
    // update- use an int to fix out issue using %d
    short nums[5];
    // update- change logic to i < 5 to prevent out-of-bounds writes
    for (int i = 0; i < 5; i++) {
        scanf("%hd", &nums[i]);
    }
    short largest;
    largest = nums[0];
    // update- change logic to i < 5 to prevent out-of-bounds reads
    for (int i = 0; i < 5; i++) {
       if (cmp(largest, nums[i]) == 0) {
           largest = nums[i];
       }
    }
    printf("The largest num is: %hd\n", largest);
    return(0); 
}
