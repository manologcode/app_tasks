from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Boolean, default=True)
    at_created = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    # Relación bidireccional con Task
    tasks = db.relationship("Task", back_populates="project")

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True)

# Tabla de asociación para la relación muchos a muchos entre Task y Tag
task_tag = db.Table('task_tag',
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    task_type = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=True)
    importance_level = db.Column(db.Integer)
    urgency_level = db.Column(db.Integer)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Clave foránea y relación bidireccional con Project
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship("Project", back_populates="tasks")

    # Relación muchos a muchos con Tag
    tags = db.relationship('Tag', secondary=task_tag, back_populates='tasks')

# Relación inversa en Tag para que las etiquetas conozcan sus tareas
Tag.tasks = db.relationship('Task', secondary=task_tag, back_populates='tags')
