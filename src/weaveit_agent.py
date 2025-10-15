from uagents import Agent, Context
from video_bridge import generate_video
from metta_integration import reason_with_metta

agent = Agent(
    name="WeaveItAgent",
    seed="weaveit-secret-seed",  # replace later with a secure one
)

@agent.on_message(model=str)
async def handle_message(ctx: Context, message: str):
    ctx.logger.info(f"Received query: {message}")

    # Step 1: Reason with MeTTa Graph
    context = reason_with_metta(message)

    # Step 2: Send to WeaveIt for video generation
    video_url = generate_video(context)

    # Step 3: Return link
    await ctx.send(ctx.sender, f"🎥 Watch your tutorial here: {video_url}")

if __name__ == "__main__":
    agent.run()
