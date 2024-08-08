from django.db import models


class AdminBots(models.Model):
    name_bot = models.CharField(primary_key=True, max_length=45)
    type_bot = models.CharField(max_length=100, blank=True, null=True)
    own_user = models.BigIntegerField(blank=True, null=True)
    full_name_bot = models.CharField(max_length=100, blank=True, null=True)
    http_api = models.CharField(max_length=100, blank=True, null=True)
    date_pay = models.BigIntegerField(blank=True, null=True)
    sum_pay = models.BigIntegerField(blank=True, null=True)
    pay = models.BigIntegerField(blank=True, null=True)
    log = models.BigIntegerField(blank=True, null=True)
    fbo = models.BigIntegerField(blank=True, null=True)
    fbs = models.BigIntegerField(blank=True, null=True)
    off = models.BigIntegerField(blank=True, null=True)
    docum = models.BigIntegerField(blank=True, null=True)
    pay_clients = models.BigIntegerField(blank=True, null=True)
    pay_fbo = models.BigIntegerField(blank=True, null=True)
    pay_fbs = models.BigIntegerField(blank=True, null=True)
    pay_log = models.BigIntegerField(blank=True, null=True)
    pic_logo = models.CharField(max_length=100, blank=True, null=True)
    support_pic_logo = models.CharField(max_length=100, blank=True, null=True)
    web_logo = models.ImageField(upload_to="photos/", null=True, blank=True)

    def __str__(self):
        return self.name_bot


    class Meta:
        managed = False
        db_table = 'admin_bots'

class SokemUsers(models.Model):
    id_user = models.BigIntegerField(primary_key=True)
    name_user = models.CharField(max_length=45, blank=True, null=True)
    act = models.CharField(max_length=200, blank=True, null=True)
    json_user = models.CharField(max_length=3000, blank=True, null=True)
    type_user = models.CharField(max_length=300, blank=True, null=True)
    mes_id = models.CharField(max_length=1000, blank=True, null=True)
    ref_day = models.BigIntegerField(blank=True, null=True)
    ref_user = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.id_user}: {self.name_user}'

    class Meta:
        managed = False
        db_table = 'sokem_users'

class SupHelps(models.Model):
    id_help = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey('SupUsers', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    text_help = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.id_help}: {self.id_user}'

    class Meta:
        managed = False
        db_table = 'sup_helps'

class SupItems(models.Model):
    id_item = models.BigAutoField(primary_key=True)
    name_item = models.CharField(max_length=20, blank=True, null=True)
    name_bot = models.ForeignKey('AdminBots', models.DO_NOTHING, db_column='name_bot', blank=True, null=True)
    arch = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.id_item}: {self.name_item}'

    class Meta:
        managed = False
        db_table = 'sup_items'

class SupNews(models.Model):
    id_new = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey('SupUsers', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    id_man = models.ForeignKey('SupUsers', models.DO_NOTHING, db_column='id_man', related_name='supnews_id_man_set', blank=True, null=True)
    status_new = models.CharField(max_length=45, blank=True, null=True)
    name_user = models.CharField(max_length=10, blank=True, null=True)
    phone_user = models.CharField(max_length=12, blank=True, null=True)
    link_tg = models.CharField(max_length=100, blank=True, null=True)
    link_wa = models.CharField(max_length=100, blank=True, null=True)
    date_create = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.id_new}: {self.name_user}'

    class Meta:
        managed = False
        db_table = 'sup_news'

class SupReqs(models.Model):
    id_req = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey('SupUsers', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    id_item = models.ForeignKey('SupItems', models.DO_NOTHING, db_column='id_item', blank=True, null=True)
    status_req = models.CharField(max_length=45, blank=True, null=True)
    type_req = models.CharField(max_length=45, blank=True, null=True)
    name_user = models.CharField(max_length=10, blank=True, null=True)
    phone_user = models.CharField(max_length=12, blank=True, null=True)
    where_user = models.CharField(max_length=20, blank=True, null=True)
    when_user = models.CharField(max_length=20, blank=True, null=True)
    name_bot = models.CharField(max_length=45, blank=True, null=True)
    link_user = models.CharField(max_length=100, blank=True, null=True)
    text_q = models.CharField(max_length=1000, blank=True, null=True)
    date_create = models.CharField(max_length=10, blank=True, null=True)
    id_man = models.ForeignKey('SupUsers', models.DO_NOTHING, db_column='id_man', related_name='supreqs_id_man_set', blank=True, null=True)

    def __str__(self):
        return f'{self.id_req}: {self.name_user}'

    class Meta:
        managed = False
        db_table = 'sup_reqs'

class SupUsers(models.Model):
    id_user = models.BigIntegerField(primary_key=True)
    name_user = models.CharField(max_length=10, blank=True, null=True)
    lk = models.CharField(max_length=300, blank=True, null=True)
    act = models.CharField(max_length=100, blank=True, null=True)
    lk_sup = models.CharField(max_length=45, blank=True, null=True)
    full_name_user = models.CharField(max_length=100, blank=True, null=True)
    link_tg = models.CharField(max_length=100, blank=True, null=True)
    phone_user = models.CharField(max_length=12, blank=True, null=True)
    ref_name = models.CharField(max_length=45, blank=True, null=True)
    obr = models.CharField(max_length=100, blank=True, null=True)
    mes_id = models.CharField(max_length=1000, blank=True, null=True)
    mes = models.CharField(max_length=2002, blank=True, null=True)
    chan = models.CharField(max_length=100, blank=True, null=True)
    json_user = models.CharField(max_length=3000, blank=True, null=True)
    month_reg = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f'{self.id_user}: {self.name_user}'

    class Meta:
        managed = False
        db_table = 'sup_users'

