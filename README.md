# Data-Structures

A repository of data structures for Python. 

## Sequential Terms

### Abstract Data Type (ADT)

An [**abstract data type (ADT)**][2] is a *set of operations* which access a collection of stored data.

### Data Structure

A [**data structure**][4] is a concrete implementation of an abstract data type.

### Time Complexity

How much **runtime** do need as the inputs to operation get larger.

### Space Complexity

How much **memory (RAM)** we need as the inputs to the operation get larger.

## Big-O Notation

For each data structure, I will provide a description for both the [time complexity][7] and the [space complexity][8] on each operation acting on the data structure within the documentation string of the operation.

### Resources on Big-O Notation

<span style="color:gray">Both time complexity and space complexity use big-o notation</span>.

These are the **best** resources I have compiled for learning about Big-O notation.

##### Time Complexity

1. [Video | CS Dojo | Introduction to Big O Notation and Time Complexity (Data Structures & Algorithms #7)][6]

##### Space Complexity

2. [Video | KodingKevin | Big O Notation: Space Complexity][9]

## Code Style

All code will be written in close regard to the [Google Python Style Guide][5] with the exception of the 2 space rule for any indented line.

I have changed this "two space rule" in the [pylintrc](.pylintrc) on line 295 - `indent-string='    '` if you would like to change it back, simply include you prefered indentation in the quotations for this instruction on this line.

## Resources

List of global resources used in this repository.

🎉 Big thanks to all! 🎉

### General

- [Wikipedia - Abstract Data Type][1]
- [Big-O Cheat Sheet][2]
- [Algorithms & Data Structures Sheets][3]

[1]: https://www.bigocheatsheet.com/
[2]: https://en.wikipedia.org/wiki/Abstract_data_type
[3]: https://cooervo.github.io/Algorithms-DataStructures-BigONotation/index.html
[4]: https://en.wikipedia.org/wiki/Data_structure
[5]: https://google.github.io/styleguide/pyguide.html
[6]: https://youtu.be/D6xkbGLQesk
[7]: https://en.wikipedia.org/wiki/Time_complexity
[8]: https://en.wikipedia.org/wiki/Space_complexity
[9]: https://www.youtube.com/watch?v=_F29n4Z69rE