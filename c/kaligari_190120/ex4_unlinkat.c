#include <stdio.h>//perror
#include <stdlib.h>//exit
#include <unistd.h>//unlink 
#include <fcntl.h>// unlinkat 
#include <sys/stat.h>
#include <sys/types.h>//open

int main(const char *path) { 
	
	int dirfd, check;

	dirfd = open(path, O_RDONLY | O_DIRECTORY);

	check = unlinkat(dirfd, path, AT_REMOVEDIR);

	if (check ==-1) {
		perror("Unlink");
		exit(1);
	}
		
	printf("%s is removed.\n", path);
	close(dirfd);

	return 0; 
} 
