#include <stdio.h>
#include <stdlib.h>

int main(void) {

	FILE *rfp, *wfp;
	char s[BUFSIZ];


	if( (rfp = fopen("190120.txt", "r")) == NULL) {
		perror("fopen : .txt");
		exit(1);
	}//file to read

	if((wfp = fopen("190120.out", "w")) == NULL) {
		perror("fopen : .out");
		exit(1);
	}//file to write


	while (fgets(s,BUFSIZ , rfp) != NULL) {
		fputs(s, wfp);
	}

	fclose(rfp);
	fclose(wfp);

	return 0;

}
