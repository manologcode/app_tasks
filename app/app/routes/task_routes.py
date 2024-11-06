from flask import  Blueprint, render_template, redirect, url_for, request, flash,current_app
from app.controllers import task_controller
from app.controllers import project_controller
from app.controllers import tag_controller

task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@task_bp.route('/')
def list_tasks():
    tags = tag_controller.get_all_tags()
    tasks = task_controller.get_all_tasks()
    projects = project_controller.get_all_active_projects()
    return render_template('index.html', tasks=tasks, projects=projects,tags=tags)

@task_bp.route('/<int:task_id>')
def detail_task(task_id):
    task = task_controller.get_task_by_id(task_id)
    return render_template('tasks/detail.html', task=task)

@task_bp.route('/new', methods=['GET'])
def new_task():
    return render_template("/tasks/form_modal.html") 

@task_bp.route('/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        current_app.logger.info('Creando nueva tasks')
        task = task_controller.create_task(request)
        # flash('Task created successfully!', 'success')
        return redirect(url_for('tasks.list_tasks'))
    return render_template('tasks/form.html', task=None)

@task_bp.route('/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = task_controller.get_task_by_id(task_id)
    if request.method == 'POST':
        # Lógica para actualizar la tarea
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks.list_tasks'))
    return render_template('tasks/form.html', task=task)