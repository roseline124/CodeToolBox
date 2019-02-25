/*
fprintf : print from file
*/

#include <stdio.h>
#include <stdlib.h>

int main(void) {

	FILE *rfp, *wfp;
	int id, ko, en, mth; // student number, korean, english, math score
        int n;

	if((rfp = fopen("190120_2.txt", "r")) == NULL) {
		perror("fopen : .txt");
		exit(1);
	} // open file to read

	if((wfp = fopen("190120_2.out", "w")) == NULL) {
		perror("fopen : .out");
		exit(1);
	} // open file to write

	fprintf(wfp, "No | Score avg\n");
	while((n =fscanf(rfp, "%d %d %d %d", &id, &ko, &en, &mth)) >0) {
	       fprintf(wfp, "%d  | %d\n", id, ((ko+en+mth)/3));
	} 	       


	fclose(rfp);
	fclose(wfp);


	return 0;
}
