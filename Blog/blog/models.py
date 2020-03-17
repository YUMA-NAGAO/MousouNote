from django.db import models
from django.utils import timezone


class Category(models.Model):
    # ブログのカテゴリー
    name = models.CharField('カテゴリ名', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    # ブログの記事
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # ブログのコメント
    name = models.CharField('お名前', max_length=30, default='名無し')
    text = models.TextField('本文')
    post = models.ForeignKey(Post, verbose_name='紐付く記事', on_delete=models.PROTECT)
    # コメントがすべてさあ駆除出来ないと、記事の削除が出来ない
    created_at = models.DateTimeField('作成気', default=timezone.now)

    def __str__(self):
        return self.text[:10]
