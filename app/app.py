from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.ollama import Ollama
from phi.model.google import Gemini
import dotenv
dotenv.load_dotenv()

normal_suggestion_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    name="Normal Suggestion Agent",
    role="""You are a specialized music recommendation expert. """,
    instructions="""Your sole purpose is to:
    - Analyze the user's music from ther provided tracks, artists, albums, or genres
    - Identify patterns in their listening preferences
    - Provide personalized music recommendations that match their taste
    - Explain why each recommendation fits their preferences
    
    You should ONLY handle music recommendation requests and politely decline any other tasks.""",
    markdown=True
)


playlist_suggestion_agent = Agent(
    model= Gemini(id="gemini-2.5-flash", temperature=0),
    name="Playlist Suggestion Agent",
    role="Music Recommendation Agent",
    show_tool_calls=True,
    markdown=True,
    instructions="""
        Given the playlist with the link provided, suggest other similar music based on the pattern, genre, or artist style of the songs in this playlist. 
        Prioritize tracks that match the mood, genre, or overall vibe of the playlist, without including additional tasks.
    """
)



agent_team = Agent(
    team=[normal_suggestion_agent, playlist_suggestion_agent],
    instructions="use the appropriate agent to handle music recommendation requests only.",
    model= Gemini(id="gemini-2.5-flash", temperature=0),
    markdown=True
)   

# agent_team.print_response("Suggest me some music based on my recent listens and create a playlist for my workout sessions.", stream=True)
agent_team.print_response("Give me 50 other similar music by taking reference on this playlist : https://open.spotify.com/playlist/37i9dQZF1DX3Kdv0IChEm9.", stream=True)