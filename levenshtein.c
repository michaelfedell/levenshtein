#include <stdio.h>

int lev(char w1[], char w2[]) {
    printf("word1: %s\n", w1);
    printf("word2: %s\n", w2);
    return 5;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        // TODO: use errors/exceptions to handle bad input
        printf("Function requires exactly two arguments, you provided %d\n", argc - 1);
        return 1;
    }

    printf("Levenshtein distance between %s and %s is %d\n", argv[1], argv[2], lev(argv[1], argv[2]));

    return 1;
}

