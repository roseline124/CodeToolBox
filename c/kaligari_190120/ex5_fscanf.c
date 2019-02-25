/*
scanf : get string from standard (monitor, terminal)
fscanf : get string from file
  */

#include <stdio.h>
#include <stdlib.h>

int main(void) {

	FILE *fp;
        char buf[BUFSIZ];	
	int n;

	if((fp = fopen("190120.txt", "r") )==NULL) {
		perror("fopen error");
		exit(1);
	}

	if((n=fscanf(fp, "%s", &buf)) == 0) {
		perror("fscanf error");
		exit(1);
	} 

	printf("n : %d\nbuf : %s\n", n, buf); 
		       


	fclose(fp);

	return 0;
}

