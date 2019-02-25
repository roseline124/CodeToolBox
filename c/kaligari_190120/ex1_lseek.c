#include <unistd.h> // read(), write(), close()
#include <sys/types.h> // lseek()
#include <stdio.h> // perror
#include <stdlib.h> // exit()
#include <fcntl.h> 
#include <sys/stat.h> // open()


int main(void) {

	int fd, n;  
	char *buf[100];

	off_t current;

	// creat file if it doesn't exist
	fd = open("190118.txt", O_CREAT); 
	if (fd == -1) {
		perror("Open Error");
		exit(1);
	} // open error

	//current  = lseek(fd, 10, SEEK_END); // offset 10 from end(90)
	current  = lseek(fd, 10, SEEK_SET); // offset 10 from first(0)
	current  = lseek(fd, 10, SEEK_CUR); // offset 10 from current(80/10)
	//current = lseek(fd, 10, SEEK_DATA); // offset 10 to data 

	if (current == -1) {
		perror("Offset Error");
		exit(1);
	} // lseek error

	n = read(fd, buf, current); // read 100 characters
	if (n ==-1) {
		perror("Read Error"); 
		exit(1);
	} // read error

	buf[n] = '\0';// recognize end of the string

	printf("offset : %d\nbytes : %d\ncontents : %s\n", current, n, buf);

	close(fd);
	return 0; 
}



