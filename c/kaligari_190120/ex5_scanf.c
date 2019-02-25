/*

scanf, fscanf : get the string with format

*/

#include <stdio.h>
//#include <stdlib.h>

int main(void) {

	char buf[BUFSIZ];

	scanf("%s", &buf);//scanf returns the number of string
	printf("written message : %s\n", buf);

	return 0;
}
