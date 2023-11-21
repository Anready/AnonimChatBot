# ChatBot Readme

This repository contains a simple chatbot implemented in Python using the Aiogram library. The bot connects users for a chat session, allowing them to communicate with each other. The bot supports various types of messages, including text, stickers, photos, documents, audio, video, voice messages, video notes, and location sharing.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Anready/Anonymous_Chat.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install aiogram==2.25.1
   ```

3. **Set Up Bot Token:**
   Replace `API_TOKEN` in the code with your Telegram Bot API token. You can obtain a token by creating a new bot on Telegram through the [BotFather](https://t.me/BotFather).

4. **Run the Bot:**
   ```bash
   python anon_chat.py
   ```

## Usage

- Start a chat session by sending the `/start` command to the bot.
- Initiate the search for a chat partner with the `/next` command.
- Stop the current chat session with the `/stop` command.
- Send different types of media, such as stickers, photos, documents, audio, video, voice messages, video notes, and location sharing during the chat.

## Commands

- `/start`: Initiates a chat session and provides a welcome message.
- `/next`: Searches for a new chat partner.
- `/stop`: Ends the current chat session.

## Message Handling

The bot handles various types of messages:

- Text messages are relayed to the chat partner.
- Stickers are sent as stickers to the chat partner.
- Photos are shared with the chat partner.
- Documents are sent to the chat partner.
- Audio messages are transmitted to the chat partner.
- Video messages are forwarded to the chat partner.
- Voice messages are relayed to the chat partner.
- Video notes are shared with the chat partner.
- Location sharing is supported during the chat.

## Contributing

Feel free to contribute to the development of this chatbot by opening issues or pull requests. Your feedback and contributions are welcome!

---