# bot_korki
#A discrod bot for my math/programming tutoring lessons

## Functionality
Upon a new member's arrival, the bot requests their name and subsequently generates a dedicated section comprising both voice and text channels exclusively for that user. Access to these channels is restricted to the admin and the respective user. This system effectively organizes students into their individual spaces, ensuring they are unable to view other channels.


## Requirements

- Discord

You can install the required Python packages using the provided `requirements.txt` file. Run the following command:

```
pip install -r requirements.txt
```

## How to Use

1. **Insert Your Discord Bot Token**

    Before you can run the bot, you'll need to insert your own Discord bot token into the code. Locate the designated section for the token and replace `YOUR_BOT_TOKEN_HERE` with your actual token.

    ```python
    # Insert your Discord bot token here
    bot_token = 'YOUR_BOT_TOKEN_HERE'
    ```

2. **Run the Bot**

    Once you've added your bot token, you can proceed to run the bot. Depending on your environment, you can start it via a terminal or command prompt.

    ```bash
    python main.py
    ```
