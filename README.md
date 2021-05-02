# My version of Rabin-Karp algorithm
## 1.Description
The Rabin-Karp algorithm is a string search algorithm that searches for a substring, in the main string using hashing.  
Program return index from which substring starting in the main string or 'Not found' if no substring in the main string  
For example:
1) The main string: ACGCACTGAC  
   Substring: ACT  
   return: 4  
2) The main string: ACGCACTGAC  
   Substring: ACTA  
   return: Not found  
## 2.Input files
There is one input files named 'inputs.txt'  
The first line contains the main string in which we will search for the substring.  
The second line contains the substring.  
## 3.Installation and launch
1) Clone this repository:
>git clone https://github.com/ushakovegor/rabin_karp.git  
>cd rabin_karp/
2) Put your nucleotide sequence in input.txt
3) Using your Python3:
> python3 rabin_karp.py  
4) Using Docker:
>docker build -t rabin_karp .  
>docker run rabin_karp
## 4.Contacts
Thank you for your attention.  
For more information:  
Email: ushakoven@yandex.ru  
Tlg: @ushakoven
