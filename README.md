# GrocEasy
Helps individuals optimize their time spent on Supermarkets

# Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Credits](#credits)

# Introduction
This algorithm was created for our Algorithms & Data Structures class at IE University. 

Groceasy is an application that maps out the shortest route to get all your desired items at a supermarket. 

Its main purpose is to optimize the time you spend grocery shopping at the supermarket. 
Groceasy was made for those busy individuals who always want do grocery shopping as fast as possible.

**Limitations** 
* The Algorithm is currently limited to a predefined supermarket

# Installation 
To run our program, we have installed and imported the following packages:
* Python programming language (version 3.11.0, although it will work with other versions)
* NumpPy library:
`````
pip install numpy
`````
* Pandas library:
`````
pip install pandas
`````
* json library :
`````
pip install json
`````
* JSONEncoder:
 `````
from json import JSONEncoder
 `````
* DefaultDict:
`````
pip install typing
from typing import DefaultDict
`````

Once you have the libraries installed and set up, you can open the file named Algorithm.py and run the program.

# Usage

1. After running the code, it will ask you to type 'import' or new'. 
  * If it is the first time running the code type 'new' in order to create a new route. 
  * Otherwise, if you want to import old routestype 'import'.

     1a. After typing 'new', you will have to input the desired sections one by one.
     - **Note** that on the code there are instructions on how to input the sections. Just in case, you have to type the section and the desired number, the name of the section such as "Bakery" is not necessary

    The Sections provided are the following:
    - Section 2: Bakery
    - Section 3: Meat
    - Section 4: Frozen products
    - Section 5: Fruits and vegetables
    - Section 6: Drinks
    - Section 7: Cleaning Products
    - Section 8: Seafood


     1b. If you have typed import. The algorithm will ask you to type the name of the route
      * Remember to type the name of the route exactly as it wast. If not, the algorithm will not find youre route

2. After the Sections are inputed and you have typed 'q'. The algorithm will ask you to save or continue 

   2a. If you want to save the route, type 'save'
    * Afterwards, type the desired name for the Route (Be sure to not forget the Route name you have saved). The user will get asked if he/she would like to import a shopping list from another usage or to start a new one.
    * Finally once you have typed the name, the algorithm will proceed to give you the most optimized route and steps based on youre preferences.

   2b. If you do not want to save and desire to continue type 'next'
    * The algorithm will proceed on giving you the most optimized route and steps based on youre preferences. 

  
## Extra information about the code
The main algorithm we used for the code is:
* The Greedy Approach 
  * From it we mainly used the traveling salesman problem

Some data structures that we used in the algorithm are:
- Arrays
- Matrices
- Dicitonaries and lists
- Many more functions imported from libraries libraries

# Future Implementations
- [ ] Stock availability for users
- [ ] Expand to more supermarkets in Spain
- [ ] Improve optimized route and create a visual route for users


# Credits
The project was created by:
- Anita Rull 
- Nora Rosa
- Sebastian Llobet 
- Alberto Padilla
- Ramon Zubiaga
- Cristina Tuduri
