ME
 
STUFFS
CollinsCOLLINS
COMPUTER SCIENCE
Cs50 Problem set 1 Solutions 2021: My step by step explanations

Oh yes, I’m so ecstatic, I’ve been able to Cs50 complete Problem set 1, though Mario, Cash, and Credit seem undoable for me at first, after working sleeplessly and thorough research I’ve been able to attempt all. Hello pset is just a copy-paste of what Prof David J.Malan taught us in the video.

here comes my solution, worry not I’ve been able to compile all solutions, if you find anyone daunting or you don’t understand kindly use the comment box, will get back to you.

So let’s dive in.

What To do in Pset1?
We are to go to ide.cs50.io and click “Sign in with GitHub” to access your CS50 IDE.

Submit Hello
Then Submit one of Mario, either feeling less or more comfortable.
Submit one of:

Cash if feeling less comfortable
Credit if feeling more comfortable
Cs50 Problem set 1 Hello Solution
Hello seems to be the easiest of all in this Pset, it only requires you to print your name by writing a program that asks your name and prints out (Hello your name).

Pseudocode

Prompt User for their name
then say Hello User
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What is your name: "); //declare a string with 'name' variable

    printf("hello, %s\n", name); //then print the name with %s 
}
view rawhello.c hosted with ❤ by GitHub
my hello.c solution
Hello Code explanation

I declare a string variable “name” with get_string and ask “What is your name:”
Then print the user’s name with printf(); and also input “hello %s” to make it print the user’s name.
Cs50 Mario less Comfortable Solution

This program was meant to mimics Super Mario steps used in the game, we are to use ‘#’ to represent the above picture like this

       #
      ##
     ###
    ####
   #####
  ######
 #######
########
Pseudocode

Prompt user for height
If the height is less than 1 or greater than 8 (or not an integer at all), go back one step
Iterate from number through height:
On iteration, print hashes and then a newline
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height; //declare int variable Height
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);  //make sure height is not less than 1 or greater than 8

    for (int row = 0; row < height; row++) //to print new line as ROW
    {
        for (int space = height - row - 1; space > 0; space--) //to print SPACE
        {
            printf(" ");
        }
        for (int hash = 0; hash < row + 1; hash++) //to print hashes(#)
        {
            printf("#");
        }
        printf("\n");
    }
}
﻿
view rawmario.c hosted with ❤ by GitHub
Mario less code explanation here

I declare user Mario height with int “height”
I use do while loop to make sure the user cooperates and doesn’t input height larger than 8 or less than 1.
Then use for loop to iterate row over the height so that it can print 8 rows.
Then use another for loop to iterate over row and height for it to print the space required for program to left align the Mario steps.
Hash for loop iterate over row for it to print the “#” like the order of the step
Mario More Comfortable Solutions

This program was meant to print two way super Mario steps with hash “#”.

Pseudocode

The same thing for Mario less, the only thing we are adding is Right align Hash
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height; //declare int variable Height
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);  //make sure height is not less than 1 or greater than 8

    for (int row = 0; row < height; row++) //to print new line as ROW
    {
        for (int space = height - row - 1; space > 0; space--) //to print SPACE
        {
            printf(" ");
        }
        for (int hash = 0; hash < row + 1; hash++) //to print hashes(#)
        {
            printf("#");
        }
        printf("  ");
        for (int right_hash = 0; right_hash < row + 1; right_hash++ )
        {
            printf("#");
        }
        printf("\n");
    }
}
view rawmario_more.c hosted with ❤ by GitHub
Mario more comfortable code explanation

we will start from where we stop the solution at Mario less Comfortable solution.
then print two space printf(” ” );
after then iterate another for loop (right_hash) with row to print right align hash.
Cs50 Problem Set 1 Cash Solution
This Problem set was meant to help sellers make a change for buyer’s easily, It’s design to help the cashier collate the lowest possible number of coins to help make a change for Customers.

Pseudocode

Prompt user for an amount of Change
if the change is less than 0, reprompt the user until cooperate.
Due to floating impression, round the cent to the nearest penny
Then use the largest coins possible, keeping track of coins used.
Print the number of coins.
#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    int count = 0;   //to count
    float change; //declare a float variable "change"
    do
    {
        change = get_float("Change owed: ");  //get change from user
    }
    while (change < 0);    //make sure change is not less than 0
    int cent = round(change * 100); //round off to the nearest whole number

    while (cent >= 25)
    {
        cent = cent - 25; // divide by 25 and give account of remainder
        count++;  //count number of times
    }
    while (cent >= 10)
    {
        cent = cent - 10; //divide by 10 and give account of remainder
        count++;       //count number of times
    }
    while (cent >= 5)
    {
        cent = cent - 5;    //divide by 5 and give account of remainder
        count++;  //count number of times
    }
    while (cent >= 1)
    {
        cent = cent - 1;  //divide by 1 and give account of remainder
        count++;     //count number of times
    }
    printf("%i\n", count);
}