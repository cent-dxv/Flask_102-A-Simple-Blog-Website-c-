from flask import Blueprint, render_template, redirect, url_for,request,flash
from flask_login import login_required ,current_user
from .model import Post, User ,Comment ,Like
from . import db

view = Blueprint("view", __name__)
@view.route("/")
@view.route("/home")
@login_required
def home():
    post = Post.query.all()
    print(post)
    return render_template('home.html', user = current_user , posts =post)

@view.route("/post/" , methods =[ 'POST' , 'GET'])
@login_required
def post():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash('Post can not be empty', category = 'erorr')
        else:
            new_post = Post(post_text=text , author =current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post successfully created ' , category = 'success')
            redirect('/')


    return render_template('create_post.html', user = current_user)

@view.route("/delete-post/<id>" , methods =[ 'GET' ])
def delete_post(id):
    deleted_post = Post.query.filter_by(id=id).first()

    if not deleted_post:
        flash("Post dosen't  exist" , category='erorr')
    elif current_user.id != deleted_post.user.id:
        flash("an Authorized access denied", category='erorr')
    else:
        db.session.delete(deleted_post)
        db.session.commit()
        flash("Post removed", category='success')
    return redirect('/')

@view.route("/<name>")
@view.route("/posts/<name>")

@login_required
def post_by_user(name):
    user = User.query.filter_by(username=name).first()

    if not user:
        flash("User does not exist", category='erorr')
        return redirect('/')
    
    post = Post.query.filter_by(author=user.id).all()
    return render_template('home.html', user = current_user , posts =post)

@view.route("/create-comment/<post_id>" , methods = ['POST'])
@login_required
def create_comment(post_id):
    post_id = Post.query.filter_by(id=post_id).first()
    text = request.form.get('text')
    if not text:
        flash("Commnet should not be Empty", category='erorr')
    
    elif not post_id:
        flash("Post does not exist", category='erorr')
    else:
        flash("successfully commented on post", category='success')
        new_commnet = Comment(text =text , author = current_user.id , post_id = post_id.id) 
        db.session.add(new_commnet)
        db.session.commit()
        
    return redirect("/")




@view.route("/delete-comment/<commnet_id>" , methods = ['GET'])
@login_required
def delet_comment(commnet_id):
    commnet_id = Comment.query.filter_by(id=commnet_id).first()
    
    if not commnet_id:
        flash("Comment does not exist", category='erorr')
    elif  commnet_id.author != current_user.id:
        flash("Your not Allowed to delete this", category='erorr')

    else:
        flash("successfully commented on post", category='success')
   
        db.session.delete(commnet_id)
        db.session.commit()
        
    return redirect("/")


@view.route("/like_posts/<post_id>" , methods = ['GET'])
@login_required
def like_posts(post_id):
    post_ids = Post.query.filter_by(id=post_id).first()
    likes = Like.query.filter_by(post_id=post_ids.id).first()
    print()

    if not post_ids:
        flash("Post does not exist", category='erorr')
    elif likes:
        flash("You have been liked", category='success')
        
        db.session.delete(likes)
        db.session.commit()
    else:
        flash("successfully Like on post", category='success')

        new_like = Like( author = current_user.id , post_id = post_ids.id) 
        db.session.add(new_like)
        db.session.commit()
        
    return redirect("/")