# WebHooks with Python

A basic example of a webhook implementation using Python and Flask. This project demonstrates how to create a **webhook listener** and an **event emitter** that communicates via HTTP.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)

---

## Overview

A **webhook** is a mechanism that allows one application to send data to another in real-time when specific events occur. This project includes:

1. **Webhook Listener**: A Flask application that listens for incoming HTTP POST requests.
2. **Event Emitter**: A Python script that sends JSON data to the webhook listener.

---

## Technologies Used

- **Python**: Programming language.
- **Flask**: Web framework for creating the webhook listener.
- **Requests**: Python library for sending HTTP requests.

---

## Setup and Installation

Follow these steps to set up the project locally:

Clone the repository:
   ```bash
   git clone https://github.com/alfadexters/WebHooks-with-Python.git
   cd WebHooks-with-Python
  ```
## How to Run

### Step 1: Start the Webhook Listener
Run the listener to start receiving webhook events:
```bash
python webhook_listener.py
```
The listener will be available at http://localhost:5000/webhook.

### Step 2: Trigger the Event Emitter
Run the emitter to send data to the webhook:

```bash
python webhook_emitter.py
```
Example Output
Webhook Listener Output:

```css
Data received: {'user_id': 123, 'name': 'John Doe', 'email': 'john.doe@example.com'}
```
Event Emitter Output:

```yaml
Webhook sent, server response: 200
```
