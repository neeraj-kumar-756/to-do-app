from flask import Flask,redirect,request,url_for,session,flash,Blueprint,render_template, abort

from app import db
from app.models.model import Task, User

task_bp=Blueprint('task',__name__)

@task_bp.route('/')
def view_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    if not user:
        session.clear()
        return redirect(url_for('auth.login'))
    tasks = user.tasks.all()
    return render_template("task.html",tasks=tasks)

@task_bp.route('/add',methods=['POST'])
def add():
    if 'user_id' not in session :
        return redirect(url_for('auth.login'))
    title=request.form.get('title')
    if title:
        new_task=Task(title=title,status='pending', user_id=session['user_id'])
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully",'success')
    return redirect(url_for('task.view_tasks'))

@task_bp.route('/<int:task_id>',methods=['POST'])
def toggle_status(task_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    task=Task.query.get(task_id)
    if not task or task.user_id != session['user_id']:
        abort(403) # Forbidden access

    if task.status=='pending':
        task.status='done'
    elif task.status=='done':
        task.status='pending'
    else:
        task.status='pending'
    db.session.commit()
    return redirect(url_for('task.view_tasks'))

@task_bp.route('/clear_all',methods=['POST'])
def clear_all():
    if 'user_id' in session:
        Task.query.filter_by(user_id=session['user_id']).delete()
        db.session.commit()
        flash('deleted all task entrys','danger')
        return redirect(url_for('task.view_tasks'))
    else:
        return redirect(url_for('auth.login'))
   
