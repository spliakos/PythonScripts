#!/usr/bin/python

from collections import OrderedDict

def insert_elem_to_orderedDict(my_orderded_dict, key1, newkey, newval, dict_setitem=dict.__setitem__):
  new_orderded_dict=my_orderded_dict.__class__()
  for key, value in my_orderded_dict.items():
    new_orderded_dict[key]=value
    if key==key1:
      new_orderded_dict[newkey]=newval
  my_orderded_dict.clear()
  my_orderded_dict.update(new_orderded_dict)
  return my_orderded_dict


def orderedDict_prepend(dct, key, value, dict_setitem=dict.__setitem__):
  # [Python version < 3.2]:: For Python 3.2 and later, you should use the move_to_end method. The method accepts a last argument which indicates whether the element will be moved to the bottom (last=True) or the top (last=False) of the OrderedDict.
  root = dct._OrderedDict__root
  first = root[1]

  if key in dct:
    link = dct._OrderedDict__map[key]
    link_prev, link_next, _ = link
    link_prev[1] = link_next
    link_next[0] = link_prev
    link[0] = root
    link[1] = first
    root[1] = first[0] = link
  else:
    root[1] = first[0] = dct._OrderedDict__map[key] = [root, first, key]
    dict_setitem(dct, key, value)



'''
#EXAMPLES::
my_orderded_dict=OrderedDict([('one', 1), ('three', 3)])
insert_elem_to_orderedDict(my_orderded_dict, 'one', 'two', 2)
print my_orderded_dict

my_orderded_dict=OrderedDict([('one', 1), ('three', 3)])
orderedDict_prepend(my_orderded_dict, 'two', 2)
print my_orderded_dict
'''