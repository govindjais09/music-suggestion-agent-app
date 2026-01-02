from app.agents.team_agent import agent_team

if __name__ == "__main__":
    # agent_team.print_response("Suggest me some music based on my recent listens and create a playlist for my workout sessions.", stream=True)
    agent_team.print_response("Give me 50 other similar music by taking reference on this playlist : https://open.spotify.com/playlist/37i9dQZF1DX3Kdv0IChEm9.", stream=True)