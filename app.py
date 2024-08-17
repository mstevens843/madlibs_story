from flask import Flask, request, render_template
from stories import stories  # Import stories dictionary

app = Flask(__name__)

@app.route('/')
def home():
    """Show form to collect Madlib words based on story selection."""
    # Get selected story, default to "original"
    story_choice = request.args.get("story_choice", "original")
    selected_story = stories.get(story_choice, stories["original"])

    # Pass prompts for the selected story to the template
    prompts = selected_story.prompts
    return render_template("home.html", prompts=prompts, story_choice=story_choice)

@app.route('/story')
def show_story():
    """Generate and display story from words."""
    # Get selected story
    story_choice = request.args.get("story_choice", "original")
    selected_story = stories.get(story_choice, stories['original'])

    # Collect user input and ensure all answers are non-None strings
    answers = {prompt: request.args.get(prompt, '') for prompt in selected_story.prompts}
    
    # Generate the story with the collected answers
    generated_story = selected_story.generate(answers)
    
    return render_template('story.html', story=generated_story)


if __name__ == "__main__":
    app.run(debug=True)
