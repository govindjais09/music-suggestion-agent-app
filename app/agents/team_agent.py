from .playlist_agent import playlist_suggestion_agent
from .normal_agent import normal_suggestion_agent
from phi.agent import Agent
from phi.model.ollama import Ollama
import dotenv
dotenv.load_dotenv()


agent_team = Agent(
    team=[normal_suggestion_agent, playlist_suggestion_agent],
    instructions="use the appropriate agent to handle music recommendation requests only.",
    model= Ollama(id="llama3.1"),
    markdown=True
)   
