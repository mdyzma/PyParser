for dir in `ls $top`;
do
    for subdir in `ls $top/$dir`;
    do
      $(python aaparser.py);
    done
done
