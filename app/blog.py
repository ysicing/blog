#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: blog/blog.py 
@time: 2017/9/10 22:46
"""

from flask_frozen import Freezer
from flask_flatpages import FlatPages
from flask import current_app as app


flatpages = FlatPages(app)
freezer = Freezer(app)


class Post(object):
    def __init__(self, ext, post_dir):
        self.ext = ext
        self.post_dir = post_dir

    def get_posts_list(self):
        try:
            posts = [post for post in flatpages if post.path.startwith(self.post_dir)]
        except:
            posts = [post for post in flatpages if post.path]
        try:
            posts.sort(key=lambda item: item['date'], reverse=True)
        except:
            posts = sorted(posts, reverse=True, key=lambda post: post['date'])
        return posts

    def recent_post(self):
        posts = self.get_posts_list()
        if len(posts) >= 10:
            recent_post = posts[:10]
        else:
            recent_post = posts
        return recent_post

    def get_tags(self):
        """

        :return: all tag info
        """
        dkey = {}
        for post in self.get_posts_list():
            for i in post.__getitem__('tags').strip().split():
                dkey.setdefault(i.lower(), 0)
                dkey[i.lower()] += 1
        return dkey

    def get_tag(self, tag):
        """
        :param tag:
        :return: tag相关的文章列表
        """

        tag = tag.lower()
        tag_info = []
        for post in self.get_posts_list():
            for itag in post.__getitem__('tags').strip().split():
                if itag == tag:
                    tag_info.append(post.path)
        print(tag_info)
        return {tag: tag_info}

    def get_post_info(self, postname):
        path = '{}/{}{}'.format(self.post_dir, postname, self.ext)
        print(path)
        post = flatpages.get_or_404(path)
        print(post)
        postindex = self.get_posts_list().index(post)
        postpre = None if postindex == 0 else self.get_posts_list()[postindex - 1]
        postnex = None if postindex == len(self.get_posts_list()) -1 else self.get_posts_list()[postindex + 1]
        post_info = {'post': post, 'postpre': postpre, 'postnex': postnex}
        return post_info


