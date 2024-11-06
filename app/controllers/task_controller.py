from datetime import datetime
from app.models import db, Task, Tag

def get_all_tasks():
    """Retorna todas las tareas de la base de datos."""
    return Task.query.all()

def get_task_by_id(task_id):
    """Retorna una tarea específica por su ID."""
    return Task.query.get(task_id)

def create_task(data):
    """Crea una nueva tarea en la base de datos."""
    new_task = Task(
        title=data.get('title'),
        description=data.get('description'),
        task_type=data.get('task_type'),
        status=data.get('status', False),  # Por defecto, estado es False
        importance_level=data.get('importance_level', 1),
        urgency_level=data.get('urgency_level', 1),
        start_time=datetime.fromisoformat(data.get('start_time')) if data.get('start_time') else None,
        end_time=datetime.fromisoformat(data.get('end_time')) if data.get('end_time') else None,
        project_id=data.get('project_id'),
        created_at=datetime.utcnow()
    )

    # Asociar etiquetas a la tarea
    if 'tags' in data:
        tag_names = data['tags']
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
