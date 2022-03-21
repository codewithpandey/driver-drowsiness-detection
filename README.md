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

<p style="background:black">
<code style="background:black;color:white">
C:\Users\YOUR_USERNAME>pip install pipreqs  
C:\Users\YOUR_USERNAME>pipreqs path/to/project
</code>
</p>

Or you can also install them manually by using: pip install package_name==version

### How to use?
You do not need the dataset for just using the program, all you have do is install all the required packages and then run - main.py.
But if you want to go through the whole experience or may be play around with the code, follow this:
- First follow the steps under _Data Source_.
- Then follow the steps under _Packages Required_.
- Then open up your Jupyter Notebook or Google Colaboratory(packages are already installed in Colab) and start running the base-model.ipynb
- Finally run main.py to use the application.

### How the application works?
After you click the Start button on the app, the application takes your picture every 100 miliseconds. Then using computer vision, the pictures of your eyes will be cropped out from your face. Then the program uses the image of the eye to see if it's closed or open and the image of the face to see if you are yawning or not. If any of those conditions match (closed eyes or yawning), the app shows **"Drowsy"** at the bottom of the window, and plays a sound to wake you up.
