from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models after db initialization to avoid circular imports
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    complete = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'complete': self.complete
        }

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    if title:
        new_todo = Todo(title=title)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.json
    new_todo = Todo(
        title=data.get('title')
    )
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
