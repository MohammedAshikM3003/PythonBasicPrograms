import google.generativeai as genai
import os

# --- Step 1: Set up your API Key ---
# Option 1: Set as an environment variable (Recommended for security)
# Before running your script, set the environment variable in your terminal:
# On Linux/macOS: export GEMINI_API_KEY="YOUR_API_KEY_HERE"
# On Windows (Command Prompt): set GEMINI_API_KEY="YOUR_API_KEY_HERE"
# On Windows (PowerShell): $env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
# Then, in your Python script:
# genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Option 2: Directly in your code (Less secure, only for quick testing)
# Replace "YOUR_API_KEY_HERE" with the actual API key you copied.
genai.configure(api_key="AIzaSyDDAq7VNYQCuQqGJYLVdiHaq60EGZjte3Y") 

# --- Step 2: Initialize the Generative Model ---
# We'll use a model suitable for text generation/summarization.
# 'gemini-1.5-flash' is a good balance of speed and capability for summarization.
# 'gemini-1.5-pro' is more powerful but might have slightly different free tier limits.
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Step 3: Define the text to summarize ---
meeting_notes = """
Meeting held on July 9, 2025, concerning the Q3 marketing strategy.

Attendees: Sarah (Marketing Lead), John (Sales Director), Emily (Product Manager), David (CEO)

Agenda:
1. Review of Q2 Performance
2. Discussion of Q3 Goals
3. Brainstorming New Campaigns
4. Action Items

Key Discussions:
* Q2 performance was strong in North America but saw a slight decline in EMEA due to increased competition.
* Q3 goals include increasing lead generation by 15% globally and improving customer retention by 5% in EMEA.
* New campaign ideas included a "Summer Sales Blitz" for North America, a partnership with a local influencer in EMEA, and a loyalty program revamp for all regions.
* John suggested focusing on existing customer upselling in EMEA.
* Emily highlighted the need for updated product collateral for the new loyalty program.
* David emphasized data-driven decisions and A/B testing for all new campaigns.

Action Items:
* Sarah: Develop detailed plan for "Summer Sales Blitz" by July 15.
* John: Research potential EMEA influencers and present options by July 20.
* Emily: Update product collateral for loyalty program by July 25.
* David: Schedule follow-up meeting for campaign approval on July 28.
"""

# --- Step 4: Send the text to the model for summarization ---
try:
    response = model.generate_content(f"Summarize the following meeting notes:\n\n{meeting_notes}\n\nProvide a concise summary highlighting key decisions and action items.")

    # --- Step 5: Print the summarized text ---
    print("Meeting Summary:")
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure your API key is correct and you have an active internet connection.")
    print("You might also be exceeding the free tier limits. Check Google AI Studio for details.")
