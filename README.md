# Malaria Detection using CNN and TensorFlow

This project implements a basic **Malaria Detection System** using **Convolutional Neural Networks (CNN)** and **TensorFlow**. The model classifies cell images as either **infected** or **uninfected**, helping in the early detection of malaria.

## Features

- **Deep Learning-based Classification**: Uses CNN to distinguish between malaria-infected and healthy cells.
- **Image Processing**: Preprocesses input images for accurate model training.
- **Model Training & Evaluation**: Trained using TensorFlow and Keras with labeled malaria cell images.
- **Basic User Interface (Optional)**: Can be integrated with a simple UI for easy image upload and classification.

## Dataset

The dataset used is the **NIH Malaria Cell Images Dataset**, which consists of:
- **Parasitized** (Infected) cell images.
- **Uninfected** (Healthy) cell images.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aashka1/Malaria-Detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Malaria-Detection
   ```
3. Install dependencies:
   ```bash
   pip install tensorflow keras numpy matplotlib opencv-python
   ```

## Usage

1. **Prepare the dataset**: Ensure the malaria cell images are stored in appropriate directories (`Parasitized/` and `Uninfected/`).
2. **Run the training script**:
   ```bash
   python train.py
   ```
3. **Evaluate the model**:
   ```bash
   python evaluate.py
   ```
4. **Make predictions on new images**:
   ```bash
   python predict.py --image path_to_image
   ```

## Model Architecture

The CNN model consists of:
- **Convolutional Layers**: Extract features from cell images.
- **Max Pooling Layers**: Reduce dimensionality while retaining important features.
- **Fully Connected Layers**: Classify images as infected or uninfected.
- **Softmax Activation**: Provides probability scores for classification.

## Technologies Used

- **TensorFlow & Keras**: For building and training the CNN model.
- **Python**: Core programming language.
- **NumPy & OpenCV**: Image preprocessing and handling.
- **Matplotlib**: Visualizing training accuracy and loss.

## Future Improvements

- Improve accuracy by experimenting with deeper CNN architectures.
- Implement data augmentation for better generalization.
- Develop a web-based or mobile app for easy malaria detection.


