## AI Personal Email Assistant (Beginner to Intermediate Level)

#### Architectural View

                      +---------------------+
                      |      Gmail API      |
                      +----------+----------+
                                 |
                                 v
                      +----------+----------+
                      |     Email Reader     | <--------+
                      +----------+----------+          |
                                 |                     |
                                 v                     |
         +----------------> Preprocessing              |
         |                       |                     |
         |                       v                     |
         |         +-------------+-------------+       |
         |         |       LLM (OpenAI GPT)     |       |
         |         +-------------+-------------+       |
         |                       |                     |
         |       +---------------+--------------+      |
         |       | Intent Detection & Actioning |      |
         |       +-------+----------------+------+      |
         |               |                |             |
         v               v                v             |
   +-------------+ +-------------+ +-------------+      |
   | Slack Bot   | | Reply Email | | Web Search  | <----+
   +-------------+ +-------------+ +-------------+

#### Tool Used :
Gmail API – Reading and Replying to emails.
Slack API – For messages and bot replies.

#### Setup Instructions :
1. Clone the Repository - git clone https://github.com/your-username/ai-assistant.git
2. Install Requirements -  pip install -r requirements.txt
3. Set up API Credentials - SLACK_BOT_TOKEN ="your-slack-token"
                            SLACK_CHANNEL = "your-channel-id"

#### Running Steps : Run CODE_FILE.ipynb and see the output in the terminal.

#### My Github Repository :   https://github.com/nidhisahani-glitch/NidhiSahani-Wasserstoff--AiInternTask.git

