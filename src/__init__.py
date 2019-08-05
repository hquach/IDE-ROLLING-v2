'''  
Author: Hoa Quach
Due Date: 2/13/2018

Python 2.7.6
'''

import sys
import time

from file_parser import *
from process_log import *
from collections import OrderedDict

if __name__ == '__main__':
	def get_signal():
		'''Main Function to process percentile calculations, create hash table to identify duplicates, and write output file'''
		f = open( sys.argv[3], 'w')
		constraints(sys.argv[2])

		_filter_by_2017 = filter_by_2017( sys.argv[1] )
		_filter_2018 = filter_by_2018( sys.argv[1] )
		percentile = parse_percentile(sys.argv[2])
		
		dupe_list = OrderedDict()
		hashTable( _filter_2018, dupe_list, _filter_by_2017 )

		index = 0
		transaction_amt = []
		for k,v in dupe_list.items():
			index += 1
			transaction_amt.append(v['trans_amt'])
			for j in cumulative(transaction_amt):
				percentile_value = calc_nearest_rank( dupe_list, percentile, sys.argv[2] )
		print(str("Percentile: ") + str(int(round(_filter_2018[percentile_value]['trans_amt']))) + "|" + str("Total: $") + str(int(round(j)))  + "|" + str("Total Number of Contributions: ") + str(index))
		f.write((str("Percentile: ") + str(int(round(_filter_2018[percentile_value]['trans_amt']))) + "|" + str("Total: $") + str(int(round(j)))  + "|" + str("Total Number of Contributions: ") + str(index)))
		#f.write("\n")
		time.sleep(5)
	while True:
		get_signal()