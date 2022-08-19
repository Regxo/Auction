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
  current_highest_bid = [0.0]
  item_bids = [0]
  item_description = []
  reserve_price = []
  item_numbers = []
  buyer_no_Array = [0]
