# -*- coding: euckr -*-
# -*- coding: utf-8 -*-
# ���̽� ���� 2�� ���� 3 ������ ���ڿ��� ó���ϴ� ����� �ٸ�. ������� ���� 3 ����� ���ڿ� ó���� �������� ���ϰ�, ���� 2���� ȣȯ���� �����ϱ� ���ؼ� �Ʒ� 2���� ��ɹ��� �ʿ�
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# reverse() �Լ��� ����ϱ� ���� ����Ʈ reverse() �Լ��� URL ������ ������ִ� ����� ���� �Լ���.
from django.core.urlresolvers import reverse
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
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()