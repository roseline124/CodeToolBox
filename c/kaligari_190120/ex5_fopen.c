#include <stdio.h>
#include <stdlib.h>

int main(void) {

	FILE *fp;

	fp = fopen("190120.txt", "r"); 
	if(fp == NULL)	{
		perror("fopen error");
		exit(1);
	}

	printf("%d\n", fp);

	fclose(fp);	

	return 0;
}
