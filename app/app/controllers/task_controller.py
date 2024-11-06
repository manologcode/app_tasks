from datetime import datetime
from app.models import db, Task, Tag

def get_all_tasks():
    """Retorna todas las tareas de la base de datos."""
    return Task.query.all()

def get_task_by_id(task_id):
    """Retorna una tarea específica por su ID."""
    return Task.query.get(task_id)

def create_task(request):
    """Crea una nueva tarea en la base de datos."""
    new_task = Task(
        title=request.form.get('title'),
        description=request.form.get('description'),
        task_type=request.form.get('task_type'),
        status=request.form.get('status', False),  # Por defecto, estado es False
        importance_level=request.form.get('importance_level', 1),
        urgency_level=request.form.get('urgency_level', 1),
        start_time=datetime.fromisoformat(request.form.get('start_time')) if request.form.get('start_time') else None,
        end_time=datetime.fromisoformat(request.form.get('end_time')) if request.form.get('end_time') else None,
        project_id=request.form.get('project_id'),
    )

    # Asociar etiquetas a la tarea
    if 'tags' in request.form:
        tag_names = request.form['tags']
        tags = Tag.query.filter(Tag.name.in_(tag_names)).all()
        new_task.tags.extend(tags)

    db.session.add(new_task)
    db.session.commit()
    return new_task

def update_task(task_id, data):
    """Actualiza una tarea existente."""
    task = Task.query.get(task_id)
    if task:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.task_type = data.get('task_type', task.task_type)
        task.status = data.get('status', task.status)
        task.importance_level = data.get('importance_level', task.importance_level)
        task.urgency_level = data.get('urgency_level', task.urgency_level)
        task.start_time = datetime.fromisoformat(data.get('start_time')) if data.get('start_time') else task.start_time
        task.end_time = datetime.fromisoformat(data.get('end_time')) if data.get('end_time') else task.end_time
        task.project_id = data.get('project_id', task.project_id)

        # Actualizar etiquetas de la tarea
        if 'tags' in data:
            tag_names = data['tags']
            tags = Tag.query.filter(Tag.name.in_(tag_names)).all()
            task.tags = tags  # Reemplaza las etiquetas actuales con las nuevas

        db.session.commit()
        return task
    return None

def delete_task(task_id):
    """Elimina una tarea de la base de datos."""
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    return False
