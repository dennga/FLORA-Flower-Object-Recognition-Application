# FLORA: Flower Object Recognition Application 🌸

## Overview

FLORA is a modern, full-stack machine learning application designed to perform high-accuracy, multi-class image classification. As the successor to the "Loki" project, FLORA leverages **Transfer Learning** with a state-of-the-art pretrained model to achieve superior performance.

The project is built on a decoupled, API-first architecture, featuring a **Python/Flask REST API** backend and a reactive **TypeScript frontend**. This structure demonstrates a professional and scalable approach to deploying machine learning models as interactive web services. This instance is configured to classify different species of flowers, but the architecture can be adapted to any multi-class problem.

![Aktivitätsdiagramm des FLORA-Projekts](FLORA_UML.svg)

## Features

### Backend (Flask API)

* **High-Accuracy Predictions:** Utilizes a pretrained model (e.g., MobileNetV2) fine-tuned for a specific multi-class task, achieving high accuracy with minimal training time.

* **Transfer Learning Workflow:** The entire pipeline for loading a base model, freezing its layers, and training a new classification head is implemented.

* **RESTful API:** A clean, stateless API built with Flask. The `/api/predict` endpoint accepts image uploads and returns structured JSON responses.

* **Scalable Structure:** Organized to handle complex logic, data processing, and model serving efficiently.

### Frontend (TypeScript App)

* **Reactive UI:** A dynamic and responsive user interface built with TypeScript (and a modern framework like React or Vue).

* **Asynchronous Communication:** Interacts with the backend API asynchronously using the `fetch` API, providing a smooth user experience without page reloads.

* **Component-Based:** Structured with reusable components for clean code and maintainability.

* **Type Safety:** Leverages TypeScript to prevent common runtime errors and improve developer experience.

## Tech Stack

* **Backend:**
    * **Language:** Python
    * **Web Framework:** Flask
    * **Machine Learning:** TensorFlow, Keras
    * **Data Processing:** NumPy

* **Frontend:**
    * **Language:** TypeScript
    * **Framework/Tooling:** React (or Vue), Vite
    * **Styling:** Bootstrap / Tailwind CSS

* **Infrastructure & Tooling:**
    * **Version Control:** Git
    * **Containerization:** Docker (optional)


The frontend application will be accessible at http://localhost:5173 (or another port specified by Vite).

## Author

Dennis Garscha

## Project Structure

FLORA employs a monorepo structure with a clear separation between the backend and frontend applications.

```text
FLORA/
├── backend/                  # The Flask API and ML service
│   ├── app.py
│   ├── requirements.txt
│   ├── src/
│   ├── data/
│   └── models/
│
├── frontend/                 # The TypeScript web application
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── tsconfig.json
│
└── README.md                 # Project documentation



