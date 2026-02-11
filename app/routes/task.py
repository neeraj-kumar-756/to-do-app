from flask import Flask,redirect,request,url_for,session,flash,Blueprint,render_template

from app import db
from db.models.model import Task

task_bp=Blueprint('Task',__name__)

@task_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    tasks = Task.query.all()
    return render_template("task.html",tasks=tasks)

@task_bp.route('/add',method=['POST'])
def add():
    if 'user' not in session :
        return redirect(url_for('auth.login'))
    title=request.form.get('title')
    if title:
        new_task=Task(title=title,status='pending')
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully",'success')
    return redirect(url_for('task.view_tasks'))
