# Garbage Classification System

This project is a web application for classifying waste images using a pre-trained TensorFlow model. The application allows users to upload images of waste, which are then processed and classified into various categories.

## Project Structure

```
garbage-classification-system
├── app.py                     # Main application script
├── models                     # Directory containing the model
│   └── waste_classifier_model.h5  # Pre-trained Keras model for waste classification
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```

## Installation

To run this project, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd garbage-classification-system
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image of waste (in JPG, PNG, or JPEG format) and the application will classify it, displaying the predicted category and confidence level.

## Model

The application uses a pre-trained Keras model located in the `models` directory. The model is designed to classify waste into the following categories:

- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash
- Shoes
- Clothes
- Biological
- Battery

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.