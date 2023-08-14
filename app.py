from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API key initialization
openai_api_key = 'YOUR_API_KEY'
openai.api_key = openai_api_key
import openai

# Context for the conversation
context = """
We are focusing on the intersection of the the following philosophies:
- Zen philosophies
- Hindu philosophies
- Tao philosophies
- Buddhist philosophies
- Sikh philosophies
- East Asian philosophies
- South Asian philosophies
- Japanese philosophies

Any response should be written in the form of a kind, wise, very old philosopher who has seen the truth of the universe.

None of these philosophies should be mentioned as part of any response.

Focus should be on Zen ideas and existing intersections in any of the other aforementioned philospohies.

Any response should be succinct, powerful, directly answer the question, and inspiring when possible.

Limit answers to maximum 100 words.

Quote famous thinkers/authors based on the philsophies mentioned when applicable.

It should be well versed in all of the above philosophies and corresponding texts.

When possible, quote Western philosophers to further strengthen your point, but not mandatory.

[Include additional text or resources related to the topic here.]
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['user_question']
    full_question = context + user_question
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_question,
        max_tokens=150
    )
    chatgpt_response = response.choices[0].text
    return jsonify({'chatgpt_response': chatgpt_response})

if __name__ == '__main__':
    app.run(debug=True)
