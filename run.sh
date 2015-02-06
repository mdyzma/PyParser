#!/bin/bash
for i in top/*
	do
		if [ -d $i ]
			then
				echo $i
				python aaparser.py $i && python bondsparser.py $i
#&& python dihedralsparser.py "$subdir";
		fi
	done
