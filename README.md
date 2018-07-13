# Analysis Of Peptides 

The objective of the project was to study proteome concepts, where the focus was to find proteins in a database (in this case, the file "uniprot-human.fasta") associated with single peptides of samples (in this case, the files: "T4evidence .txt, "being a list of peptides of 1 sample," T4-T8evidence.txt ", being a list of peptides of 2 samples combined and" Immuneevidence.txt ", being a list of peptides of 8 samples combined). In this project the libraries were used: pandas, for manipulation of dataframes and series (a data structure similar to a dictionary); numpy for search operations on dataframes and multiprocessing columns, to parallelize the search for peptides in the protein bank.

First, the file "uniprot-human.fasta" was used as input, so within a loop, each line of the file was read, where the IDs and sequences of each protein contained in the database were searched and soon after, it was added in a dictionary as the key and its respective sequence as value. Then the data was converted to series, shortly after it was converted to dataframe and saved to a file called "processData.csv", which can be found in the "result" folder in the repository described above. The beginning of the created dataframe can be seen below:

| proteinID | Sequence              |
|-----------|-----------------------|
| P0C7Y4    | MGIIAGIIKVIKSLIEQFTGK |
| P52212    | MTSTKNLAKAIVILYAICFFT |
| P15743    | MIVILYAICFFTNSDGRPMMK | 
| ...       | ...                   |

Then, we searched for the proteins with unique peptides, so we used the file "processData.csv" with the protein sequences and their respective IDs from the previous script, in addition to the files ("T4evidence.txt", "T4-T8evidence.txt "And" Immuneevidence.txt ") of the peptide samples. First, the sample file was read in the line of code written like this: peptides = pd.read_csv ("../input/T4evidence.txt", sep = '\ t'). Soon after, put in a dataframe. Attempt to change the first parameter of the ".read_csv" function used in reading, which refers to the location of the input sample file, which will generate different outputs given different samples. Then several non-important columns will be removed for analysis, leaving only the peptide sequence column. Soon after, the peptide redundancy of the dataframe was removed, as well as the creation of a column to account for such redundant frequency of each peptide contained in the dataframe. Prior to the main processing, the file "processData.csv" read as a dataframe in a list of tuples (where the first element would be the sequence and the second element would be the respective protein ID) was transformed and the file of sample read as a dataframe in a dictionary (where the key is the peptide sequence and the value is its frequency in the read file). Finally, a signature function "def findPeptide (protein, peptide)" was created, which receives as a parameter a protein and a peptide, which will return the protein ID if the peptide passed as a parameter is contained in the protein sequence. Then, a loop was looped, which iterated over the peptides of the dictionary, where with the help of the starmap function of the multiprocessing library, it was possible to create several processes that used the findPeptide function to parallel the presence of the peptide in the list of tuples of the proteins, returning a list of all returns. Subsequently, the None returns were removed, and then saved in a dictionary, where the key was the peptide sequence and its value, the return list of the findPeptide function with the sequence IDs that contain such a peptide. In short, at each iteration of the loop a peptide will be searched throughout the protein bank and saved in a dictionary the IDs of the sequences that contain such a peptide. Soon after, will be removed from the dictionary, all the peptide keys containing as values, lists larger than one, that is, only left peptides that occurred in only one protein. Soon after, the dictionary will be transformed into a dataframe, where the columns will be: the sequence of the peptide and the ID of the protein associated with it. It will also be saved to a file named "peptideUnique.csv", which can be found in the "result" folder in the repository described above. The beginning of the created dataframe can be seen below:

| Peptide               | proteinID |
|-----------------------|-----------|
| AAAAAAAAAAAAAAAAAAAAA | P0C7Y4    |
| AAAAAAAAAAAAAAAAAAAAA | P52212    |
| AAAAAAAAAAAAAAAAAAAAA | P15743    | 
| ...                   | ...       |

Lastly, in the last script will read the file "peptideUnique.csv" as dataframe and will be searched inside the ID column of proteins, single proteins, soon saved such proteins with at least one single peptide in a file called "proteinsUnique. txt "and printed on the screen the number of proteins listed.

### Prerequisites

You will need to install the modules below to run the program: 
* [python 3.7 or greater](https://www.python.org/downloads/release/python-370/)
* [pandas](https://pypi.org/project/pandas/)
* [numpy](https://pypi.org/project/numpy/)

### Running

There are two ways to run the program:

* Compile the IDE (PyCharm - Python IDE):
1. Just open the IDE
2. Import the project folder as a Project
3. Select Run/Debug Configurations:
4. Choose Run 0-preProcess on the context menu.
5. Choose Run 1-peptideUnique on the context menu.
6. Choose Run 2-proteinUnique on the context menu.
7. From this it only interacts with the system and add in script parameters box contents:

* Compile by terminal:
1. Enter the src folder and run the following command:
For 0-preProces:
```
python 0-preProcess.py
```
For 1-peptideUnique:
```
python 1-peptideUnique
```
For 2-proteinUnique:
```
python 2-proteinUnique
```
2. From this it only interacts with the system.

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - A IDE used

## Authors
### Developers: 
* **Luís Eduardo Anunciado Silva ([cruxiu@ufrn.edu.br](mailto:cruxiu@ufrn.edu.br))** 
### Project Advisor: 
* **Sandro Jose De Souza ([sandro@neuro.ufrn.br](mailto:sandro@neuro.ufrn.br))**

See also the list of [contributors](https://github.com/cruxiu/IMD0603-AnalysisOfPeptides/contributors) who participated in this project.

## License

This project is licensed under the GPL 3.0 - see the [LICENSE](LICENSE) file for details
