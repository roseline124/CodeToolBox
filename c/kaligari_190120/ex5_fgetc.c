#include <stdio.h>
#include <stdlib.h>

int main(void) {

	FILE *rfp, *wfp; 
	int c; 

	rfp = fopen("190120.txt", "r");
	if (rfp == NULL) {
		perror("fopen : .txt ");
		exit(1);
	}

	wfp = fopen("190120.out", "w");
	if (wfp == NULL) {
		perror("fopen : .out ");
		exit(1);
	}

	while ( (c =fgetc(rfp)) != EOF) {

		fputc(c, wfp);

	}


	fclose(rfp);
	fclose(wfp);

	printf("check file '190120.out'\n");

	return 0;
}
