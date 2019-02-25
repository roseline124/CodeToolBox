/*
read by buffer 
*/

#include <stdio.h>
#include <stdlib.h>

int main(void) {

	FILE *fp; 
	char buf[BUFSIZ];
	int n; 

	if((fp = fopen("190120.txt", "r")) == NULL) {
		perror("fopen error");
		exit(1);
	}// file pointer

	while((n=fread(buf, sizeof(char)*8, 5, fp))>0 ) {
		buf[40]= '\0';
		printf("n=%d, buf=%s\n", n, buf); 
	}

	fclose(fp);
	


	return 0;
}
