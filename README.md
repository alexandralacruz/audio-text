Audio Agent Project
===================
This project provides an end-to-end pipeline for:
1. Receiving audio input.
2. Transcribing speech to text.
3. Correcting grammar via a local LLM.
4. Returning the refined response through an API or notebook.

Run locally:
------------
1. Install dependencies: `pip install -r requirements.txt`
2. Launch API: `uvicorn app.main:app --reload`
3. Test endpoint: `POST /process_audio` with an audio file.

OR
--

Docker Setup:
-------------
1. Build the image: `docker build -t audio-agent .`
2. Run the container: `docker-compose up`
3. Access API at: `http://localhost:8000`
