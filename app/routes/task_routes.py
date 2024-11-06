from flask import Blueprint, request, jsonify
from app.controllers import task_controller

task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

# Obtener la lista de todas las tareas
@task_bp.route('/', methods=['GET'])
def list_tasks():
    tasks = task_controller.get_all_tasks()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'task_type': task.task_type,
        'status': task.status,
        'importance_level': task.importance_level,
        'urgency_level': task.urgency_level,
        'start_time': task.start_time,
        'end_time': task.end_time,
        'project_id': task.project_id,
        'created_at': task.created_at,
        'tags': [tag.name for tag in task.tags]
    } for task in tasks]), 200

# Obtener una tarea específica por ID
@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_controller.get_task_by_id(task_id)
    if task:
        return jsonify({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'task_type': task.task_type,
            'status': task.status,
            'importance_level': task.importance_level,
            'urgency_level': task.urgency_level,
            'start_time': task.start_time,
            'end_time': task.end_time,
            'project_id': task.project_id,
            'created_at': task.created_at,
            'tags': [tag.name for tag in task.tags]
        }), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

# Crear una nueva tarea
@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Task title is required'}), 400

    try:
        task = task_controller.create_task(data)
        return jsonify({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'task_type': task.task_type,
            'status': task.status,
            'importance_level': task.importance_level,
            'urgency_level': task.urgency_level,
            'start_time': task.start_time,
            'end_time': task.end_time,
            'project_id': task.project_id,
            'created_at': task.created_at,
            'tags': [tag.name for tag in task.tags]
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Actualizar una tarea existente
@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    task = task_controller.update_task(task_id, data)
    if task:
        return jsonify({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'task_type': task.task_type,
            'status': task.status,
            'importance_level': task.importance_level,
            'urgency_level': task.urgency_level,
            'start_time': task.start_time,
            'end_time': task.end_time,
            'project_id': task.project_id,
            'created_at': task.created_at,
            'tags': [tag.name for tag in task.tags]
        }), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

# Eliminar una tarea
@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    success = task_controller.delete_task(task_id)
    if success:
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404
