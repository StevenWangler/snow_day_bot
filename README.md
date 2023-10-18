---

# Snow Day Predictor

An automated system that uses OpenAI's GPT model combined with weather data to predict the likelihood of snow days for a particular school. It notifies users of these predictions via email.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Weather Forecast Analysis**: Fetches and analyzes weather data to predict snow days based on various factors like temperature, wind speed, humidity, and precipitation.
  
- **OpenAI Integration**: Uses OpenAI's GPT model to:
  - Derive snow day predictions.
  - Generate images based on school-specific prompts.
  - Validate the prediction to check the chance of a snow day.
  
- **Email Notifications**: Sends personalized email notifications to users about the snow day predictions.

- **Google Forms Interaction**: Fetches user sign-up responses from Google Forms to gather recipient data for email notifications.

- **Logging and Configuration**: Utilizes extensive logging for debugging and tracking. Configurations are modularly stored and easily adjustable.

- **Snow Day Policy Reference**: Uses a defined snow day policy to guide predictions.

## Usage

1. Ensure you have set up all configurations in the `settings` module.

2. Run the main application:

```bash
python main.py
```
---

## Configuration & Settings

The `settings` module is a centralized place for all configuration details needed to run the application. Before executing the application, ensure the settings are correctly configured. Here's a breakdown of the main components:

### SMTP Details
- **SMTP_SERVER**: The SMTP server address used for sending emails.
- **SMTP_PORT**: The port used for the SMTP server.
- **SENDER_EMAIL**: The email address used as the sender when dispatching emails.
- **SENDER_EMAIL_PASSWORD**: The password or app-specific password for the sender email.

### OpenAI API Details
- **OPENAI_API_KEY**: Your API key for OpenAI.
- **ENGINE_NAME**: The specific OpenAI engine or model you're using, like "text-davinci-002".
- **CHAT_COMPLETIONS_URL**: The endpoint URL for chat completions with OpenAI.

### School Specific Details
- **SCHOOL_NAME**: The name of the school or institution the application is predicting snow days for.
- **SCHOOL_MASCOT**: The mascot of the school, used for thematic content.
- **SCHOOL_COLORS**: The official colors of the school, potentially used for themed content.
- **SCHOOL_DISTRICT_STATE**: The state in which the school district is located.

### Google Forms API
Ensure you've set up credentials for Google Forms API to fetch user sign-up responses:
- **GOOGLE_SIGN_UP_FORM_ID**: The unique ID of your Google Form used for sign-ups.

### Other Settings
There might be other settings specific to your project's functionality, like paths to certain resources, themes for AI responses, etc. Ensure all such configurations are correctly set before running the application.

---

It's a best practice to never commit sensitive information like API keys or passwords directly in your code or settings file. Instead, consider using environment variables or external configuration files that are ignored by version control.

## Contributing

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes with meaningful commit messages.
4. Push your branch and submit a pull request. Ensure that your pull request describes the changes you made.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---