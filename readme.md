# Hand Gesture to Control FPS Game
This project allows you to control the Omen agent in the Valorant first-person shooter (FPS) game using hand gestures captured by a camera in real time. By recognizing specific hand gestures, you can perform various actions with Omen, enhancing your gaming experience.

## Features

- Real-time hand gesture recognition: The project utilizes computer vision techniques to detect and recognize hand gestures in real time.
- Valorant integration: The hand gestures are mapped to specific actions within the Valorant game, allowing you to control Omen using your hands.
- Customizable gestures: The project provides the flexibility to define and customize your own hand gestures, enabling you to personalize your gaming experience.
- Easy setup: The readme includes detailed instructions on how to set up the project and get started quickly.

## Requirements

To use this project, you will need:

- A computer with a camera
- Valorant game installed, supporting custom input mappings
- Python and the necessary libraries (specified in the setup instructions)

## Setup Instructions

1. Clone or download the project repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
> **ALERT:** It is recommended to create a virtual environment before installing the dependencies to avoid conflicts with existing packages.
3. Connect your camera to the computer and ensure it is working properly.
4. Launch Valorant and navigate to the input settings.
5. Configure the game to recognize the specific hand gestures defined in the project.
6. Run the project script `omen.py` once in background and start playing Valorant as Omen using hand gestures.

> **NOTE:** For detailed information on the mapped gestures to the actions in the game, please refer to the `omen.csv` file.

## How it Works

### Step 1 : Collecting & Labeling Data
1. Run the `0_data_collection.py` script to collect and label data for training the hand gesture recognition model.
2. It creates a directory named "Data" to store the collected data if it doesn't already exist.
It prompts the user to enter their name, the number of classes, the labels for each class, and the size of the dataset.
3. It asks for confirmation from the user before entering the training phase, displaying the number of classes and the total number of images.
It initializes the webcam and sets the frame width and height.
4. It iterates over each class and creates a folder/directory for each class inside the "Data" directory.
5. It displays a message to the user, asking them to press the space bar to start collecting data for the current class.
6. It starts a countdown before the training input starts, displaying the remaining time on the screen.
7. It captures frames from the webcam and stores them as images in the corresponding class directory, with filenames based on the counter, user name, and class label.
8. It repeats the above step until the desired number of images is collected for the current class.
9. After collecting data for all classes, it releases the webcam and closes all windows.
10. This code essentially collects a dataset of images from the webcam for multiple classes, allowing the user to label each class and specify the dataset size.

### Step 2 : Creating Database
1. Run the `1_create_database.py` script to create a database from the collected and labeled data.
2. Initializes the mp_hands module from mediapipe for hand detection and tracking.
3. Defines the DATA_DIR variable as the path to the data directory.
4. Initializes empty lists and dictionaries to store data, labels, and other information.
5. Iterates over each class directory in the DATA_DIR.
6. For each image in the class directory, it performs the following steps:
    - Reads the image using cv2.imread.
    - Converts the image from BGR to RGB using cv2.cvtColor.
    - Processes the image using the hands object to detect hand landmarks.
    - If hand landmarks are detected, it extracts the x and y coordinates of each landmark and calculates the relative coordinates.
    - Appends the relative coordinates to the data list and the corresponding label to the labels list.
    - If no hand landmarks are detected, it adds the image path to the notDetected list.
7. Prints a completion message for each class directory.
8. Creates a directory named "Odata" if it doesn't already exist.
9. Saves the data and labels lists as a pickle file named "raw_data.pickle" in the "Odata" directory.
10. Prints a message indicating that the data has been saved.
11. If there are images that were not detected, it prints the paths of those images.
12. Saves the lable_dict dictionary as a CSV file named "label_dict.csv" in the "Odata" directory.
13. Prints a message indicating that the label dictionary has been saved.

### Step 3 : Training the Model
1. Run the `2_train_model.py` script to train the hand gesture 
2. The code loads a pickled data dictionary from the file ./Odata/raw_data.pickle using the pickle.load() function. Pickling is a way to serialize Python objects into a byte stream, allowing them to be saved to a file or transferred over a network.
3. The loaded data dictionary contains two arrays: data and labels. The code converts these arrays into NumPy arrays using np.asarray().
4. The code then splits the data and labels into training and testing sets using the train_test_split() function from scikit-learn. The test_size parameter specifies the proportion of the data to be used for testing, while shuffle=True ensures that the data is randomly shuffled before splitting. The stratify=labels parameter ensures that the class distribution is preserved in the training and testing sets.
5. A RandomForestClassifier model is initialized using model = RandomForestClassifier(). Random Forest is an ensemble learning method that combines multiple decision trees to make predictions.
6. The model is trained on the training data using the fit() method: model.fit(x_train, y_train). This step involves constructing multiple decision trees and aggregating their predictions to make the final prediction.
6. The trained model is then used to predict the labels for the test data: y_predict = model.predict(x_test).
7. The accuracy of the model is calculated by comparing the predicted labels with the actual labels using the accuracy_score() function: score = accuracy_score(y_test, y_predict).
8. The accuracy score is printed to the console using print('Accuracy: {}'.format(score*100)).
9. The code checks if the directory ./Odata exists. If it doesn't, it creates the directory using os.makedirs('./Odata'). This step ensures that the directory exists before saving the model.
10. Finally, the trained model is saved to a file named model.p in the ./Odata directory using pickle.dump(). The model is wrapped in a dictionary before saving.

**Now you can test the model by running the `3_test_model.py` script.**

## Packages Used

*The project utilizes the following packages:*

keyboard, flatbuffers, threadpoolctl, six, pyparsing, pycparser, protobuf, pillow, packaging, numpy, kiwisolver, joblib, fonttools, cycler, colorama, attrs, absl-py, tqdm, scipy, python-dateutil, opt-einsum, opencv-python, opencv-contrib-python, ml-dtypes, contourpy, cffi, sounddevice, scikit-learn, matplotlib, jaxlib, jax, mediapipe.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the project repository.