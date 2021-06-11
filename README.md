# Application for checking SKNF

## Software implementation
Within the framework of the project, an algorithm was implemented using standard Python tools to check whether the formula is SCNF. The essence of the algorithm 
is to work with strings and lists.
## Grammar of the Utterance logic language
* < constant > ::= 1|0 
* < symbol > ::= A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
* < negation > ::= !
* < conjunction > ::= /\
* < disjunction > ::= \/
* < implication > ::= ->
* < disjunction > ::= \/
* < opening bracket > ::= (
* < closing bracket > ::= )
* < binary bundle > ::= < conjunction > | < disjunction > | < implication > | < equivalence >
* < atom > ::= < symbol >
* < unary complex formula > ::= < opening bracket > < negation > < formula > < closing bracket >
* < binary complex formula > ::= < opening bracket > < formula > < binary bundle > < formula > < closing bracket >
* < formula > ::= < constant > | < atom > | < unary complex formula > | < binary complex formula >

## Testing system
As part of the laboratory work, 24 tests were created using the unittest module to check the correct operation of the program.
## GUI
With the help of the tkinter library, a simple interface was created that allows you to click on the “Check” button to display a dialog box with the result of 
checking the formula that is entered in the string.

<p align="center">
  <img src="https://user-images.githubusercontent.com/65425021/121744773-10fd1680-cb0c-11eb-97e1-16e0d964aace.png" />
</p>
