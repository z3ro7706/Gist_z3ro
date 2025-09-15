#include <stdio.h>
#include <string.h>

// 1. Define a Book structure using typedef
typedef struct
{
    char title[100];
    char author[50];
    double price;
} Book;

// 2. Implement the updateBook function
void updateBook(Book *b, char *newTitle, char *newAuthor, double newPrice)
{
    strcpy(b->title, newTitle);
    strcpy(b->author, newAuthor);
    b->price = newPrice;
}

int main()
{
    Book myBook;
    char newTitle[100], newAuthor[50];

    // 3-1. Get the initial title, author, price
    printf("Enter initial book title, author, and price: ");
    scanf("%s %s %lf", myBook.title, myBook.author, &myBook.price);

    // 3-2. Print entered book info
    printf("\nBefore update:\n");
    printf("Title: %s, Author: %s, Price: %.2lf\n", myBook.title, myBook.author, myBook.price);

    // 3-3. Get new book information
    printf("\nEnter new book title, author, and price: ");
    scanf("%s %s %lf", newTitle, newAuthor, &myBook.price); // reuse same price var

    // 3-4. Update using the function
    updateBook(&myBook, newTitle, newAuthor, myBook.price);

    // 3-5. Print modified book info
    printf("\nAfter update:\n");
    printf("Title: %s, Author: %s, Price: %.2lf\n", myBook.title, myBook.author, myBook.price);

    return 0;
}
