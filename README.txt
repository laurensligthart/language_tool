README

Open the german.py file in a python interpreter, or place it
somewhere where a python console can find it. In the console
type 'import german.py' to import the functions to your cur-
rent session.
Alternatively, uncomment the last three lines and run the
program to automatically complete a full practice session.


Short description of the most useful functions:

start()
Call this at the start of your practice session. 
It will ask you for any new words you would like to add. New
words should be given in the format 
*(article) german word*;*(article) english word*
Type 'stop' when you've added all new words.

practice()
Can take arguments 'lang', which can be chosen as de or en,
'm', which should be an int, representing the number of words
you want to practice, and 'new', which is a Boolean represen-
ting whether you want to practice only the new words you add-
ed at the start, or all words in your word list file. If the-
se arguments are not given, it will ask for them automatical-
ly.
The function will ask you m random words from the word list.
If you make a mistake, it will give you the solution and ask
the word again at the end of the list.

update()
Update the word list file to include the new words you added.

finish()
Call this at the end of your practice session.
It will write the new words you've added at the start to the 
word list file.
DO NOT FORGET! Otherwise the new words will be lost.

add()
If you want to add a single word pair, call this function as
add( ("german word", "english word") )
If you want to add multiple words, it's easier to use start()

remove()
If you want to remove a single word pair, call this function 
as remove( ("german word", "english word") )