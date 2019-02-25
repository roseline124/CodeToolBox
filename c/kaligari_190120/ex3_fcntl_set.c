#include <fcntl.h> 
#include <unistd.h>//fcntl, write, close
#include <stdio.h>//perror
#include <stdlib.h>//exit
#include <sys/stat.h>
#include <sys/types.h> // open

int main(void) {
	
	int fd,n; 
	int flag; // flag of file

	fd = open("190119.txt",O_CREAT|O_RDWR, 0644); 
	if (fd ==-1) {
		perror("Open Error");
		exit(1);
	}
 
	flag = fcntl(fd, F_GETFL); // Get information of file flag
	if( flag==-1) {
		perror("Fcntl Error");
		exit(1);
	}
	printf("file flag : %d\n", flag); // Origin of file flag

	flag |= O_APPEND; // plus O_APPEND flag 


	fcntl(fd, F_SETFL, flag); // Set file flag to o_append

	printf("file flag : %d\n", flag); // file flag after change


	n = write(fd, "fcntl : F_SETFL test\n", 20); 
	if (n ==-1) {
		perror("Write Error");
		exit(1);
	}

	printf("%d bytes is written on %d\n", n, fd);

	close(fd);

	return 0;
}

