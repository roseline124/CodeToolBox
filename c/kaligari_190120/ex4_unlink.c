#include <stdio.h>//perror
#include <stdlib.h>//exit
#include <unistd.h>//unlink 

int main(void) {

	//char *pathname[100]; 
	char *pathname = "/root/Public/ex_unix/test_tt.txt"; //'./' + filename;
	
	int check;

	check = unlink(pathname);
	if (check ==-1) {
		perror("Unlink");
		exit(1);
	}
		
	//printf("%s is removed.\n", filename);

	return 0; 
} 
