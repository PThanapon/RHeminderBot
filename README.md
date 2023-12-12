# RheminderBot

## Project Overview

RheminderBot is a Telegram bot designed to help users manage and receive reminders for upcoming events, with a focus on exams. The bot allows users to register, upload their exam schedules, and receive daily reminders about upcoming events.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
  - [Commands](#commands)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration with unique IDs.
- Upload exam schedules in ICS format.
- Receive daily reminders about upcoming events.
- Integration with the Telegram bot API.

## Usage

### Commands

- `/start`: Initiates user registration and provides a unique user ID.
- `/upload`: Allows users to upload exam schedules in ICS format.
- `/check`: Triggers daily reminders about upcoming events.

## Project Structure

- `exam.py`: Handles the processing of ICS files, conversion to CSV, and extraction of exam details.
- `rheminder.py`: Implements the main functionality of the Telegram bot, including user interaction and reminders.
- `test.csv`: Temporary CSV file generated during the processing of exam schedules.
- `base.csv`: Base CSV file for storing extracted exam details.
- `.gitignore`: Specifies files and directories to be ignored by version control.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. Pull requests are also appreciated.

## License

This project is licensed under the [MIT License](LICENSE).
```

Remember to replace placeholder details such as `yourusername` with your actual GitHub username and customize the content based on your project's specifics. Additionally, include the appropriate license file (e.g., `LICENSE`) in your project directory.

