#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	char input[50];
	int length;
	char flag[50];
} data;

int main()
{
	setbuf(stdout, NULL);
	data d;

	strncpy(d.flag, "REDACTED", sizeof(d.flag));
	
	printf("Enter your text: ");
	scanf("%s", d.input);
	
	printf("Guess the length of this text: ");
	scanf("%d", &d.length);
	
	if (strlen(d.input) == d.length) {
		printf("You guessed the length correctly. Great job!\n");
	} else {
		printf("The actual length of '%s' is %ld, not %d. Sorry :(\n", d.input, strlen(d.input), d.length);
	}
	
	return 0;
}
