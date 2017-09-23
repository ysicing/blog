#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: blog/post.py 
@time: 2017/9/23 10:53
"""

from flask import Blueprint, render_template

from app.blog import Post

sp = Post('.md', 'posts')

post = Blueprint('post', __name__)


@post.route('/posts/')
def list_all():
    return render_template('posts.html')


@post.route('/post/<name>')
def show_post(name):
    print(sp.get_post_info(name))

    return render_template('post.html',post='111')