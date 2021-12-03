"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "blog 1", "body": "this is blog 1"})
        Blog.create({"title": "blog 2", "body": "this is blog 2"})
        Blog.create({"title": "blog 3", "body": "this is blog 3"})
