from flask import  Blueprint, render_template, redirect, url_for, request, flash, current_app
from app.controllers import tag_controller

tag_bp = Blueprint('tags', __name__, url_prefix='/tags')

@tag_bp.route('/')
def list_tags():
    tags = tag_controller.get_all_tags()
    return render_template('tags/list.html', tags=tags)

@tag_bp.route('/<int:tag_id>')
def detail_tag(tag_id):
    tag = tag_controller.get_tag_by_id(tag_id)
    return render_template('tags/detail.html', tag=tag)

@tag_bp.route('/new', methods=['GET'])
def new_tag():
    current_app.logger.info('Nueva tag')
    return render_template("/tags/modal_form.html")

@tag_bp.route('/create', methods=['GET', 'POST'])
def create_tag():
    if request.method == 'POST':
        current_app.logger.info('Creando nueva tasks')
        task = tag_controller.create_tag(request)
        # flash('tag created successfully!', 'success')
        return redirect(url_for('tasks.list_tasks'))
    return render_template('tags/form.html', tag=None)

@tag_bp.route('/<int:tag_id>/edit', methods=['GET', 'POST'])
def edit_tag(tag_id):
    tag = tag_controller.get_tag_by_id(tag_id)
    if request.method == 'POST':
        # Lógica para actualizar la tarea
        flash('tag updated successfully!', 'success')
        return redirect(url_for('tags.list_tags'))
    return render_template('tags/form.html', tag=tag)