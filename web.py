from flask import Flask, request, render_template_string

app = Flask(__name__)

FLAG = "PSNACET{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n}"

@app.route("/")
def home():
    return '''
        <h2>Template Renderer</h2>
        <form action="/render">
            <input type="text" name="name" placeholder="Enter something">
            <button type="submit">Render</button>
        </form>
    '''

@app.route("/render")
def render():
    name = request.args.get("name", "")
    
    # 🔥 FULL SSTI (guaranteed execution)
    return render_template_string(name)

if __name__ == "__main__":
    app.run()
