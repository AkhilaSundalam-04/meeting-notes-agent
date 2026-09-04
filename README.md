# Meeting Notes Agent

A simple AI-powered Meeting Notes Agent built with Python and Streamlit. The application reads meeting transcripts, extracts important discussion points, and generates concise summaries for quick review.

## Features

- Upload and process meeting transcripts
- Extract key discussion points
- Generate concise meeting summaries
- Simple and user-friendly Streamlit interface
- Easy to extend with NLP features

## Project Structure

```
meeting-notes-agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── sample_data/
│   ├── transcript1.txt
│   ├── transcript2.txt
│   └── transcript3.txt
│
└── utils/
    ├── extractor.py
    └── summarizer.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AkhilaSundalam-04/meeting-notes-agent.git
cd meeting-notes-agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

## Sample Use Case

Input:

```
Team Lead: Excellent. What are the tasks for today?

Akhila: I will work on the profile management module.

Rahul: I will complete API integration and testing.
```

Output:

```
Summary:
- Akhila will work on the profile management module.
- Rahul will complete API integration and testing.
- Team discussed today's tasks.
```

## Technologies Used

- Python
- Streamlit
- Git
- GitHub

## Author

**Akhila Sundalam**

GitHub: https://github.com/AkhilaSundalam-04