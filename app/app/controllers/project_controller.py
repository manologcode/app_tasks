from app.models import db, Project

def get_all_projects():
    return Project.query.all()

def get_all_active_projects():
    return Project.query.filter(Project.status == True).all()

def get_project_by_id(project_id):
    return Project.query.get(project_id)

def create_project(request):
    new_project = Project(
        name=request.form.get('name'),
        description=request.form.get('description'),
        status=request.form.get('status', True)  # True por defecto
    )
    db.session.add(new_project)
    db.session.commit()
    return new_project

def update_project(project_id, request):
    project = Project.query.get(project_id)
    if project:
        project.name = request.form.get('name', project.name)
        project.description = request.form.get('description', project.description)
        project.status = request.form.get('status', project.status)
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
