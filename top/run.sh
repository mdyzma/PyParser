#!/bin/bash
for dir in top/*;
	do
		if [ -d $dir ]
			then
				dir=${dir%*/}
				echo ${dir##*/}
				# python aaparser.py ${dir##*/} && python bondsparser.py ${dir##*/} && python atomname2pdb.py ${dir##*/};
				# python aaparser.py ${dir##*/} && python bondsparser.py ${dir##*/}&&python dihedralsparser.py ${dir##*/};
				# && python dihedralsparser.py ${dir##*/}
		fi
	done

