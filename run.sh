source activate exc

hdfs dfs -cat /data/assignments/ex2/part3/webLarge.txt | python bloomfilter.py $1 > temp
hdfs dfs -copyFromLocal output.out /user/$USER/assignment2/task7/part-00000
cat temp | head -20 > output.out
rm temp

source deactivate exc
