from flask import  Blueprint, render_template, redirect, url_for, request, current_app
from app.models import db, Project
from app.controllers import project_controller

project_bp = Blueprint('projects', __name__, url_prefix='/projects')

# Obtener la lista de todos los proyectos# Obtener un proyecto específico por ID
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

@project_bp.route('/new', methods=['GET'])
def new_project():
    return render_template("/projects/form_modal.html") 

@project_bp.route('/create', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        current_app.logger.info('Creando nueva projects')
        project_controller.create_project(request)
        # flash('Task created successfully!', 'success')
        return redirect(url_for('projects.list_projects'))
    return render_template('projects/form.html', project=None)
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
