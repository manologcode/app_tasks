from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Boolean, default=True)

class Tag(db.Model):
    __tablename__ = 'tags'
    name = db.Column(db.String(50), primary_key=True)
    active = db.Column(db.Boolean, default=True)

task_tag = db.Table('task_tag',
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key=True),
    db.Column('tag_name', db.String(50), db.ForeignKey('tags.name'), primary_key=True)
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
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    tags = db.relationship('Tag', secondary=task_tag, backref='tasks')
