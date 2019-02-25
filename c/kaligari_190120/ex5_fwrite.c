/*
 write by buffer
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {

	FILE *rfp, *wfp; 
	char buf[BUFSIZ];
	int n; 

	if((rfp = fopen("190120.txt", "r")) == NULL) {
		perror("fopen : .txt");
		exit(1);
	} // fopen for read 

	if((wfp = fopen("190120.out", "w")) == NULL) {
		perror("fopen : .out");
		exit(1);
	} // fopen for write

	while((n = fread(buf, sizeof(char)*5, 3, rfp)) > 0) {
		fwrite(buf, sizeof(char)*5, n, wfp);
	}

	fclose(rfp);
	fclose(wfp);

	return 0;
}
