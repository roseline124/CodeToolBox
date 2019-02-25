#include <fcntl.h> 
#include <unistd.h>//fcntl, write, close
#include <stdio.h>//perror
#include <stdlib.h>//exit
#include <sys/stat.h>
#include <sys/types.h> // open

int main(void) {
	
	int fd; 
	int flag_fl, flag_fd;

	fd = open("190119.txt",O_CREAT, 0644); 
	if (fd ==-1) {
		perror("Open Error");
		exit(1);
	}

	flag_fd = fcntl(fd, F_GETFD); 
	flag_fl = fcntl(fd, F_GETFL); 
	if( flag_fl==-1||flag_fd == -1) {
		perror("Fcntl Error");
		exit(1);
	}


	printf("fildes flag : %d\nfile flag : %d\n", flag_fd, flag_fl); 

	close(fd);

	return 0;
}

