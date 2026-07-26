import logging
import sys
import sqlite3
import datetime
import os
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentServer, AgentSession, JobContext, room_io
from livekit.plugins import noise_cancellation, silero
from livekit.agents.llm import ChatMessage

userloggedin_ID = 0

with open("useridloggedin.txt") as f:
    userloggedin_ID = (f.read())
print(userloggedin_ID)

if os.path.exists("conversation_log.txt"):
    os.remove("conversation_log.txt")

db = sqlite3.connect('Interview_lab_database.db')
cur = db.cursor()

cur.execute(f"SELECT recentjobinfo FROM USERS where id = {userloggedin_ID}")
result0 = cur.fetchone()
recentjobinfo = result0[0]

cur.execute(f"SELECT questiondomainsselected FROM USERS where id = {userloggedin_ID}")
result1 = cur.fetchone()
questiondomainsselected = result1[0]

cur.execute(f"SELECT lengthofinterview FROM USERS where id = {userloggedin_ID}")
result2 = cur.fetchone()
lengthofinterview = result2[0]

cur.execute(f"SELECT interviewerpersona FROM USERS where id = {userloggedin_ID}")
result3 = cur.fetchone()
interviewerpersona = result3[0]

cur.execute(f"SELECT difflevel FROM USERS where id = {userloggedin_ID}")
result4 = cur.fetchone()
difflevel = result4[0]

load_dotenv()

# Define your agent's behavior by extending the Agent class
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=f"as soon as the user speaks let them know the difficulty level which is {difflevel} and the length of intervieww which is {lengthofinterview} and the how you should act in speaking to the user is {interviewerpersona}. also inform the user what question types they selected by reading out this list: {questiondomainsselected}",  # System prompt for the LLM
        )

server = AgentServer()

# The entrypoint function runs when a participant joins the room
@server.rtc_session()
async def entrypoint(ctx: JobContext):
    # Configure the voice pipeline with STT, LLM, TTS, and VAD providers
    session = AgentSession(
        stt="assemblyai/universal-streaming:en",  # Speech-to-text provider
        llm="openai/gpt-4.1-mini",                # Language model for responses
        tts="cartesia/sonic-3",                   # Text-to-speech voice
        vad=silero.VAD.load(),                    # Voice activity detection
    )

    @session.on("conversation_item_added")
    def on_item(ev):
        if not isinstance(ev.item, ChatMessage):
            return
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("conversation_log.txt", "a") as f:
            f.write(f"[{ts}] {ev.item.role}: {ev.item.text_content}\n")


    # Start the session with noise cancellation enabled
    await session.start(
        agent=Assistant(),
        room=ctx.room,
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=noise_cancellation.BVC(),  # Background voice cancellation
            ),
        ),
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agents.cli.run_app(server)