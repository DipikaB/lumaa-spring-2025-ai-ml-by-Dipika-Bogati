# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Dataset Location**:
https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis


### Project Setup:

Firstly, the dataset is downloaded from the above location (https://www.kaggle.com/datasets/samruddhim/imdb-movies-analysis). The downloaded zip file is extracted into the project. The data folder is created inside the project and that downloaded csv file is copied inside the data folder. 

After that virtual environment is setup using the command: python -m venv venv. Then the virtual enviroment is activated and the dependencies are download from the requirements.txt file. Finally, main.py file is ran using: python main.py "I love thrilling action movies set in space, with a comedic twist.". It will display the output in the following way:

                                      title                                               plot
41961                                iSteve          A comedic look at the life of Steve Jobs.
9182                               Amarcord  A series of comedic and nostalgic vignettes se...
34421   Journey to the Edge of the Universe                  A journey through space and time.
17814                Muppet Treasure Island            The Muppets' twist on the classic tale.
35707  Judy Moody and the Not Bummer Summer  Third grader Judy Moody sets out to have the m...

