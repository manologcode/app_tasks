from flask import Blueprint, request, jsonify, render_template
from app.models import db, Project
from app.controllers import project_controller

project_bp = Blueprint('projects', __name__, url_prefix='/projects')

# Obtener la lista de todos los proyectos
@project_bp.route('/', methods=['GET'])
def list_projects():
    projects = project_controller.get_all_projects()
    return jsonify([{
        'id': project.id,
        'name': project.name,
        'description': project.description,
        'status': project.status
    } for project in projects]), 200

# Obtener un proyecto específico por ID
@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = project_controller.get_project_by_id(project_id)
    if project:
        return jsonify({
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'status': project.status
        }), 200
    else:
        return jsonify({'error': 'Project not found'}), 404

# Crear un nuevo proyecto
@project_bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Project name is required'}), 400

    try:
        project = project_controller.create_project(data)
        return jsonify({
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'status': project.status
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Actualizar un proyecto existente
@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    project = project_controller.update_project(project_id, data)
    if project:
        return jsonify({
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'status': project.status
        }), 200
    else:
        return jsonify({'error': 'Project not found'}), 404

# Eliminar un proyecto
@project_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    success = project_controller.delete_project(project_id)
    if success:
        return jsonify({'message': 'Project deleted successfully'}), 200
    else:
        return jsonify({'error': 'Project not found'}), 404
