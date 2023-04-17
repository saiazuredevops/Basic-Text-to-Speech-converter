Text to Speech Web Application

This web application allows users to convert text into speech by leveraging the Google Text-to-Speech API. Users can input their desired text and choose from various Indian languages for the output speech.
Features

    Convert text into speech
    Support for multiple Indian languages
    Download the converted speech as an MP3 file
    Responsive and user-friendly interface

Installation and Setup

Follow the steps below to set up the Text to Speech web application on your local machine:
1. Clone the repository

Clone the repository using the following command:

    git clone https://github.com/yourusername/text-to-speech.git

Replace yourusername with your GitHub username if you have forked the repository.
2. Install required packages

Navigate to the project directory and install the required Python packages using the following command:

    pip install -r requirements.txt

3. Set up Google Text-to-Speech API credentials

To use the Google Text-to-Speech API, you will need to create a project on the Google Cloud Platform and enable the Text-to-Speech API. Once you have done this, download the JSON key file for your project and place it in the root folder of this repository.

Next, set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of the JSON key file:


    export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key-file.json"

4. Run the application

Run the Flask application using the following command:


    flask run

Now, you can access the Text to Speech web application at http://localhost:5000.
Contributing

If you'd like to contribute to this project, feel free to create a fork and submit a pull request. All contributions are welcome!
License

This project is licensed under the MIT License.
