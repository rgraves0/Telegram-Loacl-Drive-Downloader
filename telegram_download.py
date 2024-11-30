from telethon import TelegramClient, events
import os

# Define the API ID and hash obtained from Telegram
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# Define the phone number associated with your Telegram account
phone_number = 'YOUR_PHONE_NUMBER'

client = TelegramClient('session_name', api_id, api_hash)

local_directory = 'path/to/your/local/directory'

if not os.path.exists(local_directory):
    os.makedirs(local_directory)

@client.on(events.NewMessage)
async def handler(event):
    # Check if the message contains any media (files)
    if event.message.media:
        # Download the file to the local directory
        file_path = await client.download_media(event.message, local_directory)
        print(f'File saved to {file_path}')

async def main():
    # Start the client and log in
    await client.start(phone_number)
    print('Client created and logged in')

    # Run the client until disconnected
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
