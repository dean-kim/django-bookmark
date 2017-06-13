# -*- coding: euckr -*-
# -*- coding: utf-8 -*-
# ���̽� ���� 2�� ���� 3 ������ ���ڿ��� ó���ϴ� ����� �ٸ�. ������� ���� 3 ����� ���ڿ� ó���� �������� ���ϰ�, ���� 2���� ȣȯ���� �����ϱ� ���ؼ� �Ʒ� 2���� ��ɹ��� �ʿ�
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# reverse() �Լ��� ����ϱ� ���� ����Ʈ reverse() �Լ��� URL ������ ������ִ� ����� ���� �Լ���.
from django.core.urlresolvers import reverse

from tagging.fields import TagField

from django.contrib.auth.models import User

# slug �ʵ带 �ڵ����� ä��� ���� slugify() �Լ��� ����Ʈ.
# slugify �Լ��� ���� �ܾ ���ĺ� �ҹ���, ����, ����, ���������θ� ������ �ܾ�� ������ִ� �Լ�.
# ��ȯ �� : slugify("Django is a Python Web Framework")�� "django-is-a-python-web-framework"�� ��ȯ.
from django.utils.text import slugify
# Create your models here.

@python_2_unicode_compatible

class Post(models.Model):
    # title �÷��� CharField �̹Ƿ� �� �ٷ� �Է�.
    # �÷��� ���� ���̺��� 'TITLE'�̰� �ִ� ���̴� 50���ڷ� ����
    # ���̺��� �� ȭ�鿡 ��Ÿ���� ������ Admin ���������� Ȯ�� ������.
    title = models.CharField('Title', max_length=50)
    # slug �÷��� ������ ��Ī.
    # SlugField�� unique �ɼ��� �߰��� Ư�� ����Ʈ�� �˻� �� �⺻ Ű ��ſ� ����.
    # allow_unicode �ɼ��� �߰��ϸ� �ѱ� ó���� ������.
    # help_text�� �ش� �÷��� �������ִ� ������ �� ȭ�鿡 ��Ÿ��. Admin ���������� Ȯ�� ����.


    """
    - �����׶�?
    �����״� �������� ����Ʈ�� �����ϴ� �ٽ� �ܾ��� ����. ���� �Ź��̳� ���� ��� ������ �� ��, �߿��� �ǹ̸� �����ϴ� �ܾ�� �̿��� ������
    �ۼ��ϴ� ���. �� ���� �о߿����� �������� ���� �ּҷ� ���Ǿ� �������� �ּҰ� � ���������� ���� ������ �� �ֵ��� ��.
    ���� �����״� �������� ����Ʈ�� ���񿡼� ����, ��ġ��, ��ǥ, ��ħǥ ���� ���� ����� ������(-)���� ��ü�ؼ� �����, URL�� ����.
    �����׸� URL�� ��������ν� �˻� �������� �� ���� �������� ã���ְ� �˻� ������ ��Ȯ���� ������.
    - SlugField �ʵ� Ÿ��
    �����״� ���� ������ �ܾ���� ���������� ������ �����ϸ�, URL���� pk ������� ���Ǵ� ��찡 ����. pk�� ����ϸ� ���ڷθ� �Ǿ� �־� 
    �� ������ �����ϱ� ������� �����׸� ����ϸ� ������ �ܾ���̶� �����ϱ� ���� ������.
    SlugField �ʵ��� ����Ʈ ���̴� 50�̸�, �ش� �ʵ忡�� �ε����� ����Ʈ�� ������.
    """

    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    # description Į���� ��ĭ(blank)�� �����մϴ�.
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    # content �÷��� TextField�� ��������Ƿ� ���� �� �Է��� �����մϴ�.
    content = models.TextField('CONTENT')
    # create_date �÷��� ��¥�� �ð��� �Է��ϴ� DateTimeField�̸�, auto_now_add �Ӽ��� ��ü�� ������ ���� �ð��� �ڵ����� ����ϰ� �մϴ�.
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    # modify_date �÷��� ��¥�� �ð��� �Է��ϴ� DateTimeField�̸�, auto_now �Ӽ��� ��ü�� �����ͺ��̽��� ����� ���� �ð��� �ڵ����� ����ϰ� �մϴ�.
    # ��, ��ü�� ����� ���� �ð��� ��ϵǴ� ����.
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    tag = TagField()
    owner = models.ForeignKey(User, null=True)

    # �ʵ� �Ӽ� �ܿ� �ʿ��� �Ķ���Ͱ� ������, Meta ���� Ŭ������ �����մϴ�.
    class Meta:
        # ���̺��� ��Ī�� �ܼ��� ������ ���� �� �ִµ�, �ܼ� ��Ī�� 'post'�� ��.
        verbose_name = 'post'
        # ���̺��� ���� ��Ī�� 'posts'�� ��.
        verbose_name_plural = 'posts'
        # �����ͺ��̽��� ����Ǵ� ���̺� �̸��� 'my_post'�� ����. �� �׸��� �����ϸ� ����Ʈ�� '�۸�_��Ŭ�������� ���̺� �̸����� �����.
        # �̸��� �������� �ʾҴٸ� 'blog_post'�� �Ǿ��� ����.
        db_table = 'my_post'
        # �� ��ü ���� �� 'modyfy_date' �÷��� �������� ������������ ����.
        ordering = ('-modify_date',)

    # ��ü�� ���ڿ��� ��ü.title�� ǥ�õǵ��� ��.
    def __str__(self):
        return self.title

    # get_absolute_url() �޼ҵ�� �� �޼ҵ尡 ���ǵ� ��ü�� ��Ī�ϴ� URL�� ��ȯ.
    # �޼ҵ� �������� ����� ���� �Լ��� reverse()�� ȣ����.
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # get_previous_post() �޼ҵ�� modify_date �÷��� �������� ���� ����Ʈ�� ��ȯ
    # �޼ҵ� �������� ����� ���� �Լ��� get_previous_by_modify_date()�� ȣ����
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # get_next_post() �޼ҵ�� modify_date �÷��� �������� ���� ����Ʈ�� ��ȯ
    # �޼ҵ� �������� ����� ���� �Լ��� get_next_by_modify_date()�� ȣ����
    def get_next_post(self):
        return self.get_next_by_modify_date()

    # save() �޼ҵ带 ������, save �޼ҵ�� �� ��ü�� ������ �����ͺ��̽��� �����ϴ� �޼ҵ�.
    # �����ͺ��̽� ���̺� ���� �� self.id�� Ȯ���� False�� ���, �� ó������ �����ϴ� ��쿡�� slug �ʵ带 title �ʵ��� �ܾ�� ��ȯ�� �ڵ����� ä��.
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)

        # �θ� Ŭ������ save() �޼ҵ带 ȣ���� ��ü�� ������ ���̺� �ݿ��ϴ� save �޼ҵ��� ���� ����� ������.
        super(Post, self).save(*args, **kwargs)