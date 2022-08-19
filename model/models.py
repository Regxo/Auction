from django.db import models

class item(models.Model):
  item_name = ''
  number_of_bids = 0
  count = 0
  auction_fee = 0.0
  item_no = 0
  sold_items = 0
  less_than_reserve = 0
  zero_bids_items = 0
  min_items = 10
  current_highest_bid = [0.0]*n
  item_bids = [0]*n
  item_description = []*n
  reserve_price = []*n
  item_numbers = []*n
  buyer_no_Array = [0]*n
