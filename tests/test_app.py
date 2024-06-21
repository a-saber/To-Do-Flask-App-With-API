import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_index(client):
    """Test the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List' in response.data

def test_add_todo(client):
    """Test adding a new todo."""
    response = client.post('/add', data={'title': 'New Todo'})
    assert response.status_code == 302  # Redirect status
    with app.app_context():
        todo = Todo.query.filter_by(title='New Todo').first()
        assert todo is not None

def test_get_todos_api(client):
    """Test the /api/todos endpoint."""
    with app.app_context():
        db.session.add(Todo(title='Sample Todo'))
        db.session.commit()
    response = client.get('/api/todos')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'Sample Todo'

def test_create_todo_api(client):
    """Test creating a todo via the API."""
    response = client.post('/api/todos', json={'title': 'API Todo'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'API Todo'
    with app.app_context():
        todo = Todo.query.filter_by(title='API Todo').first()
        assert todo is not None