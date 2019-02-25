#include <stdio.h> // perror
#include <stdlib.h> // exit 
#include <unistd.h> // read, write, close, dup
#include <sys/stat.h>  
#include <sys/types.h>
#include <fcntl.h> // open


int main(void) {

	int fd, nfd ;//open
	int on, nn;//read
	int won;//write
	off_t current;//lseek
	char *buf[100], *buf2[100], *wr[50];//read, write

	fd = open("190118.txt", O_RDWR);
	if (fd == -1) {
		perror("Open Error");
		exit(1);
	}

	// nfd points to same file with fd
	nfd = dup(fd);	
	if(nfd == -1) {
		perror("Duplicate Error");
		exit(1);
	}
	
	// read offset
	on = read(fd, buf, 50); 
	nn = read(nfd, buf2, 50);
	if (nn== -1|| on==-1) {
		perror("Read Error");
		exit(1);
	}

	// write string only in old file
	won = write(fd, wr, 50);
	if (won == -1) {
		perror("Wrtie Error");
		exit(1);
	}

	// read offset from current position
	on = read(fd, buf, 50); 	
	nn = read(nfd, buf2, 50);
	if (nn== -1|| on==-1) {

		perror("Read Error");
		exit(1);
	}

	// print result
	printf("Old fildes : %d\nOld contents : %s\nNew fildes : %d\nNew contents : %s\n", won, buf, nn, buf2);

	close(fd);
	close(nfd);

	return 0;
}
