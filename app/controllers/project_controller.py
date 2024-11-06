from app.models import db, Project

def get_all_projects():
    return Project.query.all()

def get_project_by_id(project_id):
    return Project.query.get(project_id)

def create_project(data):
    new_project = Project(
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status', True)  # True por defecto
    )
    db.session.add(new_project)
    db.session.commit()
    return new_project

def update_project(project_id, data):
    project = Project.query.get(project_id)
    if project:
        project.name = data.get('name', project.name)
        project.description = data.get('description', project.description)
        project.status = data.get('status', project.status)
        db.session.commit()
        return project
    return None

def delete_project(project_id):
    project = Project.query.get(project_id)
    if project:
        db.session.delete(project)
        db.session.commit()
        return True
    return False
