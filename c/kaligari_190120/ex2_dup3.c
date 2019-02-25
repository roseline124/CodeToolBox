#include <stdio.h> // perror
#include <stdlib.h> // exit 
#include <unistd.h> // read, close, dup3
#include <sys/stat.h>  
#include <sys/types.h>
#include <fcntl.h> // open
#define _GNU_SOURCE

int main(void) {

	int fd, nfd ;
	int on, nn;
	off_t current;
	char *buf[50];

	fd = open("190118.txt", O_RDONLY);
	if (fd == -1) {
		perror("Open Error");
		exit(1);
	}

	// nfd points to same file with fd
	nfd = dup3(fd, 6, O_CLOEXEC);	
	if(nfd == -1) {
		perror("Duplicate Error");
		exit(1);
	}
	
	// offset test
	current = lseek(fd, 10, SEEK_CUR); 

	// read offset from current position
	on = read(fd, buf, current); 
	nn = read(nfd, buf, current);
	if (nn== -1|| on==-1) {
		perror("Read Error");
		exit(1);
	}

	printf("Old fildes : %d\nOld offset : %d\nNew fildes : %d\nNew offset : %d\n", fd, on, nfd, nn);

	close(fd);
	close(nfd);
	close(6); 

	return 0;
}
