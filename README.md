# RheminderBot

## Project Overview

RheminderBot is a Telegram bot designed to help users manage and receive reminders for upcoming events, with a focus on exams. The bot allows users to register, upload their exam schedules, and receive daily reminders about upcoming events.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
  - [Commands](#commands)
- [Project Structure](#project-structure)

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
- `base.csv`: Base CSV with important date from 2023 Coursereg
- `events_userid.csv`: CSV file generated from combining `base.csv` with the exam date received from the ICS file

