# -*- coding: utf-8 -*-
"""Post views."""
import json

from flask import Blueprint, jsonify, request, flash, redirect, url_for, render_template

from RSSFeed.extensions import db
from RSSFeed.post.form import CreatePostForm
from RSSFeed.post.model import Post
from RSSFeed.post.schemas import ListPostSchema, DetailPostSchema
from RSSFeed.utils import flash_errors

blueprint = Blueprint("post", __name__, url_prefix="/posts", static_folder="../static")


@blueprint.route("/create", methods=["GET", "POST"])
def create_post():
    """Create a new post."""
    form = CreatePostForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            new_post = Post.create(
                name=form.name.data,
                short_description=form.short_description.data,
                content=form.content.data,
            )
            db.session.add(new_post)
            db.session.commit()
            flash("Post created successfully!", "success")
            return redirect(url_for("post.get_posts"))

    else:
        flash_errors(form)
    return render_template("post/create_post.html", form=form)


@blueprint.route('/<int:post_id>', methods=['GET'])
def get_detail_post(post_id: int):
    if post := Post.query.get(post_id):
        return render_template("post/get_detail_post.html", post=post)
    return jsonify({
        "error": "Post not found",
        "message": f"No post with ID {post_id} exists in the database."
    }), 404


@blueprint.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return render_template("post/get_posts.html", posts=posts)
