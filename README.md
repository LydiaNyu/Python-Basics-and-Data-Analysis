## Introduction 
This is a school homework deals with python basics(bits operations,`bits.py` ) and data analysis(analyzing two books `book.ipynb` ).

## Requirements
Part 1: BitList Class.  
Define custom errors; causing and handling runtime errors (Exceptions).  
Create the BitList class; it should support the following behavior:  
1. BitList.from_ints(b1, b2, ...bN): A new series of bits can also be created by supplying integers directly to a @staticmethod from_ints.    
2. Converting to a str: Implement the appropriate method on the BitList class such that converting to a list (such as when using str or printing out a value) a BitList instance displays every bit in the series of bits  
3. arithmetic_shift_left() and .arithmetic_shift_right().  
4. .bitwise_and(otherBitList).  
5. .chunk(chunk_length): This method has a single parameter, an int representing the length of the chunks that the instance of BitList should be split up by…. and it returns a list of lists, with each sub list containing bits.  
6. .decode(encoding='utf-8'): This method has a single parameter, the encoding (a str), and it returns a string:  

## Part 2: Books
Using at least two books from project Gutenberg use file io and basic Python to manipulate the content of the books.  
