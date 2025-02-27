# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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

    class Meta:
        managed = False
        db_table = 'admin_bots'

class Buysell(models.Model):
    id_sd = models.AutoField(primary_key=True)
    deposit = models.FloatField(blank=True, null=True)
    pos = models.CharField(max_length=45, blank=True, null=True)
    start_deposit = models.FloatField(blank=True, null=True)
    stop_lose = models.FloatField(blank=True, null=True)
    out_line = models.FloatField(blank=True, null=True)
    price_in = models.FloatField(blank=True, null=True)
    take_1 = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    stop_ind = models.FloatField(blank=True, null=True)
    month = models.FloatField(blank=True, null=True)
    take_2 = models.FloatField(blank=True, null=True)
    take_3 = models.FloatField(blank=True, null=True)
    pnl = models.FloatField(blank=True, null=True)
    take_deposit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buysell'

class CarsFf(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    plan_start_date = models.CharField(max_length=45, blank=True, null=True)
    plan_end_date = models.CharField(max_length=45, blank=True, null=True)
    fact_start_date = models.CharField(max_length=45, blank=True, null=True)
    fact_end_date = models.CharField(max_length=45, blank=True, null=True)
    drive = models.CharField(max_length=45, blank=True, null=True)
    gate = models.CharField(max_length=45, blank=True, null=True)
    done = models.BigIntegerField(blank=True, null=True)
    ff_city = models.BigIntegerField(blank=True, null=True)
    flag_arch = models.BigIntegerField(blank=True, null=True)
    count_pal = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars_ff'


class Clients(models.Model):
    id_user = models.CharField(primary_key=True, max_length=45)
    type_user = models.CharField(max_length=45, blank=True, null=True)
    name_user = models.CharField(max_length=45, blank=True, null=True)
    phone_user = models.CharField(max_length=45, blank=True, null=True)
    ul_user = models.CharField(max_length=45, blank=True, null=True)
    actions = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    doc_fbo = models.CharField(max_length=45, blank=True, null=True)
    doc_fbs = models.CharField(max_length=45, blank=True, null=True)
    word_1 = models.CharField(max_length=300, blank=True, null=True)
    word_2 = models.CharField(max_length=45, blank=True, null=True)
    word_3 = models.CharField(max_length=45, blank=True, null=True)
    word_4 = models.CharField(max_length=45, blank=True, null=True)
    word_5 = models.CharField(max_length=45, blank=True, null=True)
    word_6 = models.CharField(max_length=45, blank=True, null=True)
    word_7 = models.CharField(max_length=45, blank=True, null=True)
    word_8 = models.CharField(max_length=45, blank=True, null=True)
    word_9 = models.CharField(max_length=45, blank=True, null=True)
    word_10 = models.CharField(max_length=45, blank=True, null=True)
    word_11 = models.CharField(max_length=45, blank=True, null=True)
    word_12 = models.CharField(max_length=300, blank=True, null=True)
    word_13 = models.CharField(max_length=45, blank=True, null=True)
    word_14 = models.CharField(max_length=45, blank=True, null=True)
    word_15 = models.CharField(max_length=45, blank=True, null=True)
    offero = models.CharField(max_length=45, blank=True, null=True)
    id_lk = models.CharField(max_length=45, blank=True, null=True)
    obr = models.CharField(max_length=45, blank=True, null=True)
    iknow = models.BigIntegerField(blank=True, null=True)
    mon_1 = models.CharField(max_length=45, blank=True, null=True)
    mon_2 = models.CharField(max_length=45, blank=True, null=True)
    mon_3 = models.CharField(max_length=45, blank=True, null=True)
    mon_4 = models.CharField(max_length=45, blank=True, null=True)
    mon_5 = models.CharField(max_length=45, blank=True, null=True)
    mon_6 = models.CharField(max_length=45, blank=True, null=True)
    mon_7 = models.CharField(max_length=45, blank=True, null=True)
    mon_8 = models.CharField(max_length=45, blank=True, null=True)
    mon_9 = models.CharField(max_length=45, blank=True, null=True)
    mon_10 = models.CharField(max_length=45, blank=True, null=True)
    mon_11 = models.CharField(max_length=45, blank=True, null=True)
    mon_12 = models.CharField(max_length=45, blank=True, null=True)
    act = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class ClientsFf(models.Model):
    id_user = models.BigIntegerField(primary_key=True)
    act = models.CharField(max_length=1500, blank=True, null=True)
    type_user = models.CharField(max_length=45, blank=True, null=True)
    name_user = models.CharField(max_length=45, blank=True, null=True)
    phone_user = models.CharField(max_length=45, blank=True, null=True)
    ul_user = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    doc_fbo = models.CharField(max_length=45, blank=True, null=True)
    doc_fbs = models.CharField(max_length=45, blank=True, null=True)
    offero = models.CharField(max_length=45, blank=True, null=True)
    id_lk = models.CharField(max_length=45, blank=True, null=True)
    obr = models.CharField(max_length=45, blank=True, null=True)
    iknow = models.BigIntegerField(blank=True, null=True)
    mon_1 = models.CharField(max_length=45, blank=True, null=True)
    mon_2 = models.CharField(max_length=45, blank=True, null=True)
    mon_3 = models.CharField(max_length=45, blank=True, null=True)
    mon_4 = models.CharField(max_length=45, blank=True, null=True)
    mon_5 = models.CharField(max_length=45, blank=True, null=True)
    mon_6 = models.CharField(max_length=45, blank=True, null=True)
    mon_7 = models.CharField(max_length=45, blank=True, null=True)
    mon_8 = models.CharField(max_length=45, blank=True, null=True)
    mon_9 = models.CharField(max_length=45, blank=True, null=True)
    mon_10 = models.CharField(max_length=45, blank=True, null=True)
    mon_11 = models.CharField(max_length=45, blank=True, null=True)
    mon_12 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients_ff'


class DianaRequest(models.Model):
    id_request = models.AutoField(primary_key=True)
    id_client = models.BigIntegerField(blank=True, null=True)
    status_request = models.CharField(max_length=45, blank=True, null=True)
    type_request = models.CharField(max_length=45, blank=True, null=True)
    type_online = models.CharField(max_length=45, blank=True, null=True)
    q1 = models.CharField(max_length=2000, blank=True, null=True)
    q2 = models.CharField(max_length=2000, blank=True, null=True)
    q3 = models.CharField(max_length=2000, blank=True, null=True)
    q4 = models.CharField(max_length=2000, blank=True, null=True)
    q5 = models.CharField(max_length=2000, blank=True, null=True)
    q6 = models.CharField(max_length=4000, blank=True, null=True)
    fio = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diana_request'


class DianaRequestNone(models.Model):
    id_user = models.BigIntegerField(primary_key=True)
    type_request = models.CharField(max_length=45, blank=True, null=True)
    type_online = models.CharField(max_length=45, blank=True, null=True)
    q1 = models.CharField(max_length=2000, blank=True, null=True)
    q2 = models.CharField(max_length=2000, blank=True, null=True)
    q3 = models.CharField(max_length=2000, blank=True, null=True)
    q4 = models.CharField(max_length=2000, blank=True, null=True)
    q5 = models.CharField(max_length=2000, blank=True, null=True)
    q6 = models.CharField(max_length=4000, blank=True, null=True)
    fio = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diana_request_none'


class DianaUsers(models.Model):
    id_user = models.AutoField(primary_key=True)
    type_user = models.CharField(max_length=45, blank=True, null=True)
    name_user = models.CharField(max_length=45, blank=True, null=True)
    phone_client = models.CharField(max_length=45, blank=True, null=True)
    act = models.CharField(max_length=45, blank=True, null=True)
    obr = models.CharField(max_length=45, blank=True, null=True)
    ph = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diana_users'


class EndFf(models.Model):
    date_work = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'end_ff'


class EndSp(models.Model):
    date_work = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'end_sp'


class FboFf(models.Model):
    fbo_id = models.BigAutoField(primary_key=True)
    done = models.BigIntegerField(blank=True, null=True)
    create_date = models.CharField(max_length=45, blank=True, null=True)
    creater = models.CharField(max_length=45, blank=True, null=True)
    name_ul = models.CharField(max_length=45, blank=True, null=True)
    phone_ul = models.CharField(max_length=45, blank=True, null=True)
    status_fbo = models.BigIntegerField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    count_items = models.BigIntegerField(blank=True, null=True)
    pay_done = models.BigIntegerField(blank=True, null=True)
    dost = models.CharField(max_length=45, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    type_fbo = models.BigIntegerField(blank=True, null=True)
    mark = models.CharField(max_length=45, blank=True, null=True)
    pack = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)
    mark_box = models.CharField(max_length=45, blank=True, null=True)
    done_box = models.BigIntegerField(blank=True, null=True)
    fbo_0_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_0_user = models.CharField(max_length=45, blank=True, null=True)
    fbo_0_date = models.CharField(max_length=45, blank=True, null=True)
    fbo_1_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_1_user = models.CharField(max_length=45, blank=True, null=True)
    fbo_1_date = models.CharField(max_length=45, blank=True, null=True)
    fbo_2_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_2_user = models.CharField(max_length=45, blank=True, null=True)
    fbo_2_date = models.CharField(max_length=45, blank=True, null=True)
    fbo_3_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_3_user = models.CharField(max_length=45, blank=True, null=True)
    fbo_3_date = models.CharField(max_length=45, blank=True, null=True)
    car_id = models.BigIntegerField(blank=True, null=True)
    zabor = models.CharField(max_length=45, blank=True, null=True)
    fbo_18_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_18_user = models.CharField(max_length=45, blank=True, null=True)
    fbo_18_1_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_18_date = models.CharField(max_length=45, blank=True, null=True)
    fbo_19_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_19_user = models.CharField(max_length=45, blank=True, null=True)
    fbo_19_date = models.CharField(max_length=45, blank=True, null=True)
    flag_arch = models.BigIntegerField(blank=True, null=True)
    fbo_80_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_80_user = models.CharField(max_length=45, blank=True, null=True)
    fbo_80_date = models.CharField(max_length=45, blank=True, null=True)
    fbo_81_text = models.CharField(max_length=45, blank=True, null=True)
    fbo_81_user = models.CharField(max_length=45, blank=True, null=True)
    fbo_81_date = models.CharField(max_length=45, blank=True, null=True)
    own_fbo = models.CharField(max_length=45, db_collation='armscii8_general_ci', blank=True, null=True)
    weight = models.BigIntegerField(blank=True, null=True)
    check_id = models.CharField(max_length=200, blank=True, null=True)
    doc_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fbo_ff'


class ItemsFf(models.Model):
    id_item = models.BigAutoField(primary_key=True)
    id_ul = models.BigIntegerField(blank=True, null=True)
    photo = models.CharField(max_length=200, blank=True, null=True)
    name_item = models.CharField(max_length=45, blank=True, null=True)
    art_wb = models.CharField(max_length=45, blank=True, null=True)
    art_ozon = models.CharField(max_length=45, blank=True, null=True)
    color = models.CharField(max_length=45, blank=True, null=True)
    size_item = models.CharField(max_length=45, blank=True, null=True)
    pack = models.CharField(max_length=45, blank=True, null=True)
    gift = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)
    box = models.CharField(max_length=45, blank=True, null=True)
    flag_arch = models.BigIntegerField(blank=True, null=True)
    barcode = models.BigIntegerField(blank=True, null=True)
    items_count = models.BigIntegerField(blank=True, null=True)
    art_ya = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_ff'


class NewFboFf(models.Model):
    id_zakaz = models.BigAutoField(primary_key=True)
    own_zakaz = models.CharField(max_length=45, blank=True, null=True)
    status_zakaz = models.BigIntegerField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    count_items = models.BigIntegerField(blank=True, null=True)
    id_fbo = models.BigIntegerField(blank=True, null=True)
    nons = models.CharField(max_length=90, blank=True, null=True)
    zabor = models.CharField(max_length=1555, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_fbo_ff'


class NewFbsFf(models.Model):
    id_zakaz = models.BigAutoField(primary_key=True)
    own_zakaz = models.CharField(max_length=45, blank=True, null=True)
    status_zakaz = models.CharField(max_length=45, blank=True, null=True)
    date_zakaz = models.CharField(max_length=45, blank=True, null=True)
    count_items = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_fbs_ff'


class Sd(models.Model):
    id_sd = models.AutoField(primary_key=True)
    pos = models.CharField(max_length=45, blank=True, null=True)
    status_sd = models.CharField(max_length=45, blank=True, null=True)
    start_deposit = models.FloatField(blank=True, null=True)
    end_deposit = models.FloatField(blank=True, null=True)
    take_profit = models.FloatField(blank=True, null=True)
    stop_lose = models.FloatField(blank=True, null=True)
    take_ind = models.FloatField(blank=True, null=True)
    stop_ind = models.FloatField(blank=True, null=True)
    price_in = models.FloatField(blank=True, null=True)
    price_out = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    pnl = models.FloatField(blank=True, null=True)
    start_ind = models.FloatField(blank=True, null=True)
    end_ind = models.FloatField(blank=True, null=True)
    start_date = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    pnl_money = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    vol_2 = models.FloatField(blank=True, null=True)
    strat = models.CharField(max_length=45, blank=True, null=True)
    take_1 = models.FloatField(blank=True, null=True)
    take_2 = models.FloatField(blank=True, null=True)
    take_3 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sd'


class Sd2(models.Model):
    id_sd = models.AutoField(primary_key=True)
    pos = models.CharField(max_length=45, blank=True, null=True)
    status_sd = models.CharField(max_length=45, blank=True, null=True)
    start_deposit = models.FloatField(blank=True, null=True)
    end_deposit = models.FloatField(blank=True, null=True)
    take_profit = models.FloatField(blank=True, null=True)
    stop_lose = models.FloatField(blank=True, null=True)
    take_ind = models.FloatField(blank=True, null=True)
    stop_ind = models.FloatField(blank=True, null=True)
    price_in = models.FloatField(blank=True, null=True)
    price_out = models.FloatField(blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    pnl = models.FloatField(blank=True, null=True)
    start_ind = models.FloatField(blank=True, null=True)
    end_ind = models.FloatField(blank=True, null=True)
    start_date = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    pnl_money = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    vol_2 = models.FloatField(blank=True, null=True)
    strat = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sd_2'


class SellFf(models.Model):
    id_ul = models.BigIntegerField(primary_key=True)
    count_sell_wb_30 = models.BigIntegerField(blank=True, null=True)
    count_sell_ozon_30 = models.BigIntegerField(blank=True, null=True)
    count_sell_wb_60 = models.BigIntegerField(blank=True, null=True)
    count_sell_ozon_60 = models.BigIntegerField(blank=True, null=True)
    count_sell_wb_120 = models.BigIntegerField(blank=True, null=True)
    count_sell_ozon_120 = models.BigIntegerField(blank=True, null=True)
    count_sell_wb_max = models.BigIntegerField(blank=True, null=True)
    count_sell_ozon_max = models.BigIntegerField(blank=True, null=True)
    back_fbs = models.BigIntegerField(blank=True, null=True)
    ff_city = models.BigIntegerField(blank=True, null=True)
    count_pack_fbs = models.BigIntegerField(blank=True, null=True)
    comment_pack_fbs = models.CharField(max_length=300, blank=True, null=True)
    count_pal_fbs = models.BigIntegerField(blank=True, null=True)
    count_sell_ya_30 = models.BigIntegerField(blank=True, null=True)
    count_sell_ya_60 = models.BigIntegerField(blank=True, null=True)
    count_sell_ya_120 = models.BigIntegerField(blank=True, null=True)
    count_sell_ya_max = models.BigIntegerField(blank=True, null=True)
    count_sell_cdek_30 = models.BigIntegerField(blank=True, null=True)
    count_sell_cdek_60 = models.BigIntegerField(blank=True, null=True)
    count_sell_cdek_120 = models.BigIntegerField(blank=True, null=True)
    count_sell_cdek_max = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sell_ff'


class ShippingFf(models.Model):
    id_ship = models.BigAutoField(primary_key=True)
    id_client_ship = models.CharField(max_length=90, blank=True, null=True)
    date_ship = models.CharField(max_length=45, blank=True, null=True)
    num_ship = models.FloatField(blank=True, null=True)
    phone_begin = models.CharField(max_length=45, blank=True, null=True)
    phone_end = models.CharField(max_length=45, blank=True, null=True)
    time_ship = models.CharField(max_length=100, blank=True, null=True)
    item_ship = models.CharField(max_length=1000, blank=True, null=True)
    count_item_ship = models.CharField(max_length=45, blank=True, null=True)
    adress_begin = models.CharField(max_length=300, blank=True, null=True)
    adress_end = models.CharField(max_length=300, blank=True, null=True)
    type_ship = models.CharField(max_length=90, blank=True, null=True)
    begin_ship = models.CharField(max_length=45, blank=True, null=True)
    end_ship = models.CharField(max_length=45, blank=True, null=True)
    w_ship = models.CharField(max_length=45, blank=True, null=True)
    comment_ship = models.CharField(max_length=500, blank=True, null=True)
    status_ship = models.CharField(max_length=45, blank=True, null=True)
    nons = models.CharField(max_length=500, blank=True, null=True)
    car_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_ff'


class SokemCars(models.Model):
    id_car = models.BigAutoField(primary_key=True)
    name_car = models.CharField(max_length=45, blank=True, null=True)
    vin_car = models.CharField(max_length=100, blank=True, null=True)
    num_car = models.CharField(max_length=45, blank=True, null=True)
    dv_car = models.CharField(max_length=100, blank=True, null=True)
    oildv_car = models.CharField(max_length=100, blank=True, null=True)
    kmoildv_car = models.CharField(max_length=45, blank=True, null=True)
    fuel_car = models.CharField(max_length=45, blank=True, null=True)
    trans_car = models.CharField(max_length=100, blank=True, null=True)
    oiltr_car = models.CharField(max_length=100, blank=True, null=True)
    kmoiltr_car = models.CharField(max_length=45, blank=True, null=True)
    wheelwin_car = models.CharField(max_length=100, blank=True, null=True)
    wheelsum_car = models.CharField(max_length=100, blank=True, null=True)
    own_car = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sokem_cars'


class SokemHitems(models.Model):
    id_item = models.BigAutoField(primary_key=True)
    name_item = models.CharField(max_length=100, blank=True, null=True)
    own_item = models.BigIntegerField(blank=True, null=True)
    need_item = models.CharField(max_length=3, blank=True, null=True)
    cat_item = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sokem_hitems'


class SokemUsers(models.Model):
    id_user = models.BigIntegerField(primary_key=True)
    name_user = models.CharField(max_length=45, blank=True, null=True)
    act = models.CharField(max_length=200, blank=True, null=True)
    json_user = models.CharField(max_length=3000, blank=True, null=True)
    type_user = models.CharField(max_length=300, blank=True, null=True)
    mes_id = models.CharField(max_length=1000, blank=True, null=True)
    ref_day = models.BigIntegerField(blank=True, null=True)
    ref_user = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sokem_users'


class SupHelps(models.Model):
    id_help = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey('SupUsers', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    text_help = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sup_helps'


class SupItems(models.Model):
    id_item = models.BigAutoField(primary_key=True)
    name_item = models.CharField(max_length=20, blank=True, null=True)
    name_bot = models.ForeignKey(AdminBots, models.DO_NOTHING, db_column='name_bot', blank=True, null=True)
    arch = models.BigIntegerField(blank=True, null=True)

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

    class Meta:
        managed = False
        db_table = 'sup_news'


class SupReqs(models.Model):
    id_req = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey('SupUsers', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    id_item = models.ForeignKey(SupItems, models.DO_NOTHING, db_column='id_item', blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'sup_users'


class UlFf(models.Model):
    id_ul = models.BigAutoField(primary_key=True)
    name_ul = models.CharField(max_length=45, blank=True, null=True)
    arch_ul = models.CharField(max_length=45, blank=True, null=True)
    id_tg = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ul_ff'


class UsersFf(models.Model):
    id_user = models.BigIntegerField(primary_key=True)
    name_user = models.CharField(max_length=45, blank=True, null=True)
    company = models.CharField(max_length=45, blank=True, null=True)
    act = models.CharField(max_length=1000, blank=True, null=True)
    id_list = models.CharField(max_length=4000, blank=True, null=True)
    barcodes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_ff'


class WorkDriveFf(models.Model):
    date_work = models.CharField(primary_key=True, max_length=45)
    crash_auto = models.CharField(max_length=1000, blank=True, null=True)
    km_auto = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_drive_ff'


class WorkFf(models.Model):
    date_work = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'work_ff'


class WorkShipBeginFf(models.Model):
    date_work = models.CharField(primary_key=True, max_length=90)

    class Meta:
        managed = False
        db_table = 'work_ship_begin_ff'


class WorkShipFf(models.Model):
    id_ws = models.AutoField(primary_key=True)
    date_work = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_ship_ff'
