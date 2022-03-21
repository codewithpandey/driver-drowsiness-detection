# Driver Drowsiness Detection

Exhausted drivers who doze off at the wheel are responsible for about 40% of road accidents, says a study by the Central Road Research Institute (CRRI) on the 300-km Agra-Lucknow Expressway.

Even though this is the era of autonomous cars, but human attentiveness is still required, because the AIs ar not that advanced yet.

To prevent those accidents from happening we can use this software as a prevention measure.

### Data Source
https://www.kaggle.com/datasets/serenaraju/yawn-eye-dataset-new

The data you will get from this source will have all the four folders (Closed, Open, no_yawn, and yawn) will be in the same directory. You have to name that directory as **_archive_**.

After doing so, run the data-separator.py file to split the data in training, testing, and validation sets.

Finally, run the base-model.py to train the models.

### Packages Required
All the required packages (with version) are listed in requirements.txt. To install all of them at once run the following commands on your cmd (preferably as administrator):

pip install pipreqs
pipreqs path/to/project

Or you can also install them manually by using: pip install package_name==version

### How to use
You do not need the dataset for just useing the program, all you have do is install all packages and then run main.py.
